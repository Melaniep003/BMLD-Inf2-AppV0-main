import streamlit as st

st.title("Medikamenten Dosierungsrechner")

st.write("Diese Seite ist eine Unterseite der Startseite.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 🧮 GFR-Berechnung (Cockcroft-Gault-Formel)
def berechne_gfr(alter, gewicht, kreatinin, geschlecht):
    gfr = ((140 - alter) * gewicht) / (72 * kreatinin)
    if geschlecht == "Weiblich":
        gfr *= 0.85  # Frauen haben eine ca. 15% niedrigere GFR
    return round(gfr, 1)

# 🧮 Medikamenten-Dosierung berechnen
def berechne_dosis(medikament, gewicht, gfr, blutzucker):
    dosierungen = {
        "Paracetamol": 15,  # mg/kg
        "Ibuprofen": 10,
        "Amoxicillin": 50,
        "Metformin": 500,  # Standarddosis
        "Heparin": 80,  # Einheiten/kg
        "Insulin": None,  # Berechnung nach Blutzucker
        "Vancomycin": 15,  # mg/kg
        "Ciprofloxacin": None  # GFR-abhängig
    }

    if medikament not in dosierungen:
        return "Medikament nicht gefunden."

    if medikament in ["Paracetamol", "Ibuprofen", "Amoxicillin", "Vancomycin"]:
        normale_dosis = dosierungen[medikament] * gewicht
    elif medikament == "Metformin":
        if gfr < 30:
            return "❌ Metformin kontraindiziert bei GFR < 30!"
        elif gfr < 60:
            normale_dosis = dosierungen[medikament] * 0.5
        else:
            normale_dosis = dosierungen[medikament]
    elif medikament == "Heparin":
        normale_dosis = dosierungen[medikament] * gewicht
    elif medikament == "Insulin":
        if blutzucker < 140:
            return "✅ Kein Insulin nötig."
        elif blutzucker < 200:
            normale_dosis = 2
        elif blutzucker < 250:
            normale_dosis = 4
        else:
            normale_dosis = 6
    elif medikament == "Ciprofloxacin":
        if gfr < 30:
            normale_dosis = 250
        else:
            normale_dosis = 500

    if medikament in ["Paracetamol", "Ibuprofen", "Amoxicillin", "Vancomycin"] and gfr < 60:
        reduzierte_dosis = normale_dosis * 0.75
        return f"⚠️ Empfohlene Dosis: {reduzierte_dosis:.1f} mg (GFR < 60!)"
    
    return f"✅ Empfohlene Dosis: {normale_dosis:.1f} mg"


# 📌 **Streamlit UI**
st.title("💊 Medikamenten-Dosierungsrechner mit GFR-Berechnung")

# 📊 **GFR berechnen lassen**
st.header("🔬 Nierenfunktion berechnen")

alter = st.number_input("Alter (Jahre):", min_value=1, step=1)
gewicht = st.number_input("Gewicht (kg):", min_value=1.0, step=0.1)
geschlecht = st.radio("Geschlecht:", ["Männlich", "Weiblich"])
kreatinin = st.number_input("Serum-Kreatinin (mg/dl):", min_value=0.1, step=0.1)

if st.button("GFR berechnen"):
    gfr = berechne_gfr(alter, gewicht, kreatinin, geschlecht)
    st.success(f"🩺 Geschätzte GFR: {gfr} ml/min")

# 📌 **Medikamenten-Dosierung**
st.header("💊 Medikamenten-Dosierung berechnen")

medikament = st.selectbox("Wähle ein Medikament:", ["Paracetamol", "Ibuprofen", "Amoxicillin", "Metformin", "Heparin", "Insulin", "Vancomycin", "Ciprofloxacin"])
if medikament == "Insulin":
    blutzucker = st.number_input("Blutzuckerwert eingeben (mg/dl):", min_value=50, step=1)
else:
    blutzucker = None

if st.button("Dosis berechnen"):
    if "gfr" not in locals():
        st.error("❌ Bitte erst die GFR berechnen!")
    else:
        ergebnis = berechne_dosis(medikament, gewicht, gfr, blutzucker)
        st.success(ergebnis)

# 📊 **Insulin-Dosis-Kurve**
if medikament == "Insulin":
    st.subheader("📈 Insulin-Dosis-Kurve")
    blutzucker_werte = [100, 140, 180, 200, 220, 250, 300]
    insulindosen = [0, 2, 2, 4, 4, 6, 6]

    plt.figure(figsize=(5,3))
    plt.plot(blutzucker_werte, insulindosen, marker='o', linestyle='-', color='b')
    plt.xlabel("Blutzucker (mg/dl)")
    plt.ylabel("Insulin (Einheiten)")
    plt.title("Insulin-Dosierung")
    plt.grid()
    st.pyplot(plt)
