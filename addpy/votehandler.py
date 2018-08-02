import sys
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
from models import genfunc, adminmodels
import time

def updateroundnum(sessid):
    session = genfunc.queryfield(adminmodels.Sessions, "sessid", sessid)[0]
    session.round_num += 1
    session.put()
    time.sleep(2)
    return session.round_num
