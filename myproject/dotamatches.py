import requests
import json
from parsel import Selector

#dota api upcoming macthes   
def getupcomingmatches():
    dotaupcomingmatch = requests.get('https://api.pandascore.co/dota2/matches/upcoming?token=M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI')
    data = json.loads(dotaupcomingmatch.text)

    for d in data:
        if len(d['opponents']) != 1 and len(d['opponents']) != 0:
            print(d['league']['name'])
            print(d['begin_at'])
            print(d['opponents'][0]['opponent']['name'] +' VS '+ d['opponents'][1]['opponent']['name'])

#dota api live macthes       
def getlivematches():           
    dotalivematch =  requests.get('https://api.pandascore.co/dota2/matches/running?token=M-gxTfZLAuoLWGjTCK214C9k8lthOMrkYeBs-FvY87ucxjJenCI')       
    data = json.loads(dotalivematch.text)    

    for d in data:
        print(d['league']['name'])
        print(d['begin_at'])
        print(d['opponents'][0]['opponent']['name'] +' VS '+ d['opponents'][1]['opponent']['name'])
        print(d['results'][0]['score'],':',d['results'][1]['score'])

if __name__ == "__main__":
    getupcomingmatches()
    getlivematches()