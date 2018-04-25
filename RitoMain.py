from Ritoapi import Ritoapi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    api = Ritoapi('') #api key goes here
    r = api.get_summoner_by_name('Captain DaGOn')
    a = api.get_current_game(r['id'])
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
        print (rankdata[0]['tier'] + ' ' + rankdata[0]['rank'] + '\n')
        i += 1

if __name__ == "__main__":
	main()