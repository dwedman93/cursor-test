from dagster import ConfigurableResource, get_dagster_logger
from filemanager import FileManager
from typing import Optional, Dict
class BlobManager(ConfigurableResource,FileManager):
    def __init__(self, config):
        super().__init__(config)
        logging.info("BlobManager initialized with configuration.")

    def create_file(self, file_path: str, config: Optional[Dict] = None):
        logging.info(f"Creating file at {file_path} with config {config}")
        # Implementation for creating a file in blob storage
        raise NotImplementedError("Create file method is not implemented for BlobManager.")

    def delete_file(self, file_path: str, config: Optional[Dict] = None):
        logging.info(f"Deleting file at {file_path} with config {config}")
        # Implementation for deleting a file from blob storage
        raise NotImplementedError("Delete file method is not implemented for BlobManager.")

    def put_file(self, local_file: str, remote_file: str, config: Optional[Dict] = None):
        logging.info(f"Uploading file from {local_file} to {remote_file} with config {config}")
        # Implementation for uploading a file to blob storage
        raise NotImplementedError("Put file method is not implemented for BlobManager.")

    def download_file(self, remote_file: str, local_path: Optional[str] = None, config: Optional[Dict] = None):
        logging.info(f"Downloading file from {remote_file} to {local_path} with config {config}")
        # Implementation for downloading a file from blob storage
        raise NotImplementedError("Download file method is not implemented for BlobManager.")
