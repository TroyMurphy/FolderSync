import pathlib
from SyncFile import SyncFile

class SyncFileFactory():
    def CreateSyncFile(self, path):
        return SyncFile(path)

    def CreateSyncFileWithVersion(self):
        return SyncFile(r".\source\Example - Rev 1")

    def CreateSyncFileWithoutVersion(self):
        return SyncFile(r".\source\Example")

