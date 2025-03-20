import streamlit as st
import pandas as pd
import plotly.express as px

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

st.title('Dosierungsrechner Verlauf')

# Laden der Dosierungsdaten aus dem Session State
data_df = st.session_state.get('data_df', load_data())

# Überprüfen, ob Daten vorhanden sind
if data_df.empty:
    st.info('Keine Dosierungsrechner Daten vorhanden. Berechnen Sie Ihre Dosierung auf der Startseite.')
    st.stop()

# Daten nach Zeitstempel sortieren
data_df = data_df.sort_values('timestamp')

# Liniendiagramm der Dosierung über die Zeit erstellen
fig = px.line(data_df, x='timestamp', y='dosierung', title='Dosierung über die Zeit')
fig.update_layout(xaxis_title='Zeitpunkt', yaxis_title='Dosierung')

# Diagramm in Streamlit anzeigen
st.plotly_chart(fig, use_container_width=True)