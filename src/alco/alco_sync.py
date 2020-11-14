from src.folder_sync import folder_sync
from .alco_settings import SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX

def alco_sync():
    return sync_alco_folder()
    #watermark_documents()

def sync_alco_folder():
    return folder_sync(SOURCE_DIRECTORY, TARGET_DIRECTORY, SUFFIX)

def watermark_documents():
    pass