import sys
sys.path.insert(0, '../')
from models import *
import random
import time

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
    ss = adminmodels.Sessions(sessid=new_sess_id,vote_game='[[0,0,0],[0,0,0],[0,0,0]]')
    ss.put()
    time.sleep(2)
    print("session with %d was input" % new_sess_id)
    print(type(new_sess_id))
    return new_sess_id

def usertoken(userid, sessionid):
    if userid == "" or genfunc.queryfield(usermodels.User, "user_id", userid) == []: #no user data 
        userid = random.randint(10000000,99999999)
        uu = usermodels.User(user_id=userid, sessions=[sessionid])
        uu.put()
    else:
        uu = genfunc.queryfield(usermodels.User, "user_id", userid)[0]
        print("ELSE and ")
        print(uu.sessions)
        uu.sessions.append(sessionid)
        uu.put()
    s = genfunc.queryfield(adminmodels.Sessions,"sessid",int(sessionid))[0]
    #print("S: {}".format(s))
    s.playernames.append(int(userid))
    s.put()
    return userid
