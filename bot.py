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

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")


@bot.event  # Сообщение "новый участник"
async def on_member_join(member):
    channel = bot.get_channel(1141436357516992563)

    embed = disnake.Embed(
        title=f"{member} присоединился к серверу!",
        description=f"Добро пожаловать! Пожалуйста ознакомься с каналом <#1051486016634105866>.",
        color=0x00ff00
    )

    await channel.send(embed=embed)


@bot.event  # Сообщение "участник вышел"
async def on_member_remove(member):
    channel = bot.get_channel(1141436357516992563)

    embed = disnake.Embed(
        title=f"{member} покинул сервер...",
        description="Мы будем ждать тебя снова.",
        color=0xff0000
    )

    await channel.send(embed=embed)


@bot.event
async def on_command_error(error):
    print(f'--- {error} ---')


@bot.event
async def on_slash_command_error(interaction, error):
    print(f'/// {error} ///')

    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message(f"{interaction.author}, у вас недостаточно прав для использования этой команды.")
    elif isinstance(error, commands.UserInputError):
        await interaction.response.send_message(embed=disnake.Embed(
            description=f"Ой. Похоже, что-то пошло не так. Вы уверены, что правильно ввели команду?"
        ))


path = Path("cogs")
for file in os.listdir(path):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)
