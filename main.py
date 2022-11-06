#2Pass-Bitrate-Calculator
__author__ = "Nekogami"
__version__ = "0.0.2"
__email__ = "dev@nekogami.moe"
__status__ = "Dev"


Targetsize = int(input("Target-Filesize in MiB: "))
Audiobit = int(input("Audio Bitrate: "))
Runtime = input("Runtime hh:mm:ss: ")

#Calc Time
timesplit = Runtime.split(":")
hours = int(timesplit[0]) * 60 * 60
minutes = int(timesplit[1]) * 60
SRuntime = minutes + hours + int(timesplit[2])
#Calc Size
Targetsize = Targetsize * 8389
Bitrate = (Targetsize - Audiobit) / SRuntime
print("Bitrate")
print(str(round(Bitrate,2)) + " kbps")