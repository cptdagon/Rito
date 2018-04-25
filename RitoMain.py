from Ritoapi import Ritoapi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    api = Ritoapi('RGAPI-57149e71-f363-4517-aa91-8190dfd3d8e6') #api key goes here
    r = api.get_summoner_by_name('Infernacus')
    z = True
    try:
        a = api.get_current_game(r['id'])
    except KeyError:
        print ('No Game Available')
        z = False
    if z:
        b = a['participants']
        i = 0
        print(a['gameMode'])
        if a['gameQueueConfigId'] == 420:
            print('Ranked' + '\n')
        for val in b:
            if i == 0:
                print ('Blue team\n')
            if i == 5:
                print ('Red team\n')
            print (b[i]['summonerName'])
            rankdata = api.get_rank_by_summonerid(b[i]['summonerId'])
            try:
                rank = rankdata[0]['queueType'] + ' ' + rankdata[0]['tier'] + ' ' + rankdata[0]['rank'] + '\n'
            except IndexError:
                rank = 'Unranked \n'
            print (rank)
            i += 1

if __name__ == "__main__":
	main()