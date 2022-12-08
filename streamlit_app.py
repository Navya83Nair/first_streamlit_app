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

streamlit.header('Fruityvice Fruit Advice')
try:
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") #separated base url from fruit name
#streamlit.text(fruityvice_response.json())
#Enter choice of fruit
  fruit_choice = streamlit.text_input('What fruit would you likr information about?')
   streamlit.write('The user entered', fruit_choice)
   if not fruit_choice:
           streamlit.error('Please select a fruit to get information.')
    else:
           #import requests
            fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) #separated base url from fruit name
            #take the fruityvice_response into normalized form
            fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
            #put the output in a table
            streamlit.dataframe(fruityvice_normalize)
 except URLError as e:
    streamlit.error()

#Dont run anything past here while we troubleshoot
streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("Fruit Load List contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('Which fruit would you like to add?','banana')
streamlit.write('Thanks for adding ', add_fruit)

my_cur.execute(" insert into fruit_load_list values ('from streamlit')")
