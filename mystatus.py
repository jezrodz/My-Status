#!/usr/bin/env python

import random

#ANG STATUS NG BUHAY MO/My Status

def anopangalanmo():
    #asks a users name
    name = input("Anong pangalan mo? : ")
     #1sst answer to the question            
    if name[:1] == "j":
            print("nag sisimula sa j, Di ka kontento sa isang jowa!")
    #another answer to the question
    elif name[:1] == "k":
            print("Ahy loyal to!")
    #another answer to the question
    else:
            print("tatanda kang single.")
#asks if a user has girlfriend
def mayjowaka():

    jowa = input("may jowa ka ngayon? ")
#1st answer
    if jowa[:1] == "w":
            print("hina mo naman! ano hinihintay mo? ex mo?!!!")
#2nd answer    
    elif jowa[:1] == "m":
            print("Naks, Sanaol! Mag bbreak din naman kayo! dont worry :) ")
 #other answer
    else:
            print("okay!")

def ilannajowamo():
#ask a user if how many gf he/she had
    ilan = int(input("Naka ilang jowa ka na? "))
#answer 1
    if ilan == 1:
            print("boring! double time aba!")
#answer 2
    elif ilan == 2:
            print("Okay keep up!")
#answer 3
    elif ilan == 3:
            print("pwede na din!")
#answer 4
    elif ilan == 4:
            print("mag seryoso ka naman")
 #answer 5
    elif ilan > 4:
            print("lakas mo!! kakarmahin ka din!")

#call of a function
anopangalanmo()
mayjowaka()
ilannajowamo()