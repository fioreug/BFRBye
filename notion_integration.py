import requests
import datetime

NOTION_TOKEN = ""  # token de la integración
DATABASE_ID = ""  # ID de base de datos en Notion

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def getDataBase():
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "database"}
    }

    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 200:
        data = res.json()
        for db in data.get("results", []):
            title = db["title"][0]["plain_text"] if db["title"] else "(sin título)"
            print(f"Nombre: {title}")
            print(f"ID: {db['id'].replace('-', '')}")  # limpio guiones
            print("-" * 40)
    else:
        print("Error:", res.status_code, res.text)

    exit()

def send_to_notion_db(text):
    date = datetime.datetime.now().isoformat()
    
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Why": {
                "title": [{"text": {"content": text}}]
            },
            "Date": {
                "date": {"start": date}
            }
        }
    }
    
    url = "https://api.notion.com/v1/pages"
    res = requests.post(url, headers=headers, json=data)
    
    if res.status_code == 200:
        print("Saved in Notion ")
    else:
        print("Error:", res.text)

# Ejemplo de uso
send_to_notion_db("test")