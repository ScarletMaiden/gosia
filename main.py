import pandas as pd
import streamlit as st


FILE_PATH = "takk.xlsx"


COLS = [' nr zamówienia', 'nr badania', 'status ', 'imię konia',
        'Anoplocephala perfoliata', 'Oxyuris equi', 'Parascaris equorum',
        'Strongyloides spp', 'Kod-pocztowy ', 'Miasto ']

df = pd.read_excel(FILE_PATH)


df = df[[c for c in COLS if c in df.columns]]


st.set_page_config(page_title="Zamówienia", page_icon="📦", layout="wide")
st.title("📦 Podgląd i dodawanie zamówień")


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

