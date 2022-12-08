import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header(' Breakfast Menu  ')
streamlit.write('Banana','Apple', 'Chikku', 'Milk')  
streamlit.text('Curd and Muesli')
streamlit.header('🍌 :zap: Hello!!! Build Your Own Fruit Smoothie :smile: 🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#Create repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
  fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()


#import snowflake.connector
streamlit.header("Fruit Load List contains:")
#snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)

# Allow the use r to add a fruit to the list
def insert_row_snowflake(new_fruit)
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding "+ new_fruit
  
add_fruit = streamlit.text_input('Which fruit would you like to add?')
if streamlit.button('Add a fruit to the List'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_fruit)
  streamlit.text(back_from_function)
  
  
#Dont run anything past here while we troubleshoot
streamlit.stop()
add_fruit = streamlit.text_input('Which fruit would you like to add?','banana')
streamlit.write(, add_fruit)

my_cur.execute(" insert into fruit_load_list values ('from streamlit')")
