from sentence_transformers import SentenceTransformer
import torch
from wordlists import Words
import umap
import numpy as np
import random
import os
import pandas as pd 
def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)  # Example seed

# Load a dedicated sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Define two lists of words
list1, labels = Words().get_good_and_bad_words()

# Get sentence embeddings
sentence_embeddings = model.encode(list1)

# Define the path for the embeddings file
embeddings_file_path = 'embeddings_array.npy'

embeddings_array = np.array(sentence_embeddings, dtype=np.float32)

# Perform UMAP on the embeddings
reducer = umap.UMAP(random_state=42)
embedding_umap = reducer.fit_transform(embeddings_array)

import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

classifier = SVC(kernel='linear', random_state=42)
classifier.fit(embedding_umap, labels)

# Create a grid to evaluate the model
x_min, x_max = embedding_umap[:, 0].min() - 1, embedding_umap[:, 0].max() + 1
y_min, y_max = embedding_umap[:, 1].min() - 1, embedding_umap[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Predict on each point in the grid
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)



# Calculate the distance of each point to the decision boundary
distances = classifier.decision_function(embedding_umap)

# Print distances
for i, distance in enumerate(distances):
    print(f'Embedding {i} distance to decision boundary: {distance}')


class_dict = {'distances':distances,
                 'labels':labels,
                 'words': list1,
                 }

df = pd.DataFrame(class_dict)



df['classified_label'] = classifier.predict(embedding_umap)

for ind, row in df.iterrows():
    if row['classified_label'] != row['labels']:
        print(f"{row['words']} - {row['classified_label']} - {row['labels']} - {row['distances']}")

#print(df[df['classified_label'] != df['labels']])

# Plot the results
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(embedding_umap[:, 0], embedding_umap[:, 1], c=labels, edgecolors='k')
plt.colorbar()
plt.show()
exit()
print('first cluster left bottom')
i = 0
for embedding in embedding_umap:
    if classifier.predict(embedding.reshape(1, -1)) == 0:
        print(f'{list1[i]} label: {labels[i]}')
    i += 1

print('second cluster')
i = 0
for embedding in embedding_umap:
    if classifier.predict(embedding.reshape(1, -1)) > 0:
        print(f'{list1[i]} label: {labels[i]}')
    i += 1
