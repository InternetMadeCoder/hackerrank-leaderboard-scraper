import requests
import pandas as pd

contest_slug = 'muj-cse-dsa-2'
url = f'https://www.hackerrank.com/rest/contests/{contest_slug}/leaderboard'

all_entries = []
offset = 0
limit = 10

headers = {
    "Cookie": "YOUR_COOKIE",
    "User-Agent": "YOUR_USER_AGENT"
}

while True:
    params = {'offset': offset, 'limit': limit}
    response = requests.get(url, params=params, headers=headers)
    
    try:
        data = response.json()
    except:
        print("Error: Could not parse JSON. Check login/session headers.")
        break
    
    entries = data.get('models', [])
    if not entries:  
        break
    
    all_entries.extend(entries)
    offset += limit



df = pd.DataFrame(all_entries)
df.to_excel('full_leaderboard.xlsx', index=False)
print(f"Saved {len(all_entries)} entries to full_leaderboard.xlsx")
