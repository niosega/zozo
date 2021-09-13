import os
from zozo import Zoe

myRenaultUser = os.getenv("RENAULT_USER")
myRenaultPass = os.getenv("RENAULT_PASS")
VIN = os.getenv("RENAULT_VIN")

zoe = Zoe(VIN, myRenaultUser, myRenaultPass)
zoe.getPersonnalInfo()
print(zoe.googleLocation())
# zoe.batteryStatus()
# zoe.location()
# zoe.chargingSettings()
# zoe.cockpit()
# zoe.hvacStatus()
