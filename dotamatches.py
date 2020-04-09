import json
import time
import schedule
import requests
from django.utils import timezone
from myproject.wsgi import *
from esport_db.models import nextmatches, listmatches, livematches
from datetime import datetime
import urllib3
urllib3.disable_warnings()

#dota api upcoming macthes   
def getnextmatches():
    token = 'M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI'
    dotaupcomingmatch = requests.get('https://api.pandascore.co/dota2/matches/upcoming?token={0}'.format(token),verify=False)
    createdata = json.loads(dotaupcomingmatch.text)


    for d in createdata:
        if len(d['opponents']) != 1 and len(d['opponents']) != 0:
            if len(d['opponents']) == 0:
                pass
            else:
                datetime_beginat = d['begin_at']
                convertstrptime = datetime.strptime(datetime_beginat,"%Y-%m-%dT%H:%M:%SZ")
                stringdatetime = convertstrptime.strftime("%Y-%m-%d %H:%M:%S")
                
                #create the upcoming matches data
                insertnextmatch = nextmatches(leaguename=d['league']['name'],games_id=d['id'],opponent_one=d['opponents'][0]['opponent']['name']
                                    ,opponent_two=d['opponents'][1]['opponent']['name'],datetime=stringdatetime,odds_one=0.0000,odds_two=0.0000)      
                insertnextmatch.save()

        #remove duplicate after update from api
        # for row in nextmatches.objects.all().reverse():
        #     if nextmatches.objects.filter(games_id=row.games_id).count() > 1 :
        #         row.delete()

        lastSeenId = float('-Inf')
        rows =  nextmatches.objects.all().order_by('games_id')

        for row in rows:
            if row.games_id == lastSeenId:
                print('delete')
                row.delete()
            if row.odds_one != 0:
                pass
            else:
                lastSeenId = row.games_id

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
                                    ,livescore_opone=livescore_opone,livescore_optwo=livescore_optwo,matches_status=matches_status,odds_one=0.0000,odds_two=0.0000)
        insertlivematch.save()

        lastSeenId = float('-Inf')
        rows =  livematches.objects.all().order_by('matches_id')

        for row in rows:
            if row.matches_id == lastSeenId :
                print('delete')
                row.delete()
            else:
                lastSeenId = row.matches_id


        #auto update the live score
        livematches.objects.filter(matches_id=matches_id).update(livescore_opone=livescore_opone,livescore_optwo=livescore_optwo)
    
def sched_livematches():
    schedule.every(10).seconds.do(createlivematches)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    getnextmatches()