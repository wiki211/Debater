import sys
sys.path.insert(0, '../')
from models import *
import random

def createsess(inputsessid, score='[]'):
    dd = adminmodels.Sessions(sessid=inputsessid,vote_game=score)
    dd.put()

def getsessionid():
    # array of previous values
    sess_id = genfunc.queryfield(adminmodels.Otherdatastore, "propname", "sessionids" )

    if sess_id == []:
        new_sess_id = random.randint(10000000,99999999)
        dd = adminmodels.Otherdatastore(propname="sessionids", genval=[new_sess_id])
        dd.put()
    elif len(sess_id[0].genval) == 0:
        new_sess_id = random.randint(10000000,99999999)
        sess_id[0].genval = [new_sess_id]
        sess_id[0].put()
    else:
        new_sess_id = random.randint(10000000,99999999)
        n = 0
        while sess_id[0].genval.count(new_sess_id) != 0 or n<100:
            n+=1
            new_sess_id = random.randint(10000000,99999999)
        sess_id[0].genval.append(new_sess_id)
        sess_id[0].put()
    #make session entity code HEREEEEE
    createsess(new_sess_id, score='[[0,0,0],[0,0,0],[0,0,0]]')
    return new_sess_id