import sys
sys.path.insert(0, '../')
from models import *

def checksessionid(inputid):
    idcheck = genfunc.queryfield(adminmodels.Sessions,"sessid", inputid)
    if len(idcheck) == 1: #if it's not empty
        return True
    else:
        return False
