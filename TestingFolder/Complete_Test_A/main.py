#import modules
import StartSchermTest1
import CMDR
import PLT
import FD

#variabelen
rol = None

#run Startscherm 
rol = StartSchermTest1.Startscherm_prog()
print(rol)

#run verschillende rollen

if rol == "CMDR":
    CMDR.CMDR_prog()
elif rol == "PLT":
    PLT.PLT_prog()
elif rol == "FD":
    FD.FD_prog()
elif rol == "WXT":
    print("weermand programma")
elif rol == "LD":
    print("launch director programma")
elif rol == "ELSS":
    print("entry and landing, etc man programma")
elif rol == "SSO":
    print("Spacecraft Systems Officer programma")
elif rol == "PAO":
    print("Pupblic Affairs Officer programma")