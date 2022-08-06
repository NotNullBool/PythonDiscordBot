""" Discord Bot Application
"""
import discord
import token_handler

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

client = MyClient()

client.run(token_handler.get_token())
