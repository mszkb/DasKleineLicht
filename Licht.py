import os
from time import sleep





def wait():
    input("")


def seitelesen(text, timer=0.03):
    """optional Parameterm 0.02 is standard for shell animationed text"""

    with open("storytexts/" + text + ".txt") as f:
        content = f.read()

    charlist = list(content)

    for char in charlist:
        print(char, end="", flush=True)
        sleep(timer)


def bildanschauen(text, timer=0.00):
    seitelesen(text, timer)


def umblaettern():
    os.system("clear")


def buchaufschlagen():
    os.system("clear")



buchaufschlagen()


seitelesen("kap1")
wait()
bildanschauen("/bilder/sonne")
wait()
umblaettern()

seitelesen("kap2")
wait()
bildanschauen("/bilder/andereLichter")
wait()
umblaettern()

seitelesen("kap3")
wait()
bildanschauen("/bilder/tanzen")
wait()
umblaettern()

seitelesen("kap4")
wait()
bildanschauen("/bilder/vorhoehle")
wait()
umblaettern()

seitelesen("kap5")
wait()
bildanschauen("/bilder/inhoehle")
wait()
umblaettern()

seitelesen("kap6")
wait()
bildanschauen("/bilder/endehoehle")
wait()
umblaettern()

seitelesen("kap7")
wait()
bildanschauen("/bilder/sonneweg")
wait()
umblaettern()

seitelesen("kap8")
wait()
bildanschauen("/bilder/kugel")
wait()
umblaettern()

seitelesen("kap9")
wait()
bildanschauen("/bilder/mond")
wait()
umblaettern()

seitelesen("kap10")
wait()
bildanschauen("/bilder/wiederbeisonne")
wait()
umblaettern()

