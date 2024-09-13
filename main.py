import requests
import os
import base64
import time
from dotenv import load_dotenv

load_dotenv()


def checkDotEnv():
    checkDotenv = os.path.isfile("./.env")
    if checkDotenv is True:
        auth = os.environ.get("AUTH_VALUE")
        if auth is not None:
            return True
        else:
            with open(".env", "w") as x:
                print("The 'AUTH_VALUE' in the .env file seems to be empty.\n")
                token = input(
                    "Enter your Discord user token value, the script will automatically add into your .env file as your 'AUTH_VALUE' value\nValue: "
                )
                x.write(f"AUTH_VALUE={token}")
    else:
        with open(".env", "w") as x:
            print(
                ".env file couldn't be found.\nThis might be your first time running this script. It has been added.\n"
            )
            auth = os.environ.get("AUTH_VALUE")
            if auth is not None:
                print(
                    "Seems like you had set the 'AUTH_VALUE' in your .env file / pc environment variables. Continuing...\n"
                )
                return True
            else:
                with open(".env", "w") as x:
                    print("The 'AUTH_VALUE' in the .env file seems to be empty.\n")
                    token = input(
                        "Enter your Discord user token value, the script will automatically add into your .env file as your 'AUTH_VALUE' value\nValue: "
                    )
                    x.write(f"AUTH_VALUE={token}")


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
    if response.status_code == 200:
        item = {
            "1214340999644446720": "Buster Blade",
            "1214340999644446721": "Cute Plushie",
            "1214340999644446722": "Wump Shell",
            "1214340999644446723": "Speed Boost",
            "1214340999644446724": "⮕⬆⬇⮕⬆⬇",
            "1214340999644446725": "Power Helmet",
            "1214340999644446726": "Quack!!",
            "1214340999644446727": "OHHHHH BANANA",
            "1214340999644446728": "Dream Hammer",
        }
        if "opened_item" in response.json():
            openedItem = response.json()["opened_item"]
            if openedItem in item:
                print(
                    f"Lootbox opened! You just got: {item[openedItem]} (ID: {openedItem})"
                )
            else:
                print("The opened item is not recognized.")
    else:
        print(response.status_code, response.text)
        print("Failed to open lootbox! Status code:", response.status_code)


if __name__ == "__main__":
    checkDotEnv()
    times = input(
        "How many times you wish to open? Leave blank for default (∞)\nValue: "
    )
    print()
    auth = os.environ.get("AUTH_VALUE")
    discordID = (
        str(base64.b64decode(auth.split(".", 1)[0]).decode("utf-8")) if auth else None
    )

    query = """
        query Discord($userId: String!) {
            discord {
                lookup(userId: $userId) {
                    user {
                        id
                        type
                        username
                        displayName
                        accountAge
                        createdAt
                        creationTimestamp
                        badges {
                            title
                            description
                            url
                            __typename
                        }
                        profileAppearance {
                            accentColor
                            avatar {
                                url
                                __typename
                            }
                            avatarDecoration
                            banner {
                                url
                                __typename
                            }
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                __typename
            }
        }
    """

    response = requests.post(
        "https://api.discord.name/graphql",
        headers={
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "749",
            "Host": "api.discord.name",
            "Origin": "https://discord.name",
            "Referer": "https://discord.name/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "accept": "*/*",
            "content-type": "application/json",
            "sec-ch-ua": '"Brave";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
        },
        json={
            "operationName": "Discord",
            "variables": {"userId": discordID},
            "query": query,
        },
    )

    print(
        f'Login as: {response.json()["data"]["discord"]["lookup"]["user"]["username"]} (ID: {discordID})'
    )
    print("\u2500" * 50)
    if times:
        for x in range(int(times)):
            main()
            time.sleep(3)
    else:
        while True:
            main()
            time.sleep(3)
    print("Done!")
