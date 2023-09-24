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
disease_columns = Cause_of_death

# Sum 'Total Deaths' for each disease across all years
disease_total_deaths = df[disease_columns].sum()

# Creating a new DataFrame with disease names and their total deaths
disease_data = pd.DataFrame({'Disease': disease_columns, 'Total Deaths': disease_total_deaths})

# Selecting the top 10 diseases by total deaths
top_10_diseases = disease_data.nlargest(10, 'Total Deaths')

# Create a Streamlit app
st.title('Global Health Data Overview')

# Create tabs for each visualization
st.sidebar.title("Select Visualization")
selected_viz = st.sidebar.radio("", ["Total Deaths by Country", "Top 10 Diseases by Total Deaths", "Cardiovascular Disease Deaths Map", "Top 5 Diseases in Lebanon", "Total Deaths in Lebanon Over the Years"])

# Total Deaths by Country Tab
if selected_viz == "Total Deaths by Country":
    st.header('Total Deaths by Country from 1990 to 2019')
    
    # Define the list of countries
    countries = df['Country/Territory'].unique()
    
    # Create a multi-select box to choose countries
    selected_countries = st.sidebar.multiselect("Select Countries", countries, countries[:5])
    
    # Filter the DataFrame based on selected countries
    filtered_df = df[df['Country/Territory'].isin(selected_countries)]
    
    # Create a line chart showing total deaths by country over the years
    fig = px.line(
        filtered_df,
        x='Year',
        y='Total Deaths',
        color='Country/Territory',
        title='Total Deaths by Country from 1990 to 2019',
        labels={'Country/Territory': 'Country', 'Total Deaths': 'Total Deaths', 'Year': 'Year'},
    )
    
    st.plotly_chart(fig)

        
    

# Top 10 Diseases by Total Deaths Tab
elif selected_viz == "Top 10 Diseases by Total Deaths":
    st.header('Top 10 Diseases by Total Deaths')
    fig = px.scatter(
        top_10_diseases,
        x='Disease',
        y='Total Deaths',
        color='Disease',  # Color by disease
        color_discrete_sequence=px.colors.qualitative.Set1,
        title='Top 10 Diseases by Total Deaths',
        labels={'Disease': 'Disease', 'Total Deaths': 'Total Deaths'},
    )
    st.plotly_chart(fig)

# Cardiovascular Disease Deaths Map Tab
elif selected_viz == "Cardiovascular Disease Deaths Map":
    st.header('Cardiovascular Disease Deaths (1990-2019) Map')
    fig = px.choropleth(
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
    
    # Create a year slider
    year_range = st.slider("Select Year Range", min_value=1990, max_value=2019, value=(1990, 2019))
    
    # Filter data based on the selected year range
    filtered_lebanon_data = lebanon_data[(lebanon_data['Year'] >= year_range[0]) & (lebanon_data['Year'] <= year_range[1])]
    
    fig_lebanon = px.scatter(
        filtered_lebanon_data, x='Year', y='Total Deaths', title='Total Deaths in Lebanon Over the Years'
    )

    st.plotly_chart(fig_lebanon)
