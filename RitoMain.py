from Ritoapi import Ritoapi
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def main():
    api = Ritoapi('RGAPI-18fb1348-b7de-4d46-bd9f-cd30d4fa6786')
    #r = api.get_summoner_by_name('Captain DaGOn')
    #a = api.get_rank_by_summonerid(r['id'])
    #b = api.get_past_20_ranked_solo(r['accountId'])
    #c = api.get_maps()
    #print(c)
    #print (r['name'])
    #print (a[0]['tier'] + ' ' + a[0]['rank'])
    #print (b)
    img=plt.imread('map11.png')
    imgplot = plt.imshow(img)
    plt.scatter([511],[511])
    plt.show()
    

if __name__ == "__main__":
	main()