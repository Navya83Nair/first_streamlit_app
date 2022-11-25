import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header(' Breakfast Menu  ')
streamlit.write('Banana','Apple', 'Chikku', 'Milk')  
streamlit.text('Curd and Muesli')
streamlit.header('🍌 :zap: Hello!!! Build Your Own Fruit Smoothie :smile: 🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.fruit))

streamlit.dataframe(my_fruit_list)
