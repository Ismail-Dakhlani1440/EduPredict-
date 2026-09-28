from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

DOSSIER = Path(__file__).parent / "models"
SEUIL_RISQUE = 65

LMH = {"Low": 0, "Medium": 1, "High": 2}
NUMERIQUES = {
    "Hours_Studied": (1, 44, 20),
    "Attendance": (60, 100, 80),
    "Sleep_Hours": (4, 10, 7),
    "Previous_Scores": (50, 100, 75),
    "Tutoring_Sessions": (0, 8, 1),
    "Physical_Activity": (0, 6, 3),
}
ORDINALES = {
    "Parental_Involvement": LMH,
    "Access_to_Resources": LMH,
    "Motivation_Level": LMH,
    "Family_Income": LMH,
    "Teacher_Quality": LMH,
    "Parental_Education_Level": {"High School": 0, "College": 1, "Postgraduate": 2},
    "Distance_from_Home": {"Near": 0, "Moderate": 1, "Far": 2},
}
NOMINALES = {
    "Gender": ["Female", "Male"],
    "School_Type": ["Private", "Public"],
    "Extracurricular_Activities": ["No", "Yes"],
    "Internet_Access": ["No", "Yes"],
    "Learning_Disabilities": ["No", "Yes"],
    "Peer_Influence": ["Negative", "Neutral", "Positive"],
}


@st.cache_resource
def charger():
    return (joblib.load(DOSSIER / "final_pipeline.joblib"),
            joblib.load(DOSSIER / "columns.joblib"))


st.title("EduPredict : score d'examen")

try:
    modele, colonnes = charger()
except FileNotFoundError:
    st.error("Modèle introuvable : exportez-le depuis le notebook dans models/.")
    st.stop()

ligne = pd.DataFrame(0, index=[0], columns=colonnes)

for col, (mini, maxi, defaut) in NUMERIQUES.items():
    ligne[col] = st.slider(col, mini, maxi, defaut)
for col, mapping in ORDINALES.items():
    ligne[col] = mapping[st.selectbox(col, list(mapping))]
for col, choix in NOMINALES.items():
    nom = f"{col}_{st.selectbox(col, choix)}"
    if nom in ligne.columns:
        ligne[nom] = 1

if st.button("Prédire"):
    score = float(modele.predict(ligne[colonnes])[0])
    st.metric("Score estimé", f"{score:.1f}")
    if score < SEUIL_RISQUE:
        st.error("Étudiant à risque")
    else:
        st.success("Pas de risque détecté")