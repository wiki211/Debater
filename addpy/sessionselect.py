import sys
sys.path.insert(0, '../')
from models import *

def checksessionid(inputid):
    idcheck = genfunc.queryfield(adminmodels.Sessions,
         "sessid", str(inputid))
    if idcheck != []: #if it's not empty
        return True
    else:
        return False
