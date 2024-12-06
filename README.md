# APRS updating by Python
This is a very simple APRS python script that uses a socket to update a HAM operators current location.  
  
  
The results are found by looking up the call-sign of the radio operator on  

[aprs.fi](http://aprs.fi)

---
  
You should either create your own support file called aprs_secinfo.py that has a class of the same name, or replace  
  the tags in the send_aprs.py file with your own data using strings  
Here is a sample of a support script that holds authentication information.  

```
class aprs_secinfo():
    def __init__(self):
        self.CALLSIGN = "YOUR_CALL_SIGN_GOES_HERE"      # Replace with your callsign
        self.PASSCODE = "YOUR_PASSCODE_GOES_HERE"       # Replace with your APRS passcode
        self.LATITUDE = "4021.41N"                      # Replace with your latitude
        self.LONGITUDE = "11143.28W"                    # Replace with your longitude
        self.COMMENT = "APRS via Python script"  		# Optional status comment
        self.SYMBOL_CODE = "-"							# This indicates a house icon for APRS

    def about(self):
        print("APRS information about this users ham call sign and passcode to APRS")
```
You get your APRS passcode from this web-site, using your call-sign  
[PASSCODE-GENERATOR](https://n5dux.com/ham/aprs-passcode/)
  
---
This section of the main code *send_aprs.py* uses what was placed in the *aprs_secinfo.py*  
file or you can simply add your own string here and delete the instance of *aprssec*  
from the code.
  
```
APRS_SERVER = "rotate.aprs2.net"  # APRS-IS server
APRS_PORT = 14580                # APRS-IS port
aprssec = aprs_secinfo()

CALLSIGN = aprssec.CALLSIGN       # Replace with your callsign
PASSCODE = aprssec.PASSCODE      # Replace with your APRS passcode
LATITUDE = aprssec.LATITUDE            # Replace with your latitude
LONGITUDE = aprssec.LONGITUDE          # Replace with your longitude
COMMENT = aprssec.COMMENT            # Optional status comment
SYMBOL_CODE = aprssec.SYMBOL_CODE
```