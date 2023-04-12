import streamlit as st
import pandas as pd
import json 
from sqlalchemy import create_engine
from pandas.io import sql
import pymysql

with open(r'C:\Users\Hardware\Downloads\pulse-master\data\map\transaction\hover\country\india\2022\1.json','r') as f:
    datas = json.loads(f.read()),
json_df1 = pd.json_normalize(datas,record_path =['data','hoverDataList','metric'],meta=['success','code',['data','hoverDataList','name']]) 

with open(r'C:\Users\Hardware\Downloads\pulse-master\data\map\transaction\hover\country\india\2022\2.json','r') as f:
    datas = json.loads(f.read()),
json_df2 = pd.json_normalize(datas,record_path =['data','hoverDataList','metric'],meta=['success','code',['data','hoverDataList','name']]) 

with open(r'C:\Users\Hardware\Downloads\pulse-master\data\map\transaction\hover\country\india\2022\3.json','r') as f:
    datas = json.loads(f.read()),
json_df3 = pd.json_normalize(datas,record_path =['data','hoverDataList','metric'],meta=['success','code',['data','hoverDataList','name']]) 

with open(r'C:\Users\Hardware\Downloads\pulse-master\data\map\transaction\hover\country\india\2022\4.json','r') as f:
    datas = json.loads(f.read()),
json_df4 = pd.json_normalize(datas,record_path =['data','hoverDataList','metric'],meta=['success','code',['data','hoverDataList','name']]) 

def cap_sentence(s):
  return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))

state_caps1 = json_df1["data.hoverDataList.name"].str.replace(r'(\w+)', lambda x: x.group().capitalize(),n=2, regex=True)
json_df1['states']=state_caps1
json_df1['Qtr']=1
json_df1.drop(['data.hoverDataList.name'], axis=1,inplace=True)

state_caps2 = json_df2["data.hoverDataList.name"].str.replace(r'(\w+)', lambda x: x.group().capitalize(),n=2, regex=True)
json_df2['states']=state_caps2
json_df2['Qtr']=2
json_df2.drop(['data.hoverDataList.name'], axis=1,inplace=True)

state_caps3 = json_df3["data.hoverDataList.name"].str.replace(r'(\w+)', lambda x: x.group().capitalize(),n=2, regex=True)
json_df3['states']=state_caps3
json_df3['Qtr']=3
json_df3.drop(['data.hoverDataList.name'], axis=1,inplace=True)

state_caps4 = json_df4["data.hoverDataList.name"].str.replace(r'(\w+)', lambda x: x.group().capitalize(),n=2, regex=True)
json_df4['states']=state_caps4
json_df4['Qtr']=4
json_df4.drop(['data.hoverDataList.name'], axis=1,inplace=True)

all_df=[json_df1,json_df2,json_df3,json_df4]

final_df=pd.concat(all_df)

final_df

conEng = create_engine("mysql+pymysql://root:Mayava321@localhost:3306/phonepe",pool_size=1000, max_overflow=2000)

final_df.to_sql('2022', conEng, if_exists='append', index=False, chunksize=None, dtype=None, method=None)

# Data insert successfully


