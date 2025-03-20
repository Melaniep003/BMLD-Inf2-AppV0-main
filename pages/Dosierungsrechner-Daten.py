import streamlit as st
import pandas as pd

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# Funktion zum Laden der Daten
def load_data():
    try:
        return pd.read_csv('data.csv', parse_dates=['timestamp'])
    except FileNotFoundError:
        return pd.DataFrame(columns=['timestamp', 'gewicht', 'dosierung'])

st.title('Dosierungsrechner Daten')

# Laden der Dosierungsdaten aus dem Session State
data_df = st.session_state.get('data_df', load_data())

# Überprüfen, ob Daten vorhanden sind
if data_df.empty:
    st.info('Keine Dosierungsrechner Daten vorhanden. Berechnen Sie Ihre Dosierung auf der Startseite.')
    st.stop()

# Daten nach Zeitstempel sortieren
data_df = data_df.sort_values('timestamp', ascending=False)

# Tabelle anzeigen
st.dataframe(data_df)