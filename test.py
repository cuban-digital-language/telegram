import asyncio
from telethon import TelegramClient, events

api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

async def main():
  client = TelegramClient('session_name', api_id, api_hash,)
  await client.start("+5353029854")

asyncio.run(main())