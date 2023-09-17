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

# List of disease column names
disease_columns = ['Meningitis', "Alzheimer's Disease and Other Dementias", "Parkinson's Disease",
                   'Nutritional Deficiencies', 'Malaria', 'Drowning', 'Interpersonal Violence',
                   'Maternal Disorders', 'HIV/AIDS', 'Drug Use Disorders', 'Tuberculosis',
                   'Cardiovascular Diseases', 'Lower Respiratory Infections', 'Neonatal Disorders',
                   'Alcohol Use Disorders', 'Self-harm', 'Exposure to Forces of Nature',
                   'Diarrheal Diseases', 'Environmental Heat and Cold Exposure', 'Neoplasms',
                   'Conflict and Terrorism', 'Diabetes Mellitus', 'Chronic Kidney Disease', 'Poisonings',
                   'Protein-Energy Malnutrition', 'Road Injuries', 'Chronic Respiratory Diseases',
                   'Cirrhosis and Other Chronic Liver Diseases', 'Digestive Diseases',
                   'Fire, Heat, and Hot Substances', 'Acute Hepatitis']

# Sum 'Total Deaths' for each disease across all years
disease_total_deaths = df[disease_columns].sum()

# Creating a new DataFrame with disease names and their total deaths
disease_data = pd.DataFrame({'Disease': disease_total_deaths.index, 'Total Deaths': disease_total_deaths.values})

# Selecting the top 10 diseases by total deaths
top_10_diseases = disease_data.nlargest(10, 'Total Deaths')

# Create a Streamlit app
st.title('Global Health Data Overview')

# Create tabs for each visualization
st.sidebar.title("Select Visualization")
selected_viz = st.sidebar.radio("", ["Overview", "Total Deaths by Country", "Top 5 Diseases in Lebanon", "Total Deaths in Lebanon Over the Years", "Cardiovascular Disease Deaths Map", "Top 10 Diseases by Total Deaths"])

# Overview Tab
if selected_viz == "Overview":
    st.write("This app shows different visuals related to the Causes of Deaths dataset from Kaggle, ranging from 1990 to 2019, worldwide.")
    # Add an overview or description here.

# Total Deaths by Country Tab
elif selected_viz == "Total Deaths by Country":
    st.header('Total Deaths by Country from 1990 to 2019')
    
    # Filter by country
    country_filter = st.selectbox("Select a Country", df['Country/Territory'].unique())
    
    filtered_df = df[df['Country/Territory'] == country_filter]
    
    fig = px.scatter(
        filtered_df,
        x='Year',
        y='Total Deaths',
        title=f'Total Deaths by Country for {country_filter} from 1990 to 2019',
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

    st.header('Top 5
