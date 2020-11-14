from src.folder_sync import folder_sync
from .morowat_settings import SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX

def morowat_sync():
    return folder_sync(SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX)