from src.alco.alco_sync import alco_sync
from src.penticton.penticton_sync import penticton_sync
from src.morowat.morowat_sync import morowat_sync

"""
To run this project:
1. In folder_sync.py, confirm whether to import testDirectoryList or directoryList
2. In settings.py, update the SOURCE variable
"""

def main():
    threads = alco_sync()
    join_threads(threads)

    threads = penticton_sync()
    join_threads(threads)

    threads = morowat_sync()
    join_threads(threads)

    print("Finished Sync. Hooray!")

def join_threads(threads_list):
    for t in threads_list:
        t.join()

if __name__=="__main__":
    main()