import json
import requests
import os
import time

script_dir = os.path.dirname(os.path.realpath(__file__))

with open("stars.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    with open("stars2.json", "w+", encoding="utf-8") as json_file2:
        json_file2.write(json.dumps(json_data, ensure_ascii=False, indent=4))

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
}

for row in json_data["rows"]:
    if "img_url" in row and len(row["img_url"].strip()) != 0:
        file_url = f"https://ceremony.ckg48.com/{row['img_url']}"
        file_name = (
            f"{row['sid']}_{row['sname']}_2024_{os.path.basename(row['img_url'])}"
        )
        try:
            response = requests.get(url=file_url, headers=headers, timeout=10)
            response.raise_for_status()
            with open(f"{script_dir}/note_2024/{file_name}", "wb+") as file_bin:
                file_bin.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {file_url}: {e}")
        time.sleep(2)
