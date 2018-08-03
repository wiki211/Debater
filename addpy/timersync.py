import sys
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
from models import adminmodels, genfunc
import datetime

def timedif(sessionid, timeallowed):
    session = genfunc.queryfield(adminmodels.Sessions, "sessid", int(sessionid))[0]
    timedelta = session.session_start - datetime.datetime.now()
    secdelta = timedelta.total_seconds() + timeallowed
    return round(secdelta/60, 6)