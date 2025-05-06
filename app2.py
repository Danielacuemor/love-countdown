import streamlit as st
from datetime import datetime
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Love Countdown 💛", page_icon="💛")

# --- FECHA OBJETIVO ---
# Cambia esta fecha a la de su próximo encuentro
target_date = datetime(2025, 5, 15, 10, 20)

# --- CÁLCULO DEL CONTEO REGRESIVO ---
now = datetime.now()
time_left = target_date - now
days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# --- NOTAS DE AMOR ---
love_notes = [
    "You’ve been on my mind all day — I can’t wait to hold you 💛",
    "You make me feel safe, sexy, and silly — all at once 🥰",
    "I’ve never smiled this much just from someone’s messages 😘",
    "You are literally the highlight of my life 💫",
    "If home had a face, it would look exactly like yours 🏡"
]

# --- FRASES NOCTURNAS ---
bedtime_quotes = [
    "Sleep well, my love. You’re always in my dreams 🌙",
    "Another day closer to kissing you for real 💋",
    "I hope you feel how much you're loved, even from far away ✨",
    "Goodnight, my king. I’m already smiling thinking of you 🛌"
]

# --- INTERFAZ DE USUARIO ---
st.title("💛 Our Love Countdown 💛")
st.subheader("Until I'm in your arms...")

st.markdown(f"""
### 🗓️ {days} days  
⏰ {hours} hours, {minutes} minutes  
""")

st.divider()

# Nota de amor diaria
st.header("💌 Today's Note")
st.info(random.choice(love_notes))



st.divider()

# Frase para dormir
st.header("🌙 Tonight's Bedtime Thought")
st.write(random.choice(bedtime_quotes))

# Footer romántico
st.markdown("---")
st.caption("Made with love for David 💛")
