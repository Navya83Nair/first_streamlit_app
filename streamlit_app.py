import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header(' Breakfast Menu  ')
streamlit.write('Banana','Apple', 'Chikku', 'Milk')  
streamlit.text('Curd and Muesli')
streamlit.header('🍌 :zap: Build Your Own Fruit Smoothie :smile: 🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
