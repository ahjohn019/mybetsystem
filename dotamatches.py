import requests
import json
import schedule
import time
from myproject.wsgi import *
from esportlist_db.models import nextmatches, listmatches, livematches
from datetime import datetime
import urllib3
urllib3.disable_warnings()

#dota api upcoming macthes   
def getupcomingmatches():
    dotaupcomingmatch = requests.get('https://api.pandascore.co/dota2/matches/upcoming?token=M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI')
    data = json.loads(dotaupcomingmatch.text)

    for d in data:
        print('Upcoming Matches')
        if len(d['opponents']) != 1 and len(d['opponents']) != 0:
            if len(d['opponents']) == 0:
                pass

            else:
                datetime_beginat = d['begin_at']
                convertstrptime = datetime.strptime(datetime_beginat,"%Y-%m-%dT%H:%M:%SZ")
                stringdatetime = convertstrptime.strftime("%Y-%m-%d %H:%M:%S")
                
                #create the upcoming matches data
                insertnextmatch = nextmatches(leaguename=d['league']['name'],games_id=d['id'],opponent_one=d['opponents'][0]['opponent']['name']
                                    ,opponent_two=d['opponents'][1]['opponent']['name'],datetime=stringdatetime)      
                insertnextmatch.save()

        #remove duplicate after update from api
        for row in nextmatches.objects.all():
            if nextmatches.objects.filter(games_id=d['id']).count() > 1:
                row.delete()

        #update request form oddbet to db (needtemplate)

        
def retrievenextmatches():
    db_nextmatches = nextmatches.objects.all()
    for i in db_nextmatches:
        print(i.leaguename)

#dota api live macthes       
def createlivematches():
    token = 'M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI'
    dotalivematch = requests.get('https://api.pandascore.co/dota2/matches/running?token={0}'.format(token),verify=False)       
    data = json.loads(dotalivematch.text)  
    urllib3.disable_warnings()

    for d in data:
        leaguename = d['league']['name']
        beginat = d['begin_at']
        opponent_one = d['opponents'][0]['opponent']['name']
        opponent_two = d['opponents'][1]['opponent']['name']
        livescore_opone = d['results'][0]['score']
        livescore_optwo = d['results'][1]['score']
        matches_id = d['id']
        matches_status = d['status']

        insertlivematch = livematches(leaguename=leaguename,matches_id=matches_id,datetime=beginat,opponent_one=opponent_one,opponent_two=opponent_two
                                    ,livescore_opone=livescore_opone,livescore_optwo=livescore_optwo,matches_status=matches_status)
        insertlivematch.save()

        #remove duplicate after update from api
        for row in livematches.objects.all():
            if livematches.objects.filter(matches_id=matches_id).count() > 1:
                row.delete()

        #auto update the live score
        livematches.objects.filter(matches_id=matches_id).update(livescore_opone=livescore_opone,livescore_optwo=livescore_optwo)

        #update request form oddbet to db (needtemplate)

    
def sched_livematches():
    schedule.every(10).seconds.do(createlivematches)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    getupcomingmatches()
