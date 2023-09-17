import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.components.v1 import components

# Read the data
df = pd.read_csv("cause_of_deaths.csv")

# Define the list of causes of death
Cause_of_death = ['Meningitis', "Alzheimer's Disease and Other Dementias", 'Parkinson\'s Disease',
                  'Nutritional Deficiencies', 'Malaria', 'Drowning',
                  'Interpersonal Violence', 'Maternal Disorders', 'HIV/AIDS',
                  'Drug Use Disorders', 'Tuberculosis', 'Cardiovascular Diseases',
                  'Lower Respiratory Infections', 'Neonatal Disorders',
                  'Alcohol Use Disorders', 'Self-harm', 'Exposure to Forces of Nature',
                  'Diarrheal Diseases', 'Environmental Heat and Cold Exposure',
                  'Neoplasms', 'Conflict and Terrorism', 'Diabetes Mellitus',
                  'Chronic Kidney Disease', 'Poisonings', 'Protein-Energy Malnutrition',
                  'Road Injuries', 'Chronic Respiratory Diseases',
                  'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases',
                  'Fire, Heat, and Hot Substances', 'Acute Hepatitis']

# Calculate the total deaths for each year
df['Total Deaths'] = df[Cause_of_death].sum(axis=1)

# Create a Streamlit app
st.title('Global Health Data Overview')

# Create a sidebar with tabs
selected_tab = st.sidebar.radio("Select Tab:", ["Overview", "Choropleth Map"])

# Overview Tab
if selected_tab == "Overview":
    # Description
    st.write("This app shows different visuals related to the Causes of Deaths dataset from Kaggle, ranging from 1990 to 2019, worldwide.")
    
    # Scatterplot by Country
    st.header('Total Deaths by Country from 1990 to 2019')
    fig = px.scatter(
        df,
        x='Year',
        y='Total Deaths',
        color='Country/Territory',
        title='Total Deaths by Country from 1990 to 2019',
        labels={'Country/Territory': 'Country', 'Total Deaths': 'Total Deaths', 'Year': 'Year'},
    )
    st.plotly_chart(fig)

    # Filtering data for Lebanon
    lebanon_data = df[df['Country/Territory'] == 'Lebanon']

    # Calculating the sum of deaths for each disease in Lebanon
    lebanon_disease_deaths = lebanon_data.drop(['Country/Territory', 'Code', 'Year', 'Total Deaths'], axis=1).sum()

    # Sorting the diseases by total deaths in descending order and select the top 5
    top_5_diseases = lebanon_disease_deaths.sort_values(ascending=False).head(5)

    # Pie chart for Top 5 Diseases in Lebanon
    st.subheader('Top 5 Diseases in Lebanon by Total Deaths')
    fig_pie = px.pie(names=top_5_diseases.index, values=top_5_diseases)

    # Customizing the layout
    fig_pie.update_traces(textinfo='percent+label')

    st.plotly_chart(fig_pie)

    # Scatterplot for Total Deaths in Lebanon Over the Years
    st.subheader('Total Deaths in Lebanon Over the Years')
    fig_lebanon = px.scatter(lebanon_data, x='Year', y='Total Deaths', title='Total Deaths in Lebanon Over the Years')

    st.plotly_chart(fig_lebanon)

# Choropleth Map Tab
elif selected_tab == "Choropleth Map":
    st.header('Cardiovascular Disease Deaths (1990-2019) Choropleth Map')
    fig_choropleth = px.choropleth(
        df,
        locations="Country/Territory",
        locationmode="country names",
        color="Cardiovascular Diseases",
        animation_frame="Year",
        color_continuous_scale="Viridis",
        title="Cardiovascular Disease Deaths (1990-2019)",
        hover_name="Country/Territory",
        projection="natural earth"
    )

    st.plotly_chart(fig_choropleth)
