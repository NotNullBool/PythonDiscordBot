""" Discord Bot Application
"""
import discord
import meta_info_handler

TOKEN: str = meta_info_handler.get_token()

class MyClient(discord.Client):
    """MyClient The Base Client

    Args:
        discord (discord.Client): The base client info for bot
    """
    async def on_ready(self):
        """on_ready when bot first starts
        """
        print(f"Logged on as {self.user}")
    async def on_message(self, message: discord.Message):
        """on_message when message is sent in discord

        Args:
            message (discord.Message): message info
        """
        print(f"Message from {message.author}: {message.content}")

if __name__ == "__main__":
    client = MyClient()
    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print("token.json needs a valid token")
