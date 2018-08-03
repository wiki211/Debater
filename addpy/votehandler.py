import sys
sys.path.insert(0, '/Users/demouser/Desktop/cssi-project/Debater/')
from models import genfunc, adminmodels
import time

def updateroundnum(sessid, update = False):
    session = genfunc.queryfield(adminmodels.Sessions, "sessid", int(sessid))[0]
    if session.round_num > 3:
        return True, -1
    elif update == False:
        return False, session.round_num
    else:
        session.round_num += 1
        session.put()
        time.sleep(2)
        return False, session.round_num

def updatevotetally(sessid, team):
    session = genfunc.queryfield(adminmodels.Sessions, "sessid", int(sessid))[0]
    round = session.round_num
    vote_list = eval(session.vote_game)
    vote_list[round-1][team-1] += 1
    session.vote_game = str(vote_list)
    session.put()
    time.sleep(2)