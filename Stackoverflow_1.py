import pandas as pd
import numpy as np
import datetime as dt
import json

import pandas as pd

import pytz

# Testing by adding a comment

data = ['2017-01-01 00:00:00']
df = pd.DataFrame()
datatf= pd.to_datetime(data)
#df['Gmt time'] = data
#df1 = pd.DataFrame()
#df1['time'] = pd.to_datetime(df['Gmt time'])
my_timestamp = dt.datetime.now()
new_timezone = pytz.timezone("US/Pacific")
old_timezone = pytz.timezone("US/Eastern")
my_timestamp_in_new_timezone = old_timezone.localize(datatf[0]).astimezone(new_timezone)
print(my_timestamp_in_new_timezone )
df['Gmt time'] = [my_timestamp_in_new_timezone]
df['Gmt time'] = pd.DatetimeIndex(df['Gmt time'])
#df['Gmt time'] = df['Gmt time'].dt.tz_localize('GMT').dt.tz_convert('America/New_York')
print(df)




####


df = pd.read_json('{"Technology Group":{"0":"Cloud","1":"Cloud","2":"Cloud","3":"Collaboration","4":"Collaboration","5":"Collaboration","6":"Collaboration","7":"Collaboration","8":"Collaboration","9":"Core", "10": "Software"},"Technology":{"0":"AMP","1":"EWS","2":"Webex","3":"Telepresence","4":"Call Manager","5":"Contact Center","6":"MS Voice","7":"Apps","8":"PRIME  ","9":"Wirelees", "10": "Prime Infrastructure"}}')
print(df)

tech_input2 = ['AMP', 'Call Manager', 'PRIME']
df = df[df['Technology'].isin(tech_input2)]

d = pd.DataFrame()
key = ['govern', 'data']
for k in key:
    for w in range(0, len(train_vs)):
        wordcount = Counter(train_vs['doc_text'].iloc[w])
        a_vs = (wordcount[k]/len(train_v.iloc[w])*1)
        temp = pd.DataFrame([{k: a_vs}] )
        d = pd.concat([d, temp])









months = ['0:00','9:00']#,'1996-01-04'] #,5,6,7,8,9,10,11,12]
months2 = ['4:00','14:30']#,'1996-01-03','1996-01-04'] #,5,6,7,8,9,10,11,12]
data1 = [100,200]#,300,400]# ,500,600,700,800,900,1000,1100,1200]
df = pd.DataFrame({
                    'month' : months,'month2' : months2,
                    'd1' : data1,
                    'd2' : 0,
                });


t1 = pd.to_datetime(df['month'])
t2 = pd.to_datetime(df['month2'])
t3 = t1 - t2

print (t3)
#df = {'name': [a,c,e],'author': [b,d,f], 'count'= [10,5,2] }




l = []
xyz_dictionary = {'x': 1, 'y': 2, 'z':3}
l.append(xyz_dictionary)
l.append(xyz_dictionary)
#.... #append all xyz values
data = {'xyz' : l}
json_data = json.dumps(data)
print json_data
df = pd.DataFrame({ 'A' : 1.,
'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1,index=list(range(4))),
'D' : [1, 2, 1, 3],
'E' : pd.Categorical(["test","train","test","train"]),
'F' : 'foo' })

for index, row in df.iterrows():
    if row['D'] == 1:
        row['E'] = row['F']

    print(row, index)


print('Done')