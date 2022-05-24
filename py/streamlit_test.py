import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title='Dashboard',
                    page_icon=':bar_chart:',
                    layout='wide')

df = pd.read_csv("C:\\Users\\shahs\\Desktop\\Player_piece_sac_data.csv")

# st.dataframe(df)

st.sidebar.header('Filter:')
color = st.sidebar.multiselect(
    'Select Color:',
    options = df['color'].unique(),
    default = df['color'].unique()
)

player = st.sidebar.multiselect(
    'Select Player:',
    options = df['player'].unique(),
    default = df['player'].unique()
)

df_selection = df.query(
    'color == @color & player == @player'
)
st.dataframe(df_selection)


st.title(':bar_chart: Dashboard')
st.markdown('##')

total_game = len(df_selection)
try: total_white_game = df_selection['color'].value_counts().White
except: total_white_game = 0
try: total_black_game = df_selection['color'].value_counts().Black
except: total_black_game = 0
average_moves = round(df_selection['moves'].mean(), 1)
star_moves = ':star:' * (int(round(average_moves,  0))//10)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Games Played:')
    st.subheader(f'{total_game:,}')

with middle_column:
    st.subheader('Average Moves:')
    st.subheader(f'{average_moves} {star_moves}')

with right_column:
    st.subheader('Total white and black game:')
    st.subheader(f'White: {total_white_game}')
    st.subheader(f'Black: {total_black_game}')

st.markdown('---')

moves_by_color_line = (
    df_selection.groupby(by=['color']).sum()[['moves']].sort_values(by=['moves'], ascending=1)
)

fig_moves_color = px.bar(
    moves_by_color_line,
    x = 'moves',
    y = moves_by_color_line.index,
    orientation = 'h',
    title = '<b>Moves by Color Line</b>',
    color_discrete_sequence = ['#0083B8'] * len(moves_by_color_line),
    template = 'plotly_white',
)

st.plotly_chart(fig_moves_color)



hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)