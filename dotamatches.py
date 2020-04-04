import requests
import json
import schedule
import time
from myproject.wsgi import *
from esport_db.models import upcomingmatches,listmatches,livematches

#dota api upcoming macthes   
def getupcomingmatches():
    dotaupcomingmatch = requests.get('https://api.pandascore.co/dota2/matches/upcoming?token=M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI')
    data = json.loads(dotaupcomingmatch.text)

    for d in data:
        print('Upcoming Matches')
        if len(d['opponents']) != 1 and len(d['opponents']) != 0:
            print(d['league']['name'])
            print(d['begin_at'])
            print(d['opponents'][0]['opponent']['name'] +' VS '+ d['opponents'][1]['opponent']['name'])

#dota api live macthes       
def getlivematches():           
    dotalivematch =  requests.get('https://api.pandascore.co/dota2/matches/running?token=M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI')       
    data = json.loads(dotalivematch.text)    

    for d in data:
        print('Live Matches')
        print(d['league']['name'])
        print(d['begin_at'])
        print(d['opponents'][0]['opponent']['name'] +' VS '+ d['opponents'][1]['opponent']['name'])
        print(d['results'][0]['score'],':',d['results'][1]['score'])

def inserttestdb():
    inserttestupcoming = {'leaguename':['EG','OG'],'opponent_one':['EG','LIQUID'],'opponent_two':['VG','IG'],'datetime':['2019-06-24','2019-07-10'],'odds_one':[2.9,1.2],'odds_two':[1.5,3.0]}
    inserttest = upcomingmatches(leaguename='EG')
    inserttest.save()
    
def sched_livematches():
    schedule.every(10).seconds.do(getlivematches)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    inserttestdb()