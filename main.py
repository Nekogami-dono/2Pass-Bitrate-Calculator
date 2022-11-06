#2Pass-Bitrate-Calculator
__author__ = "Nekogami"
__version__ = "0.0.1"
__email__ = "dev@nekogami.moe"
__status__ = "Dev"


Targetsize = int(input("Target-Filesize in MiB: "))
Audiobit = int(input("Aduio Bitrate: "))
Runtime = int(input("Runtime in M: "))
Targetsize = Targetsize * 8389
SRuntime = Runtime * 60
Bitrate = (Targetsize - Audiobit) / SRuntime
print("Bitrate")
print(Bitrate)
