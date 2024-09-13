import requests
import os
import base64
import time
from dotenv import load_dotenv

load_dotenv()


def main():
    auth = os.environ.get("AUTH_VALUE")

    url = "https://discord.com/api/v9/users/@me/lootboxes/open"
    headers = {
        "Accept-Language": "en-US,zh-Hans-CN;q=0.9,ko;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": auth,
        "Content-Length": "0",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/970305017238159440/1044866457210736660",
        "Sec-Fetch-Site": "same-origin",
        "X-Discord-Timezone": "Asia/Kuala_Lumpur",
        "X-Super-Properties": base64.b64encode(
            '{"os": "Windows", "client_build_number": 282068}'.encode("ascii")
        ).decode("ascii"),
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
        "Accept": "*/*",
        "X-Discord-Locale": "en-GB",
        "X-Debug-Options": "bugReporterEnabled",
        "Sec-Fetch-Mode": "cors",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
    }
    response = requests.post(url, headers=headers)
    print(response.status_code, response.text)
    if response.status_code == 200:
        print("Lootbox opened!")
    else:
        print("Failed to open lootbox! Status code:", response.status_code)


if __name__ == "__main__":
    times = 1
    for times in range(times):
        main()
        print("\n")
        time.sleep(2)
    print("Done!")
