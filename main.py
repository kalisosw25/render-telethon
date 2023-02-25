# pip3 install -r requirements.txt
# python3 main.py
# python3 t.py
# +16802051325

# apt-get update
# apt-get install screen
# screen
# python3 index.py



import asyncio
import telebot
import time

tg_id = "1357007249"
API_TOKEN = '1965634792:AAGSAHkmaYIGQ-0iV0T5Hapfn4THdm3YXnM'
bot = telebot.TeleBot(API_TOKEN)
async def main():
    bot.send_message(tg_id, "render working")
    time.sleep(60)
    
    
while True:
  try:
    asyncio.get_event_loop().run_until_complete(main())
  except Exception as e: 
    # print(e)
    # print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
    print(f"[ERROR]: {type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")

