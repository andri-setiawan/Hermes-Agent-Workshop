# Telegram Bot & Account ID

## 1. Create Bot
- Chat with [@BotFather](https://t.me/botfather)
- `/newbot` -> Name & Username
- Copy API Token

## 2. Add Token to .env
```bash
echo "TELEGRAM_TOKEN=your_bot_token_here" >> ~/.hermes/.env
```

## 3. Get Your Account ID
- Chat with [@userinfobot](https://t.me/userinfobot)
- Your numeric ID is the first message

## 4. Configure Gateway
```bash
hermes gateway setup
```

## 5. Run
```bash
hermes gateway run
```
