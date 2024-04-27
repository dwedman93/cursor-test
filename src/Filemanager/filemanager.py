import os
import hashlib
from typing import Optional, Dict, List
import logging

class FileManager:
    """
    Abstract base class for managing files across various storage systems like blob, sftp, smb, ftp, etc.
    This class provides a framework for file operations such as creating, deleting, moving, uploading files, and retrieving file information.
    """
    def __init__(self, config: Dict):
        """
        Initialize the FileManager with specific configuration.

        Args:
            config (dict): Configuration specific to the file manager subclass.
        """
        self.config = config
        logging.basicConfig(level=logging.INFO)

    def create_file(self, file_path: str, config: Optional[Dict] = None):
        """
        Create a file at the specified path with optional configuration.

        Args:
            file_path (str): The path where the file should be created.
            config (dict, optional): Additional configuration for file creation.

        Raises:
            NotImplementedError: If the method is not overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def delete_file(self, file_path: str, config: Optional[Dict] = None):
        """
        Delete a file from the specified path with optional configuration.

        Args:
            file_path (str): The path of the file to be deleted.
            config (dict, optional): Additional configuration for file deletion.

        Raises:
            NotImplementedError: If the method is not overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def put_file(self, local_file: str, remote_file: str, config: Optional[Dict] = None):
        """
        Upload a file from a local path to a remote path using specific configurations.

        Args:
            local_file (str): The local file path.
            remote_file (str): The remote file path where the file should be uploaded.
            config (dict, optional): Configuration specific to the file manager subclass for uploading the file.

        Raises:
            NotImplementedError: If the method is not overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def download_file(self, remote_file: str, local_path: Optional[str] = None, config: Optional[Dict] = None):
        """
        Download a file to a local path, if not specified use default temp path.

        Args:
            remote_file (str): The remote file path to download.
            local_path (str, optional): The local path where the file should be downloaded.
            config (dict, optional): Configuration specific to the file manager subclass for downloading the file.

        Raises:
            NotImplementedError: If the method is not overridden by subclasses.
        """
        if local_path is None:
            # Create a default path if none is provided
            class_name = self.__class__.__name__
            file_name = os.path.basename(remote_file)
            hash_digest = hashlib.md5(file_name.encode()).hexdigest()  # Using MD5 for example
            default_directory = f"/tmp/{class_name}/{hash_digest}"
            os.makedirs(default_directory, exist_ok=True)
            local_path = os.path.join(default_directory, file_name)

        self._download_file_impl(remote_file, local_path, config)

    def _download_file_impl(self, remote_file: str, local_path: str, config: Optional[Dict] = None):
        """
        Actual implementation of the file download logic, to be overridden by subclasses.

        Args:
            remote_file (str): The remote file path to download.
            local_path (str): The local path where the file should be downloaded.
            config (dict, optional): Configuration specific to the file manager subclass for downloading the file.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def list_dir(self, directory_path: str) -> List[str]:
        """
        List all entries in the directory given by directory_path.

        Args:
            directory_path (str): The path of the directory to list.

        Returns:
            List[str]: A list of names of entries in the directory.
        """
        try:
            return os.listdir(directory_path)
        except OSError as e:
            logging.error(f"Failed to list directory {directory_path}: {e}")
            raise

    def list_tree(self, directory_path: str) -> List[str]:
        """
        List all files and directories in the directory tree rooted at directory_path.

        Args:
            directory_path (str): The root directory path.

        Returns:
            List[str]: A list of paths to all files and directories in the tree.
        """
        tree = []
        for root, dirs, files in os.walk(directory_path):
            tree.append(root)
            for file in files:
                tree.append(os.path.join(root, file))
        return tree

    def list_files(self, directory_path: str) -> List[str]:
        """
        List all files in the directory given by directory_path.

        Args:
            directory_path (str): The path of the directory to list files from.

        Returns:
            List[str]: A list of file names in the directory.
        """
        files = []
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            if os.path.isfile(full_path):
                files.append(entry)
        return files

    def list_folders(self, directory_path: str) -> List[str]:
        """
        List all folders in the directory given by directory_path.

        Args:
            directory_path (str): The path of the directory to list folders from.

        Returns:
            List[str]: A list of folder names in the directory.
        """
        folders = []
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            if os.path.isdir(full_path):
                folders.append(entry)
        return folders

    def list_files_tree(self, directory_path: str) -> List[str]:
        """
        List all files in the directory tree rooted at directory_path.

        Args:
            directory_path (str): The root directory path.

        Returns:
            List[str]: A list of paths to all files in the tree.
        """
        files = []
        for root, dirs, files_in_dir in os.walk(directory_path):
            for file in files_in_dir:
                files.append(os.path.join(root, file))
        return files
