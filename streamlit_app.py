import streamlit as st
from stmol import showmol
import py3Dmol

st.title('🎈 stmol')

# Structure of Green Fluorescent Protein from Aequoria victoria
xyzview = py3Dmol.view(query='pdb:1EMA') 
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)
