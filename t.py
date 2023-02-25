# pip3 install telethon

from telethon.sync import TelegramClient, events
api_id = 3347140
api_hash = "861f9a0dbf5c24b919f1f83e997ad79a"
with TelegramClient('shell', api_id, api_hash) as client:
   client.send_message('me', 'Hello, myself!')
   # print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*#captcha_audio'))
   async def handler(event):
      # await event.reply('Hey!')
      # print(event.stringify())
      # print(event.message.message)
      mess = event.message.message
      await client.send_message("@our_test_bbot", mess)

   client.run_until_disconnected()