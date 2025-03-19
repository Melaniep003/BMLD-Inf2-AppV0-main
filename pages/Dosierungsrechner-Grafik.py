import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dosierungsrechner Verlauf')

# Laden der Dosierungsdaten aus dem Session State
data_df = st.session_state.get('data_df', pd.DataFrame())

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