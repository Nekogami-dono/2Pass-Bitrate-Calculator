#2Pass-Bitrate-Calculator
__author__ = "Nekogami"
__version__ = "0.0.2"
__email__ = "dev@nekogami.moe"
__status__ = "Dev"
import math

Targetsize = int(input("Target-Filesize in MiB: "))
Audiobit = int(input("Audio Bitrate: "))
Runtime = input("Runtime hh:mm:ss: ")
minbit = input("Min Bitrate: ")


#Calc Time
timesplit = Runtime.split(":")
hours = int(timesplit[0]) * 60 * 60
minutes = int(timesplit[1]) * 60
SRuntime = minutes + hours + int(timesplit[2])
#Calc Size
Targetsize = (Targetsize)
Targetsize = Targetsize * 8389
Bitrate = (Targetsize) / SRuntime

if not minbit:
    print("Bitrate")
    print(str(round(Bitrate-Audiobit,2)) + " kbps")
else:
    if Bitrate < int(minbit):
       minsize = (int(minbit) + Audiobit) * SRuntime 
       outsize = round((minsize / 8389),2)
       print("With a Bitrate of " + str(minbit) + " kBit your file must be at least")
       print(str(outsize) + " MiB")
       advicedsize = math.ceil((outsize / 1120)) * 1120
       print("Adviced Size: " + str(advicedsize) + " MiB")
    else:
        print("Bitrate")
        print(Audiobit)
        print(str(round(Bitrate-Audiobit,2)) + " kbps")