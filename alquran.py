import requests
import json
import os
import getpass

def baca_ayat(pilih,surah):
    for x in surah:
        print(surah[x])



def menu_surah():
        asurah = open('surah.json',encoding="utf-8").read()
        surah = json.loads(asurah)
        for x in range(0,len(surah['hasil'])):
                nomor = surah['hasil'][x]['nomor']
                nama = surah['hasil'][x]['nama']
                turun = surah['hasil'][x]['type']
                ayat = surah['hasil'][x]['ayat']
                asma = surah['hasil'][x]['asma']
                arti = surah['hasil'][x]['arti']
                print(f"{nomor}. {nama} ({arti})\n{turun}  |  {ayat} ayat\n")

        pilih = input("Pilih Surah : ")
        surah = open("surah/"+pilih+".json",encoding="utf-8").read()
        s = json.loads(surah)[pilih]['text']
        baca_ayat(pilih,s)

menu_surah()
