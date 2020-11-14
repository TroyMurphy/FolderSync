from src.folder_sync import folder_sync
from .penticton_settings import SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX

def penticton_sync():
    folder_sync(SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX)