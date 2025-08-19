import re
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from local_llm import ask_ollama, ask_gemini, ask_chatgpt

engine = create_engine("sqlite:///ornek.db")

st.subheader("📚 LLM Destekli Kütüphane Sistemi")
user_input = st.text_area("SQL olarak çalıştırmak istediğiniz sorguyu yazın (yalnızca SQL döndür):")

if st.button("Çalıştır"):
    with st.spinner("Lütfen bekleyin, işlem yapılıyor..."):
        #sql_query = ask_ollama(user_input)
        #sql_query = ask_gemini(user_input)
        sql_query = ask_chatgpt(user_input)
        rawsql = re.sub(r"```sql|```", "", sql_query).strip()
        st.code(rawsql, language="sql")
        try:
            if rawsql.strip().lower().startswith("select"):
                df = pd.read_sql(rawsql, engine)
                st.dataframe(df)
            else:
                with engine.begin() as conn:
                    conn.execute(text(rawsql))
                st.success("✅ Sorgu başarıyla çalıştırıldı.")
        except Exception as e:
            st.error(f"Hata: {e}")
