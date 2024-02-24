import disnake
from disnake.ext import commands

import pathlib
from pathlib import Path

import os
from dotenv import load_dotenv

import config.config as cfg

dir_path = pathlib.Path.cwd()

path_env = Path('bot_token', 'bot_token.env')

load_dotenv(dotenv_path=path_env)


intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(cfg.on_member_join))

    embed = disnake.Embed(
        title=f"{member} присоединился к серверу!",
        description=f"Добро пожаловать! Пожалуйста ознакомься с каналом <#1051486016634105866>.",
        color=0x00ff00
    )

    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(cfg.on_member_remove))

    embed = disnake.Embed(
        title=f"{member} покинул сервер...",
        description="Мы будем ждать тебя снова.",
        color=0xff0000
    )

    await channel.send(embed=embed)


path_cogs = Path("cogs")
for file in os.listdir(path_cogs):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)
