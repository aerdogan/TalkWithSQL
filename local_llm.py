from ollama import chat
from schema import schema

system_msg = f"""
    Sen bir SQL kodu üreticisisin. Sana verilen doğal dil sorularını, 
    aşağıdaki veritabanı şemasına uygun SQL sorgularına dönüştüreceksin. 
    şemada bulunan ingilizce tablo ve alan isimlerini kullanmalısın. şemada olmayan hiçbir tanım üretme.
    ilişkisel alanlar book_id, user_id gibi belirtilmiştir.
    inser update ve delete işlemlerinde ilişkisel sorgu oluşturmana gerek yok.
    kullanıcılar users, kitaplar books, kiralama ve teslim etme işlemleri ise book_events tablosunda yer almaktadır.
    Sadece ve sadece SQL kodunu döndür. Başka bir açıklama yapma.
    Veritabanı Şeması:
    {schema}
    """

def ask_ollama(prompt):
    resp = chat(
        model= "qwen2.5-coder:1.5b", #"deepcoder:1.5b", #"qwen2.5-coder:1.5b", #"qwen3:1.7b", #"gemma3:1b",#"deepseek-r1:1.5b"
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return resp["message"]["content"].strip()


from dotenv import load_dotenv
load_dotenv()

def ask_gemini(prompt):
    import os
    import google.generativeai as genai
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))    
    model = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[{"role": "user", "parts": [system_msg]}])
    response = model.send_message(prompt)    
    return response.text.strip()


def ask_chatgpt(prompt):
    import os
    from openai import OpenAI

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('ROUTER_API_KEY'),
    )

    completion = client.chat.completions.create(
        extra_headers={"HTTP-Referer": "localhost", "X-Title": "localhost"},
        extra_body={},
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt }
        ]
    )
    return completion.choices[0].message.content.strip()
