import pandas as pd
import plotly.express as px
import streamlit as st

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

# Create tabs for each visualization
st.sidebar.title("Select Visualization")
selected_viz = st.sidebar.radio("", ["Overview", "Total Deaths by Country", "Top 5 Diseases in Lebanon", "Total Deaths in Lebanon Over the Years"])

# Overview Tab
if selected_viz == "Overview":
    st.write("This app shows different visuals related to the Causes of Deaths dataset from Kaggle, ranging from 1990 to 2019, worldwide.")
    # Add an overview or description here.

# Total Deaths by Country Tab
elif selected_viz == "Total Deaths by Country":
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

# Top 5 Diseases in Lebanon Tab
elif selected_viz == "Top 5 Diseases in Lebanon":
    # Filtering data for Lebanon
    lebanon_data = df[df['Country/Territory'] == 'Lebanon']

    # Calculating the sum of deaths for each disease in Lebanon
    lebanon_disease_deaths = lebanon_data.drop(['Country/Territory', 'Code', 'Year', 'Total Deaths'], axis=1).sum()

    # Sorting the diseases by total deaths in descending order and select the top 5
    top_5_diseases = lebanon_disease_deaths.sort_values(ascending=False).head(5)

    st.header('Top 5 Diseases in Lebanon by Total Deaths')
    fig_pie = px.pie(names=top_5_diseases.index, values=top_5_diseases)

    # Customizing the layout
    fig_pie.update_traces(textinfo='percent+label')

    st.plotly_chart(fig_pie)

# Total Deaths in Lebanon Over the Years Tab
elif selected_viz == "Total Deaths in Lebanon Over the Years":
    # Filtering data for Lebanon
    lebanon_data = df[df['Country/Territory'] == 'Lebanon']

    st.header('Total Deaths in Lebanon Over the Years')
    fig_lebanon = px.scatter(lebanon_data, x='Year', y='Total Deaths', title='Total Deaths in Lebanon Over the Years')

    st.plotly_chart(fig_lebanon)
