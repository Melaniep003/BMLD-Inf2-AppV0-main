import streamlit as st

# Streamlit App Titel
st.title("Medikamenten-Dosierungsrechner mit Geschlecht")

# Sidebar für Eingaben
st.header("Eingabeparameter")

# Formular für die Berechnung
with st.form(key='dosierungs_form'):
    # Eingabe: Körpergewicht des Patienten
    gewicht = st.number_input("Körpergewicht (kg)", min_value=1, max_value=200, value=70, step=1)
    
    # Eingabe: Dosierung pro Kilogramm Körpergewicht
    dosierung_pro_kg = st.number_input("Dosierung (mg/kg)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
    
    # Eingabe: Geschlecht
    geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich"])
    
    # Formular-Absende-Button
    submit_button = st.form_submit_button(label="Berechnen")

# Berechnung der gesamten Medikamentendosis nach Absenden des Formulars
if submit_button:
    # Optional: Beispiel einer Anpassung der Dosis basierend auf Geschlecht
    if geschlecht == "Weiblich":
        # Beispiel: Frauen erhalten 90% der Standarddosis
        dosis = gewicht * dosierung_pro_kg * 0.9
    else:
        dosis = gewicht * dosierung_pro_kg

    st.write(f"Die berechnete Medikamentendosis für eine {geschlecht.lower()} Person mit {gewicht} kg Körpergewicht beträgt {dosis} mg.")
