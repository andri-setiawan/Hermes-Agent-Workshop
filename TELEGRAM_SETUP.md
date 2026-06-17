# Telegram Bot & Account ID

![telegram-web](screenshots/05a_telegram_web.png)

## 1. Create Bot
- Chat with [@BotFather](https://t.me/botfather)
- `/newbot` -> Name & Username
- Copy API Token

## 2. Add Token to .env
```bash
echo "TELEGRAM_TOKEN=your_b...re" >> ~/.hermes/.env
```

## 3. Get Your Account ID
- Chat with [@userinfobot](https://t.me/userinfobot)
- Your numeric ID is the first message

## 4. Configure Gateway
```bash
hermes gateway setup
```

![telegram-api](screenshots/05b_my_telegram.png)

## 5. Run
```bash
hermes gateway run
```
