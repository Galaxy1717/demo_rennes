import streamlit as st
import json

with open('data/references.json', 'r') as f:
    mapping_mat_ref = json.load(f)

with open('data/matching_results.json', 'r') as f:
    mapping = json.load(f)

MATIERES = list(mapping.keys())

st.set_page_config(page_title="Matching ROME - RNCP", layout="wide")

st.title("Demo Rennes Business School: Matching Matiere - Competences")

# Dropdown to select reference
selected_reference = st.selectbox("Choix de la matière:", MATIERES, key="selected_reference")

course = mapping_mat_ref[selected_reference]
elements = mapping[selected_reference]
rncp = elements["rncp"]
rome = elements["rome"]

st.markdown(f"### Matière sélectionnée: {selected_reference}")
if st.checkbox('Show content preview'):
    st.markdown(course.replace("\n", "\n\n"), unsafe_allow_html=True)
best_rome = [(element[0], element[1]) for element in rome if element[1]["score"] >= 9]
st.markdown("---")
st.markdown(f"### {len(best_rome)} compétences ROME liés")
st.markdown("**Source: ~13 000 micro compétences ROME  - score de pertinence supérieur à 9/10**")
new_collection = []
for competence, score in best_rome:
    new_dic = {}
    new_dic["competence"] = competence["micro_competency"]
    new_dic["macro competence"] = competence["macro_competency"]
    new_dic["score de pertinence"] = score["score"]
    new_dic["justification"] = score["justification"]
    new_dic["code arborescence"] = competence["code_arborescence"]
    new_dic["code ogr"] = competence["code_ogr"]
    new_dic["Objectif"] = competence["objective"]
    new_dic["Enjeu"] = competence["challenge"]
    new_dic["Domaine"] = competence["domain"]
    new_collection.append(new_dic)
st.json(new_collection)
best_rncp = [(element[0], element[1]) for element in rncp if element[1]["score"] >= 9]
st.markdown("---")
st.markdown(f"### {len(best_rncp)} compétences RNCP liés")
st.markdown("**Source: ~25 000 compétences RNCP actives - score de pertinence supérieur à 9/10**")
new_collection = []
for competence, score in best_rncp:
    new_dic = {}
    new_dic["competence"] = competence["competency"]
    new_dic["fiche rncp"] = competence["fiche_name"]
    new_dic["score de pertinence"] = score["score"]
    new_dic["justification"] = score["justification"]
    new_dic["code"] = competence["competency_code"]
    new_collection.append(new_dic)
st.json(new_collection)
