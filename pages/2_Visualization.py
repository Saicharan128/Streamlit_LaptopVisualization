import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
laptop_df = pd.read_csv('resources/data/Laptop.csv')
laptop_df.drop("Unnamed: 0",axis=1,inplace=True)


# Title of the web app
st.title('Laptop Dataset :red[Visualizations]')

# Select visualization type
visualization_type = st.selectbox('Select a Visualization', 
                                  ['Laptop Count by Website', 
                                   'RAM vs. Price', 
                                   'Laptop Models by Brand', 
                                   'Laptop Price Distribution',
                                   'RAM vs. ROM sizes by Brand'])

# Create visualization based on selection
if visualization_type == 'Laptop Count by Website':
    st.write('## Laptop Count by Website :red[Bar Chart]\n')
    website_counts = laptop_df['Website'].value_counts().reset_index()
    website_counts.columns = ['Website', 'Count']
    fig = px.bar(website_counts, x='Website', y='Count',
                 title='Laptop Count by Website')
    fig.update_xaxes(title_text='Website')
    fig.update_yaxes(title_text='Count')
    st.plotly_chart(fig)

elif visualization_type == 'RAM vs. Price':
    st.write('## RAM vs. Price :red[Scatter Plot]\n')
    fig = px.scatter(laptop_df, x='Ram', y='Price  (₹)',title='Laptop Ram by Price', color='Brand', hover_name='Model')
    fig.update_traces(marker=dict(size=8, opacity=0.7))
    fig.update_layout(showlegend=True, legend=dict(title='Brand'))
    fig.update_xaxes(title_text='RAM (GB)')
    fig.update_yaxes(title_text='Price (Rs)', tickprefix='₹', tickformat=".2s")
    st.plotly_chart(fig)

elif visualization_type == 'Laptop Models by Brand':
    st.write('## Laptop Models by Brand :red[Donut Chart]\n')
    df = laptop_df.groupby(['Brand', 'Model']).size().reset_index(name='Count')
    fig = px.pie(df, names='Brand', values='Count', hole=0.6, color='Brand', 
                 title='Laptop Models by Brand', hover_data=['Brand', 'Model'])
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig)

elif visualization_type == 'Laptop Price Distribution':
    st.write('## Laptop Price Distribution :red[Histogram]\n')
    fig = px.histogram(laptop_df, x='Price  (₹)', nbins=20,
                       title='Distribution of Laptop Prices')
    fig.update_xaxes(title_text='Price (₹)', tickprefix='₹')
    fig.update_yaxes(title_text='Count')
    st.plotly_chart(fig)

elif visualization_type == 'RAM vs. ROM sizes by Brand':
    st.write('## RAM vs ROM sizes by Brand :red[Scatter Plot]\n')
    fig = px.scatter(laptop_df, x='Ram', y='Rom', color='Brand', 
                     title='RAM vs ROM sizes by Brand')
    fig.update_xaxes(title_text='RAM (GB)', tickformat=".0f")
    fig.update_yaxes(title_text='ROM (GB)', tickformat=".0f")
    st.plotly_chart(fig)









