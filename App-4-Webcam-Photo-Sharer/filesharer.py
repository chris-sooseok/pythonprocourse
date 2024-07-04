
# filestack Cleint is an built-in api provided for users to upload to Filestack
from filestack import Client


class FileSharer:

    def __init__(self, filepath, api_key=""):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(api_key=self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
