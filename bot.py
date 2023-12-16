import disnake
from disnake.ext import commands

import pathlib
from pathlib import Path

import os
from dotenv import load_dotenv

dir_path = pathlib.Path.cwd()

path_cogs = Path('bot_token', 'bot_token.env')
path_channels = Path('bot_channels', '.env')

load_dotenv(dotenv_path=path_cogs)
load_dotenv(dotenv_path=path_channels)


intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


ON_MEMBER_JOIN = os.environ.get("ON_MEMBER_JOIN")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(ON_MEMBER_JOIN))

    embed = disnake.Embed(
        title=f"{member} присоединился к серверу!",
        description=f"Добро пожаловать! Пожалуйста ознакомься с каналом <#1051486016634105866>.",
        color=0x00ff00
    )

    await channel.send(embed=embed)


ON_MEMBER_REMOVE = os.environ.get("ON_MEMBER_REMOVE")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(ON_MEMBER_REMOVE))

    embed = disnake.Embed(
        title=f"{member} покинул сервер...",
        description="Мы будем ждать тебя снова.",
        color=0xff0000
    )

    await channel.send(embed=embed)


@bot.event
async def on_command_error(error):
    print()
    print(f'--- {error} ---')
    print()


@bot.event
async def on_slash_command_error(interaction, error):
    print()
    print(f'/// {error} ///')
    print()
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(f"{interaction.author}, у вас недостаточно прав для использования этой команды.")
    elif isinstance(error, commands.UserInputError):
        await interaction.response.send_message(embed=disnake.Embed(
            description=f"Ой. Похоже, что-то пошло не так. Вы уверены, что правильно ввели команду?"
        ))
    print()
    print(f'/// {error} ///')
    print()


path_cogs = Path("cogs")
for file in os.listdir(path_cogs):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)
