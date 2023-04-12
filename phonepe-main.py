import streamlit as st
import pandas as pd
import json 
from sqlalchemy import create_engine
from pandas.io import sql
import pymysql
import plotly.express as px
import plotly.io as pio


st.title(':blue[Phone Pe Pulse]')

plots=st.sidebar.radio('Select Plot', ['Map', 'Scatter Plot','Line Graph'],horizontal=True)

filter_year=st.sidebar.selectbox('Select Year',[2018,2019,2020,2021,2022])
filter_Qtr=st.sidebar.selectbox('Select Quarter',[1,2,3,4])
fitter_val=st.sidebar.selectbox('Select '+plots+' Values',['Transaction','Count'])
 
if fitter_val=="Transaction":
    fin_filter_val='amount'
if fitter_val=="Count":
    fin_filter_val='count'
# sumint_val=
sub_botton=st.sidebar.button('Get '+plots)



conEng = create_engine("mysql+pymysql://root:Mayava321@localhost:3306/phonepe",pool_size=1000, max_overflow=2000)
sql=f'select * from `{filter_year}` where Qtr={filter_Qtr}'
mysql_df=pd.read_sql(sql, conEng, index_col=None,chunksize=None)

st.subheader(f":green[Year {str(filter_year)} Quarter {str(filter_Qtr)}]")
mysql_df





if sub_botton:
    if plots=='Scatter Plot':
        data = [dict(
            type = 'scatter',
            x = mysql_df['states'],
            y = mysql_df[fin_filter_val],
            mode = 'markers',
            transforms = [dict(
                type = 'groupby',
                groups = mysql_df['states'],
               )]
        )]

        fig_dict = dict(data=data)
        pio.show(fig_dict, validate=False)


if sub_botton:
    if plots=='Map':
        fig = px.choropleth(
        mysql_df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='states',
            color=fin_filter_val,
            color_continuous_scale='oranges'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()



if sub_botton:
    if plots=='Line Graph':
        fig = px.line(mysql_df, x='states', y=fin_filter_val)
        fig.show()

