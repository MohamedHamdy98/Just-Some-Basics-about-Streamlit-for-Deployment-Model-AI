import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from dataset import class_data

st.set_page_config(
    page_title="US Accidents Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

class webApp(class_data):
    st.title('Just Simple Practice about Basics of Streamlit 😀')
    # object from data class 
    cd = class_data()
    # setup the layout of visualization
    row1 = st.columns(2)
    row2 = st.columns(1)

    # preprocessing data
    df = cd.add_count()
    df = cd.convert_to_date()
    df = cd.split_date()

    #all functions
    def show_data_Frame(data):
        st.dataframe(data.head(2))

    # to filter you data by the year and the city
    def create_sidebar(self, df):   
        st.sidebar.title('US Accidents')
        years = list(df['years'].unique())[::-1]
        city = list(df['City'].unique())[::-1]
        city.insert(0, 'All City')
        selected_year = st.sidebar.selectbox('Select a year', years, index=len(years)-1)
        selected_city = st.sidebar.selectbox('Select the city', city, index=0)
        if selected_city == 'All City':
            df_selected_year  = df[df['years'] == selected_year]
            df_selected_year_sorted = df_selected_year.sort_values(by='months', ascending=False)
            return df_selected_year_sorted
        else:
            df_selected_year_city  = df[(df['years'] == selected_year) & (df['City'] == selected_city)]
            df_selected_year_city_sorted = df_selected_year_city.sort_values(by='months', ascending=False)
            return df_selected_year_city_sorted
        
    # Count of Accidents by date and the place

    def plot_scatter(self, df):
        cnt = st.container(border=True)
        scatter_plot_data = df.groupby(['months','days','hours', 'Country', 'City'])['count'].sum().reset_index().sort_values(by='count', ascending=False).nlargest(400,'count')
        cnt.markdown('Count of Accidents by date and the place')
        fig = px.scatter(scatter_plot_data, x="months", y="days",size="count",color="City",hover_name="City",size_max=60)
        cnt.plotly_chart(fig, use_container_width=True)

    # Imapct of Traffic on Accidents

    def plot_bar(self, df):
        cnt = st.container(border=True)
        data_traffic_calming = df[['City','Traffic_Calming']].value_counts().reset_index().nlargest(10,'count')
        cnt.markdown('Imapct of Traffic on Accidents')
        # barmode='group'
        fig = px.bar(data_traffic_calming, x='City', y='count', hover_name='Traffic_Calming', color='City')
        cnt.plotly_chart(fig, use_container_width=True)
    
    # def plot_map(df):
    #     cnt = st.container(border=True)
    #     geography = df.groupby(['City','Start_Lat', 'Start_Lng'])['count'].sum().reset_index().nlargest(20,'count')
    #     fig = px.scatter_geo(geography, lat='Start_Lat', lon='Start_Lng', color="City", hover_name="City", size="count", projection="natural earth")
    #     cnt.plotly_chart(fig, use_container_width=True)

    # Count of Accidents on street by date

    def plot_street_map(self, df):
        cnt = st.container(border=True, height=600)
        cnt.markdown('Count of Accidents on street by date')
        geography = df.groupby(['City','Start_Lat', 'Start_Lng', 'months', 'Street'])['count'].sum().reset_index().nlargest(20,'count')
        fig = px.scatter_mapbox(geography, lat='Start_Lat', lon='Start_Lng',color='Street', size="count",hover_data=['months'],
                                size_max=40, zoom=3, height=550,color_continuous_scale=px.colors.cyclical.IceFire)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        cnt.plotly_chart(fig, use_container_width=True)

    # def plot_correlation(df, obj):
    #     cnt = st.container(border=True)
    #     data_corr = obj.get_correlation()
    #     data_correlation = data_corr.corr()
    #     fig = plt.figure()
    #     sns.heatmap(data_correlation, annot=True, annot_kws={'size': 6})
    #     cnt.pyplot(fig)


    def show_visualization(self, df):
        self.plot_scatter(df)
        self.plot_bar(df)
        self.plot_street_map(df)






