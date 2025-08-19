import schema, re
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from local_llm import ask_ollama, ask_gemini

engine = create_engine("sqlite:///ornek.db")

st.subheader("📚 LLM Destekli Kütüphane Sistemi")
user_input = st.text_area("SQL olarak çalıştırmak istediğiniz sorguyu yazın (yalnızca SQL döndür):")

if st.button("Çalıştır"):
    with st.spinner("Lütfen bekleyin, işlem yapılıyor..."):
        #sql_query = ask_ollama(user_input, schema)
        sql_query = ask_gemini(user_input, schema)

        rawsql = re.sub(r"```sql|```", "", sql_query).strip()
        print(rawsql)
        st.code(rawsql, language="sql")
        try:
            if rawsql.strip().lower().startswith("select"):
                df = pd.read_sql(rawsql, engine)
                st.dataframe(df)
            else:
                with engine.begin() as conn:  # otomatik commit
                    conn.execute(text(rawsql))
                st.success("✅ Sorgu başarıyla çalıştırıldı.")
        except Exception as e:
            st.error(f"Hata: {e}")
