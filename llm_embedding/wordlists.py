import nltk

from nltk.corpus import wordnet


class Words:
    def __init__(self):
        nltk.download('wordnet')

    def get_bad_words(self):
        bad_words = ['bad', 'worse', 'no', 'ugly']
        synonyms = []
        for word in bad_words:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())
        bad_words.extend(synonyms)
        bad_words = list(set(bad_words))
        bad_words.sort()
        bad_words =  [
                                'abysmal',
                                'adverse',
                                'alarming',
                                'angry',
                                'annoy',
                                'anxious',
                                'apathy',
                                'appalling',
                                'atrocious',
                                'awful',
                                'B',
                                'bad',
                                'banal',
                                'barbed',
                                'belligerent',
                                'bemoan',
                                'beneath',
                                'boring',
                                'broken',
                                'C',
                                'callous',
                                "can't",
                                'clumsy',
                                'coarse',
                                'cold',
                                'cold-hearted',
                                'collapse',
                                'confused',
                                'contradictory',
                                'contrary',
                                'corrosive',
                                'corrupt',
                                'crazy',
                                'creepy',
                                'criminal',
                                'cruel',
                                'cry',
                                'cutting',
                                'D',
                                'damage',
                                'damaging',
                                'dastardly',
                                'dead',
                                'decaying',
                                'deformed',
                                'deny',
                                'deplorable',
                                'depressed',
                                'deprived',
                                'despicable',
                                'detrimental',
                                'dirty',
                                'disease',
                                'disgusting',
                                'disheveled',
                                'dishonest',
                                'dishonorable',
                                'dismal',
                                'distress',
                                "don't",
                                'dreadful',
                                'dreary',
                                'E',
                                'enraged',
                                'eroding',
                                'evil',
                                'F',
                                'fail',
                                'faulty',
                                'fear',
                                'feeble',
                                'fight',
                                'filthy',
                                'foul',
                                'frighten',
                                'frightful',
                                'G',
                                'gawky',
                                'ghastly',
                                'grave',
                                'greed',
                                'grim',
                                'grimace',
                                'gross',
                                'grotesque',
                                'gruesome',
                                'guilty',
                                'H',
                                'haggard',
                                'hard',
                                'hard-hearted',
                                'harmful',
                                'hate',
                                'hideous',
                                'homely',
                                'horrendous',
                                'horrible',
                                'hostile',
                                'hurt',
                                'hurtful',
                                'I',
                                'icky',
                                'ignorant',
                                'ignore',
                                'ill',
                                'immature',
                                'imperfect',
                                'impossible',
                                'inane',
                                'inelegant',
                                'infernal',
                                'injure',
                                'injurious',
                                'insane',
                                'insidious',
                                'insipid',
                                'J',
                                'jealous',
                                'junky',
                                'L',
                                'lose',
                                'lousy',
                                'lumpy',
                                'M',
                                'malicious',
                                'mean',
                                'menacing',
                                'messy',
                                'misshapen',
                                'missing',
                                'misunderstood',
                                'moan',
                                'moldy',
                                'monstrous',
                                'N',
                                'naive',
                                'nasty',
                                'naughty',
                                'negate',
                                'negative',
                                'never',
                                'no',
                                'nobody',
                                'nondescript',
                                'nonsense',
                                'not',
                                'noxious',
                                'O',
                                'objectionable',
                                'odious',
                                'offensive',
                                'old',
                                'oppressive',
                                'P',
                                'pain',
                                'perturb',
                                'pessimistic',
                                'petty',
                                'plain',
                                'poisonous',
                                'poor',
                                'prejudice',
                                'Q',
                                'questionable',
                                'quirky',
                                'quit',
                                'R',
                                'reject',
                                'renege',
                                'repellant',
                                'reptilian',
                                'repugnant',
                                'repulsive',
                                'revenge',
                                'revolting',
                                'rocky',
                                'rotten',
                                'rude',
                                'ruthless',
                                'S',
                                'sad',
                                'savage',
                                'scare',
                                'scary',
                                'scream',
                                'severe',
                                'shocking',
                                'shoddy',
                                'sick',
                                'sickening',
                                'sinister',
                                'slimy',
                                'smelly',
                                'sobbing',
                                'sorry',
                                'spiteful',
                                'sticky',
                                'stinky',
                                'stormy',
                                'stressful',
                                'stuck',
                                'stupid',
                                'substandard',
                                'suspect',
                                'suspicious',
                                'T',
                                'tense',
                                'terrible',
                                'terrifying',
                                'threatening',
                                'U',
                                'ugly',
                                'undermine',
                                'unfair',
                                'unfavorable',
                                'unhappy',
                                'unhealthy',
                                'unjust',
                                'unlucky',
                                'unpleasant',
                                'unsatisfactory',
                                'unsightly',
                                'untoward',
                                'unwanted',
                                'unwelcome',
                                'unwholesome',
                                'unwieldy',
                                'unwise',
                                'upset',
                                'V',
                                'vice',
                                'vicious',
                                'vile',
                                'villainous',
                                'vindictive',
                                'W',
                                'wary',
                                'weary',
                                'wicked',
                                'woeful',
                                'worthless',
                                'wound',
                                'Y',
                                'yell',
                                'yucky',
                                'Z',
                                'zero'
                                ]
        bad_words = [bad_word  for bad_word in bad_words if len(bad_word) > 1]
        return bad_words

    def get_good_words(self):
        good_words = ['good', 'better', 'yes', 'nice']
        synonyms = []
        for word in good_words:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())
        good_words.extend(synonyms)
        good_words = list(set(good_words))
        good_words.sort()
        good_words = ["absolutely",
                        "accepted",
                        "acclaimed",
                        "accomplish",
                        "accomplishment",
                        "achievement",
                        "action",
                        "active",
                        "admire",
                        "adorable",
                        "adventure",
                        "affirmative",
                        "affluent",
                        "agree",
                        "agreeable",
                        "amazing",
                        "angelic",
                        "appealing",
                        "approve",
                        "aptitude",
                        "attractive",
                        "awesome",
                        "B",
                        "beaming",
                        "beautiful",
                        "believe",
                        "beneficial",
                        "bliss",
                        "bountiful",
                        "bounty",
                        "brave",
                        "bravo",
                        "brilliant",
                        "bubbly",
                        "C",
                        "calm",
                        "celebrated",
                        "certain",
                        "champ",
                        "champion",
                        "charming",
                        "cheery",
                        "choice",
                        "classic",
                        "classical",
                        "clean",
                        "commend",
                        "composed",
                        "congratulation",
                        "constant",
                        "cool",
                        "courageous",
                        "creative",
                        "cute",
                        "D",
                        "dazzling",
                        "delight",
                        "delightful",
                        "distinguished",
                        "divine",
                        "E",
                        "earnest",
                        "easy",
                        "ecstatic",
                        "effective",
                        "effervescent",
                        "efficient",
                        "effortless",
                        "electrifying",
                        "elegant",
                        "enchanting",
                        "encouraging",
                        "endorsed",
                        "energetic",
                        "energized",
                        "engaging",
                        "enthusiastic",
                        "essential",
                        "esteemed",
                        "ethical",
                        "excellent",
                        "exciting",
                        "exquisite",
                        "F",
                        "fabulous",
                        "fair",
                        "familiar",
                        "famous",
                        "fantastic",
                        "favorable",
                        "fetching",
                        "fine",
                        "fitting",
                        "flourishing",
                        "fortunate",
                        "free",
                        "fresh",
                        "friendly",
                        "fun",
                        "funny",
                        "G",
                        "generous",
                        "genius",
                        "genuine",
                        "giving",
                        "glamorous",
                        "glowing",
                        "good",
                        "gorgeous",
                        "graceful",
                        "great",
                        "green",
                        "grin",
                        "growing",
                        "H",
                        "handsome",
                        "happy",
                        "harmonious",
                        "healing",
                        "healthy",
                        "hearty",
                        "heavenly",
                        "honest",
                        "honorable",
                        "honored",
                        "hug",
                        "I",
                        "idea",
                        "ideal",
                        "imaginative",
                        "imagine",
                        "impressive",
                        "independent",
                        "innovate",
                        "innovative",
                        "instant",
                        "instantaneous",
                        "instinctive",
                        "intellectual",
                        "intelligent",
                        "intuitive",
                        "inventive",
                        "J",
                        "jovial",
                        "joy",
                        "jubilant",
                        "K",
                        "keen",
                        "kind",
                        "knowing",
                        "knowledgeable",
                        "L",
                        "laugh",
                        "learned",
                        "legendary",
                        "light",
                        "lively",
                        "lovely",
                        "lucid",
                        "lucky",
                        "luminous",
                        "M",
                        "marvelous",
                        "masterful",
                        "meaningful",
                        "merit",
                        "meritorious",
                        "miraculous",
                        "motivating",
                        "moving",
                        "N",
                        "natural",
                        "nice",
                        "novel",
                        "now",
                        "nurturing",
                        "nutritious",
                        "O",
                        "okay",
                        "one",
                        "one-hundred percent",
                        "open",
                        "optimistic",
                        "P",
                        "paradise",
                        "perfect",
                        "phenomenal",
                        "pleasant",
                        "pleasurable",
                        "plentiful",
                        "poised",
                        "polished",
                        "popular",
                        "positive",
                        "powerful",
                        "prepared",
                        "pretty",
                        "principled",
                        "productive",
                        "progress",
                        "prominent",
                        "protected",
                        "proud",
                        "Q",
                        "quality",
                        "quick",
                        "quiet",
                        "R",
                        "ready",
                        "reassuring",
                        "refined",
                        "refreshing",
                        "rejoice",
                        "reliable",
                        "remarkable",
                        "resounding",
                        "respected",
                        "restored",
                        "reward",
                        "rewarding",
                        "right",
                        "robust",
                        "S",
                        "safe",
                        "satisfactory",
                        "secure",
                        "seemly",
                        "simple",
                        "skilled",
                        "skillful",
                        "smile",
                        "soulful",
                        "sparkling",
                        "special",
                        "spirited",
                        "spiritual",
                        "stirring",
                        "stunning",
                        "stupendous",
                        "success",
                        "successful",
                        "sunny",
                        "super",
                        "superb",
                        "supporting",
                        "surprising",
                        "T",
                        "terrific",
                        "thorough",
                        "thrilling",
                        "thriving",
                        "tops",
                        "tranquil",
                        "transformative",
                        "transforming",
                        "trusting",
                        "truthful",
                        "U",
                        "unreal",
                        "unwavering",
                        "up",
                        "upbeat",
                        "upright",
                        "upstanding",
                        "V",
                        "valued",
                        "vibrant",
                        "victorious",
                        "victory",
                        "vigorous",
                        "virtuous",
                        "vital",
                        "vivacious",
                        "W",
                        "wealthy",
                        "welcome",
                        "well",
                        "whole",
                        "wholesome",
                        "willing",
                        "wonderful",
                        "wondrous",
                        "worthy",
                        "wow",
                        "Y",
                        "yes",
                        "yummy",
                        "Z",
                        "zeal",
                        "zealous"]
        good_words = [good_word  for good_word in good_words if len(good_word) > 1]
        return good_words

    def get_good_and_bad_words(self):
        bad_words = self.get_bad_words()
        good_words = self.get_good_words()
        bad_label = [0] * len(bad_words)
        good_label = [1] * len(good_words)
        return [*bad_words, *good_words], [*bad_label, *good_label]


if __name__ == "__main__":
    print(Words().get_good_and_bad_words()[0])
