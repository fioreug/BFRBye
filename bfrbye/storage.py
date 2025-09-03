import csv
import requests
from datetime import datetime
from pathlib import Path

class NotionClient():
    def __init__(self, token: str, database_id: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        self.database_id = database_id
    
    def send_to_db(self, text: str, date):
        

        data = {
            "parent": {"database_id": self.database_id},
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
        res = requests.post(url, headers=self.headers, json=data)
        
        if res.status_code == 200:
            print("Saved in Notion")
        else:
            print("Error:", res.text)

def save_response(response: str, config: dict):

    date = datetime.now().isoformat()
    method = config["storage"]["method"]

    if method == "csv":
        file = Path(config["storage"]["output_file"])
        with open(file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, response])

    if method == "txt":
        file = Path(config["storage"]["output_file"])
        with open(file, "a") as f:
            f.write(f"{date},{response}\n")

    if method == "notion":
        notion = NotionClient(config["notion"]["token"],config["notion"]["database_id"])
        notion.send_to_db(response, date)