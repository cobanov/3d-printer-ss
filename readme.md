# 3D Printer SS

## How to get Telegram Bot Chat ID

### Create a Telegram Bot and get a Bot Token

1. Open Telegram application then search for `@BotFather`
2. Click Start
3. Click Menu -> /newbot or type `/newbot` and hit Send
4. Follow the instruction until we get message like so

    ```txt
    Done! Congratulations on your new bot. You will find it at t.me/new_bot.
    You can now add a description.....

    Use this token to access the HTTP API:
    63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
    Keep your token secure and store it safely, it can be used by anyone to control your bot.

    For a description of the Bot API, see this page: https://core.telegram.org/bots/api
    ```

5. So here is our bot token `63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c` (make sure we don't share it to anyone).

### Get Chat ID for a Private Chat

1. Search and open our new Telegram bot
2. Click Start or send a message
3. Open this URL in a browser `https://api.telegram.org/bot{our_bot_token}/getUpdates`
    - See we need to prefix our token with a wor `bot`
    - Eg: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/getUpdates`
4. We will see a json like so

    ```json
    {
      "ok": true,
      "result": [
        {
          "update_id": 83xxxxx35,
          "message": {
            "message_id": 2643,
            "from": {...},
            "chat": {
              "id": 21xxxxx38,
              "first_name": "...",
              "last_name": "...",
              "username": "@username",
              "type": "private"
            },
            "date": 1703062972,
            "text": "/start"
          }
        }
      ]
    }
    ```

5. Check the value of `result.0.message.chat.id`, and here is our Chat ID: `21xxxxx38`
6. Let's try to send a message: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/sendMessage?chat_id=21xxxxx38&text=test123`
7. When we set the bot token and chat id correctly, the message `test123` should be arrived on our Telegram bot chat.
