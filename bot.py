import disnake
from disnake.ext import commands

import pathlib
from pathlib import Path

import os
from dotenv import load_dotenv

dir_path = pathlib.Path.cwd()

path = Path('bot_token', 'bot_token.env')

load_dotenv(dotenv_path=path)


intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="!@#$%", help_command=None, intents=intents)


@bot.event  # Проверка на готовность бота
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event  # Сообщение "новый участник"
async def on_member_join(member):
    channel = bot.get_channel(1141356092358656122)

    embed = disnake.Embed(
        title=f"{member} joined the server!",
        description=f"Welcome! Please read <#1140367048841625771> channel.",
        color=0x00ff00
    )

    await channel.send(embed=embed)


@bot.event  # Сообщение "участник вышел"
async def on_member_remove(member):
    channel = bot.get_channel(1141356092358656122)

    embed = disnake.Embed(
        title=f"{member} left the server...",
        description="We will miss you.",
        color=0xff0000
    )

    await channel.send(embed=embed)


@bot.event  # Сообщение об ошибке
async def on_command_error(interaction, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(f"{interaction.author}, you don't have enough rights to use this command.")
    elif isinstance(error, commands.UserInputError):
        await interaction.response.send_message(embed=disnake.Embed(
            description=f"Oops. It seems something went wrong. Are you sure you entered the command correctly?"
        ))


path = Path("cogs")  # Путь использования когов
for file in os.listdir(path):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)  # Запуск бота по токену
