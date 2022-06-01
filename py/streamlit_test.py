import pandas as pd
import plotly.express as px
import streamlit as st
import os


data_location = os.path.realpath(
    os.path.join(os.getcwd(), 'data\\azerbaijan_suicide_data.xlsx'))

st.set_page_config(page_title='Dashboard',
                    page_icon=':bar_chart:',
                    layout='wide')

data_year = pd.read_excel(data_location, sheet_name='year').loc[::-1].reset_index(drop=True)

both_sexes = [float(d[:d.find(' ')]) for d in data_year.Both_sexes]
both_sexes_len = len(both_sexes)
average_both_sexes_year = sum(both_sexes) / (both_sexes_len if both_sexes_len else 1)
male = [float(d[:d.find(' ')]) for d in data_year.Male]
male_len = len(male)
average_male_year = sum(male) / (male_len if male_len else 1)
female = [float(d[:d.find(' ')]) for d in data_year.Female]
female_len = len(female)
average_female_year = sum(female) / (female_len if female_len else 1)

data_year_graph = pd.DataFrame(
    {'Year': data_year.Year, 'Both Sexes': both_sexes, 'Male': male, 'Female': female})

graph1 = px.scatter(data_year_graph, x='Male', y='Female', animation_frame="Year")

df = px.data.gapminder()
graph2 = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                    size="pop", color="continent", hover_name="country",)

st.plotly_chart(graph2)
st.plotly_chart(graph1)