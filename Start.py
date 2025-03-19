# === Initialize the data manager ===
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 



# === Initialize the login manager ===
from utils.login_manager import LoginManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# === Start with actual app ===
import streamlit as st
import pandas as pd

st.title("Dosierungsrechner")

"""
Diese App wurde von folgenden Personen entwickelt:
- Melanie Pomellitto (pomelmel@students.zhaw.ch)


Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)


"""