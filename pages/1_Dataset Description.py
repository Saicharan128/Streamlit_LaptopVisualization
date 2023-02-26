import streamlit as st
import pandas as pd

# Load the dataset
laptop_df = pd.read_csv('resources/data/Laptop.csv')
laptop_df.drop("Unnamed: 0",axis=1,inplace=True)


# Set the page title
st.set_page_config(page_title='Laptop Dataset Description')

# Display the column descriptions
st.write('## Laptop Dataset Description\n')

st.caption("### This is the :red[Dataset] that has been made by scrapping from :red[3 different websites] :  :blue['Flipkart'] , :blue['Reliance Digital'] and :blue['Dell'] as a part of my :red[Webscraping project] at :red[Innomatics Research Labs]")

st.write("### :red[Columns] and :red[Description] : ")

st.write('**Brand:** The brand name of the laptop.\n')
st.write('**Model:** The model name or number of the laptop.\n')
st.write('**Ram:** The amount of RAM (Random Access Memory) in the laptop.\n')
st.write('**Rom:** The amount of storage (Read Only Memory) in the laptop.\n')
st.write('**Processor:** The name of the processor in the laptop.\n')
st.write('**Price Category:** The price category of the laptop.\n')
st.write('**Processor Type:** The type of processor in the laptop (e.g. Intel Core i5, AMD Ryzen 7, etc.).\n')
st.write('**Rom Type:** The type of storage in the laptop (e.g. SSD, HDD, etc.).\n')
st.write('**Price (₹):** The price of the laptop in Indian rupees.\n')
st.write('**Website:** The website from which the laptop was obtained.\n')

# Display the dataset
st.write('## Laptop Dataset\n')
st.write(laptop_df)

