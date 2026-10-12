import streamlit as st
st.title("Boutique NOVIDA - Goma")
st.write("Par Gloirerafiki de Goma")

if 'stock' not in st.session_state:
    st.session_state.stock = []
if 'solde' not in st.session_state:
    st.session_state.solde = 0.0

nom = st.text_input("Nom du produit (ex: Novida)")
achat = st.number_input("Prix d'achat", min_value=0.0)
vente = st.number_input("Prix de vente", min_value=0.0)
qte = st.number_input("Quantite", min_value=1, step=1)

if st.button("Ajouter"):
    benef = (vente - achat) * qte
    st.session_state.stock.append(f"{nom} - {qte} pcs - Benef {benef} $")
    st.session_state.solde += benef
    st.success("Ajoute!")

st.divider()
st.write(f"Solde total: {st.session_state.solde} $")
for p in st.session_state.stock:
    st.write(p)
