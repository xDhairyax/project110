import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics as st 
import random 
import pandas as pd 

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
        mean=st.mean(dataset)
        return mean

def showfig(meanlist):
    df=meanlist
    mean=st.mean(df)
    fig=ff.create_distplot([df],["ReadingTime"],show_hist=False)
    #fig.show()


meanlist=[]
for i in range(0,100):
    setofmean=randomsetofmean(30)
    meanlist.append(setofmean)
showfig(meanlist)



mean1=st.mean(data)
print(mean1)

mean2=st.mean(meanlist)
print(mean2)
