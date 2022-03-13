import os

from dotenv import load_dotenv

import pyvolt

client = pyvolt.Client()


@client.listen("message", raw=True)
async def my_message_listener_any_name_is_ok(payload):
    if payload["content"] == "-ping":
        await client.http.send_message(payload["channel"], "pong")
    if payload["content"] == "-embed":
        await client.http.send_message(payload["channel"], "h", embeds=[{"title": "h"}])


load_dotenv()
client.run(os.getenv("token"))
