from Ritoapi import Ritoapi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    api = Ritoapi('') #api key goes here
    r = api.get_summoner_by_name('Captain DaGOn')
    z = True

    data = [['' for x in range (0,3)] for y in range (0,20)]

    try:
        a = api.get_current_game(r['id'])
    except KeyError:
        data[0][1] = ('No Game Available')
        z = False
    if z:
        b = a['participants']
        i = 0
        j = 5
        data[0][1] = 'Game Mode'
        data[1][1] = (a['gameMode'])
        if a['gameQueueConfigId'] == 420:
            data[2][1] = ('Ranked')
        for val in b:
            if i == 0:
                data[3][0] = ('Blue team')
                k = 0
            if i == 5:
                data[3][2] = ('Red team')
                j = 5
                k = 2
            data[j][k] = (b[i]['summonerName'])
            rankdata = api.get_rank_by_summonerid(b[i]['summonerId'])
            try:
                rank = rankdata[0]['queueType'] + ' ' + rankdata[0]['tier'] + ' ' + rankdata[0]['rank']
            except IndexError:
                rank = 'Unranked'
            j += 1
            data[j][k] = (rank)
            i += 1
            j += 2
    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print ("".join(word.ljust(col_width) for word in row))

if __name__ == "__main__":
	main()