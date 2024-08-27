import streamlit as st
from stmol import showmol
import py3Dmol

st.title('🎈 stmol')

# Structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA
xyzview = py3Dmol.view(query='pdb:1A2C') 
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)
