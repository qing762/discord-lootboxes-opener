> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

> [!WARNING]
> Please be advised that usage of this tool is entirely at your own risk. I assumes no responsibility for any adverse consequences that may arise from its use, and users are encouraged to exercise caution and exercise their own judgment in utilizing this tool.

# Discord Lootbox Opener
A simple tool that works to open [Discord's new released lootboxes](https://www.youtube.com/watch?v=cc2-4ci4G84).

## Run this tool

Before starting, you should had your Discord user token in order to run this tool. To get your Discord user token, follow the steps below:
1. Go to Discord
2. Open the browser's console (Option (⌥) + Command (⌘) + J (on macOS) or Shift + CTRL + J (on Windows/Linux)).
3. Paste the following code to the console
```javascript
console.log((webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken())
```
4. Copy the value given (**DO NOT SHARE THE VALUE TO ANYONE, THEY CAN HAVE DIRECT ACCESS TO YOUR ACCOUNT AND BYPASS 2FA IF GIVEN!**)

### Run Locally

To run this tool yourself, follow the steps below:

1. Clone the project

```bash
  git clone https://github.com/qing762/discord-lootboxes-opener
```

2. Go to the project directory

```bash
  cd discord-lootboxes-opener
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```

4. Run the code 

```bash
  python main.py
```

5. Enter your Discord user token value in the `.env` file / __in your pc environment variables__ (this is more recommend personally).

```dotenv
AUTH_VALUE=YOUR VALUE
```

You should get a 200 status code and a json of your lootbox data after this, meaning that the lootboxes had successfully opened.


### Automation

To automate the lootbox opening process, follow the steps below:

1. [Fork the project.](https://github.com/qing762/discord-lootboxes-opener/fork)

2. [You can set the intervals between each execution at line 5 by using cron format.](https://github.com/qing762/discord-lootboxes-opener/blob/master/.github/workflows/automate.yml) (This is completely optional, by default it's every minute once)

3. Go to your forked repository, head to Settings > Secrets and Variables > Actions and click the button `New Repository secret`.

4. Enter your `AUTH_VALUE` as the secret name and your Discord user token value as the secret value.

5. Lastly, go the your forked repository and go the Actions tab and press the button `I understand my workflows, go ahead and enable them`.

You should get a 200 status code and a json of your lootbox data after the Github Actions finished the instance, meaning that the lootboxes had successfully opened.


## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.

## Feedback / Issues

If you have any feedback or issues running the code, please join the [Discord server](https://qing762.is-a.dev/discord)

### FOR DISCORD INC. EMPLOYEES IF YOU WISH TO REQUEST FOR TAKING DOWN THIS PROJECT

If the company wishes to discontinue or terminate this project, please do not hesitate to reach out to me. I can be reached at [Discord/qing762](https://discord.com/users/635765555277725696). Thank you for your attention to this matter.


## License

[MIT LICENSE](https://choosealicense.com/licenses/mit/)


