from src.alco.alco_sync import alco_sync
from src.penticton.penticton_sync import penticton_sync
from src.morowat.morowat_sync import morowat_sync

def main():
    alco_sync()
    penticton_sync()
    morowat_sync()

if __name__=="__main__":
    main()