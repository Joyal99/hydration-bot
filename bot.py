from telegram import Bot
import schedule
import asyncio
import random
from datetime import datetime
import time

BOT_TOKEN = "7263721084:AAFK92i3VHEZPK7qTke1YTGLG9F5sKJ1Gxs"
CHAT_ID = 5598573874   # Replace with your actual chat ID

MESSAGES = [
    "💧 Time to drink some water!",
    "🥤 Hydration break!",
    "🚰 Stay fresh, take a sip.",
    "🫗 You vs. dehydration. Drink now!",
    "⏰ Water alarm — fill that bottle!"
]

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    message = random.choice(MESSAGES)
    timestamp = datetime.now().strftime("%H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    await bot.send_message(chat_id=CHAT_ID, text=full_message)
    print(f"✅ Sent: {full_message}")

def job():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_message())
        loop.close()
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        
# Customize these times
schedule.every().day.at("23:12").do(job)
schedule.every().day.at("23:13").do(job)
schedule.every().day.at("23:14").do(job)
schedule.every().day.at("23:15").do(job)

print("🤖 Hydration bot is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
