import os
import schedule
import asyncio
import random
import time
from datetime import datetime
from telegram import Bot
from flask import Flask

BOT_TOKEN = os.getenv("7263721084:AAFK92i3VHEZPK7qTke1YTGLG9F5sKJ1Gxs")
CHAT_ID = int(os.getenv(5598573874))   # Replace with your actual chat ID

MESSAGES = [
    "💧 Time to drink some water!",
    "🥤 Hydration break!",
    "🚰 Stay fresh, take a sip.",
    "🫗 You vs. dehydration. Drink now!",
    "⏰ Water alarm — fill that bottle!"
]

# Set up Telegram bot
async def send_message():
    bot = Bot(token=BOT_TOKEN)
    message = random.choice(MESSAGES)
    timestamp = datetime.now().strftime("%H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    await bot.send_message(chat_id=CHAT_ID, text=full_message)
    print(f"✅ Sent: {full_message}")

# Sync wrapper for schedule
def job():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_message())
        loop.close()
    except Exception as e:
        print(f"❌ Error sending message: {e}")

# Schedule your times
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("16:00").do(job)
schedule.every().day.at("20:00").do(job)

# Small web server to keep Replit alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Background thread to run scheduled jobs
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start bot + Flask
if __name__ == "__main__":
    import threading
    threading.Thread(target=run_schedule).start()
    app.run(host='0.0.0.0', port=8080)