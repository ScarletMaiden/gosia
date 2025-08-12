import pandas as pd
import streamlit as st

# Ścieżka do pliku (nazwa pliku z danymi)
FILE_PATH = "takk.xlsx"

# Kolumny, które chcemy wyświetlać
COLS = [' nr zamówienia', 'nr badania', 'status ', 'imię konia',
        'Anoplocephala perfoliata', 'Oxyuris equi', 'Parascaris equorum',
        'Strongyloides spp', 'Kod-pocztowy ', 'Miasto ']

# --- Wczytaj dane ---
df = pd.read_excel(FILE_PATH)

# Zostaw tylko wybrane kolumny (jeśli ich brakuje, pominie)
df = df[[c for c in COLS if c in df.columns]]

# --- Aplikacja ---
st.set_page_config(page_title="Zamówienia", page_icon="📦", layout="wide")
st.title("📦 Podgląd i dodawanie zamówień")

# Wyszukiwanie
with st.sidebar:
    st.header("🔎 Wyszukiwanie")
    q = st.text_input("Numer zamówienia (część lub całość)", placeholder="np. 12345")
    search = st.button("Szukaj")

st.subheader("Wyniki wyszukiwania")
if search and q.strip():
    mask = df[' nr zamówienia'].astype(str).str.contains(q.strip(), case=False, na=False)
    res = df.loc[mask]
    if res.empty:
        st.info("Brak wyników.")
    else:
        st.success(f"Znaleziono {len(res)} rekord(y).")
        st.dataframe(res, use_container_width=True)
else:

    st.dataframe(df, use_container_width=True)
