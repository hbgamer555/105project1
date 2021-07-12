import statistics

import pandas as pd



df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\project.csv")
project=df["Height"]
snd=statistics.stdev(project)
print(snd)


#data=[600,470,170,430,300]
#step no1
#findmean=statistics.mean(data)
#print(findmean)

#submean=[206,76,-224,36,-94]
#dog1m=206*206
#print(dog1m)

