#2Pass-Bitrate-Calculator
__author__ = "Nekogami"
__version__ = "0.0.3"
__status__ = "Dev"
import math

Targetsize = int(input("Target-Filesize in MB: "))
Audiobit = int(input("Audio Bitrate in kBit: "))
Runtime = input("Runtime hh:mm:ss: ")
minbit = input("Min Bitrate in kBit: ")


#Calc Time
timesplit = Runtime.split(":")
hours = int(timesplit[0]) * 60 * 60
minutes = int(timesplit[1]) * 60
SRuntime = minutes + hours + int(timesplit[2])
#Calc Size
Targetsize = (Targetsize)
Targetsize = Targetsize * 8000
Bitrate = (Targetsize) / SRuntime

if not minbit:
    print("Bitrate")
    print(str(round(Bitrate-Audiobit,2)) + " kBit")
else:
    if Bitrate < int(minbit):
       minsize = (int(minbit) + Audiobit) * SRuntime 
       outsize = round((minsize / 8000),2)
       print("With a Bitrate of " + str(minbit) + " kBit your file must be at least")
       print(str(outsize) + " MB")
       advicedsize = math.ceil((outsize / 1120)) * 1120
       print("Adviced Size: " + str(advicedsize) + " MB")
    else:
        print("Bitrate: ")
        print(str(round(Bitrate-Audiobit,2)) + " kBit")