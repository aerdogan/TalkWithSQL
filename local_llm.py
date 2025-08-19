from ollama import chat

def ask_ollama(prompt, schema):
    system_msg = f"""
    Sen yalnızca geçerli SQL sorgusu döndüren bir SQL uzmanısın.
    Görev: Kullanıcının doğal dilde yazdığı isteğini SQL sorgusuna çevir. tablo isimleri alanlarda şemanın dışına çıkma.
    Kesinlikle açıklama, yorum veya başka metin ekleme. tablo isimleri ingilizcedir. kullanıcı istekleri türkçe olabilir.
    Yanıt yalnızca tek bir SQL sorgusu olmalı.
    Veritabanı şeması:
    {schema}
    """
    resp = chat(
        model= "deepcoder:1.5b", #"qwen2.5-coder:1.5b", #"qwen3:1.7b", #"gemma3:1b",#"deepseek-r1:1.5b"
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return resp["message"]["content"].strip()


from dotenv import load_dotenv
load_dotenv()

def ask_gemini(prompt, schema):
    import os
    import google.generativeai as genai

    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    system_msg = f"""
    Sen bir SQL kodu üreticisisin. Sana verilen doğal dil sorularını, 
    aşağıdaki veritabanı şemasına uygun SQL sorgularına dönüştüreceksin. 
    şemada bulunan ingilizce tablo ve alan isimlerini kullanmalısın. şemada olmayan hiçbir tanım üretme.
    inser update ve delete işlemlerinde ilişkisel sorgu oluşturmana gerek yok.
    Sadece ve sadece SQL kodunu döndür. Başka bir açıklama yapma.
    Veritabanı Şeması:
    {schema}
    """
    
    model = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[
        {
        "role": "user",
        "parts": [system_msg]
        },
    ])

    response = model.send_message(prompt)    
    return response.text.strip()
