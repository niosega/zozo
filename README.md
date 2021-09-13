# Python API to query Renault Zoe information.

# Installation
```
virtualenv -v venv -p python3
pip install -r requirement.txt
```

# Launch
```
. venv/bin/activate
export RENAULT_USER=<myRenaultUser>
export RENAULT_PASS_=<myRenaultPass>
export RENAULT_VIN=<VIN>
python main.py
```

The program create three file : `firststep.dta`, `secondstep.dta` and `thirdstep.dta` that contains cache response from Renault server. This file are created in order not to reach the server quota. You can safely remove these three files.

# API
Before doing anything, you have to call the method `getPersonnalInfo`.

```
zoe = Zoe(VIN, user, password)
zoe.getPersonnalInfo()
# Then, you can use API methods.
```

# Thanks
Big thanks to [dehsgr](https://gist.github.com/dehsgr/32c4d3dd5f8125be3a4c66d04e41d9b8).