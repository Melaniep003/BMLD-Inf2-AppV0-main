import streamlit as st
import pandas as pd

st.title('Dosierungsrechner Daten')

# Laden der Dosierungsdaten aus dem Session State
data_df = st.session_state.get('data_df', pd.DataFrame())

# Überprüfen, ob Daten vorhanden sind
if data_df.empty:
    st.info('Keine Dosierungsrechner Daten vorhanden. Berechnen Sie Ihre Dosierung auf der Startseite.')
    st.stop()

# Daten nach Zeitstempel sortieren
data_df = data_df.sort_values('timestamp', ascending=False)

# Tabelle anzeigen
st.dataframe(data_df)