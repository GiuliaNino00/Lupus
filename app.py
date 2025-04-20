
import streamlit as st
import random

# Lista dei partecipanti
players = ["Cosimo", "Giuliano", "Nadia", "Vincenzo", "Marina", "Anna"]

# Inizializzazione dello stato
if "shuffled_roles" not in st.session_state:
    roles = ["Lupo", "Bodyguard"] + ["Cittadino"] * (len(players) - 2)
    random.shuffle(roles)
    st.session_state.shuffled_roles = roles
    st.session_state.current_index = 0
    st.session_state.show_black_screen = True

# Titolo
st.title("Estrazione dei Ruoli")

# Variabili utili
i = st.session_state.current_index
show_black = st.session_state.show_black_screen

# Se siamo alla fine
if i >= len(players):
    st.success("Tutti hanno visto il loro ruolo!")
    st.stop()

# Schermata nera
if show_black:
    st.markdown("## Passa il telefono a:")
    st.markdown(f"### **{players[i]}**")
    st.markdown("---")
    st.markdown("#### Tocca il pulsante qui sotto per vedere il tuo ruolo")
    st.button("Vedi il tuo ruolo", on_click=lambda: st.session_state.update({"show_black_screen": False}))
else:
    st.markdown(f"## Ciao, {players[i]}!")
    st.markdown(f"### Il tuo ruolo è: **{st.session_state.shuffled_roles[i]}**")
    st.markdown("---")
    st.button("Passa il telefono al prossimo", on_click=lambda: st.session_state.update({
        "current_index": i + 1,
        "show_black_screen": True
    }))
