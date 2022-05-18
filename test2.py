from telethon import TelegramClient
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

client = TelegramClient('test', api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())