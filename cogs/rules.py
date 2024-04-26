import datetime

import disnake
from disnake.ext import commands


class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):

        time = datetime.datetime.now() + datetime.timedelta(minutes=int(0))
        cool_time = disnake.utils.format_dt(time, style="R")

        embed_title = disnake.Embed(color=0xff0000, title='Правила сервера:')

        embed_update_time = disnake.Embed(color=0xff0000, title=f'Последнее обновление правил было: {cool_time}')

        embed = disnake.Embed(color=0xff0000, title='')
        embed.add_field(name='', value='# Конфликты')
        embed.add_field(name='', value='```• Оскорбления/унижение/угрозы в адрес участников\n# мьют на 1-4 часа```', inline=False)
        embed.add_field(name='', value='```• Неадекватное/токсичное поведение\n# мьют на 4-12 часов```', inline=False)
        embed.add_field(name='', value='```• Разведение/поддержка конфликтных ситуаций\n# мьют на 3-7 дней```', inline=False)
        embed.add_field(name='', value='```• Провокация участников на совершение нарушений\n# мьют на 7 дней```', inline=False)
        embed.add_field(name='', value='```• Слив личных данных участников\n# бан```', inline=False)
        embed.add_field(name='', value='```• Обсуждение и публикация политических и военных тем, а также провокационные высказывания своих взглядов на эти темы и т.д.\n# мьют 3-7 дней```', inline=False)
        embed.add_field(name='', value='```• Откровенная травля, клевета, распускание ложных слухов об участниках сервера\n# бан```', inline=False)
        embed.add_field(name='', value='```• Разногласия на тему расы, национальности и т.д.\n# мьют на 30 дней```', inline=False)
        embed.add_field(name='', value='```• Злоупотребление правами особых ролей\n# лишение роли перманентно```', inline=False)
        embed.add_field(name='', value='```• Шумы/посторонние звуки, мешающие участникам голосового чата\n# мьют микрофона до исправления```', inline=False)
        embed.add_field(name='', value='```• Использование звуковых устройства без разрешения участников голосового канала(Soundpad и тд.)\n# мьют на 4 часа```', inline=False)
        
        embed2 = disnake.Embed(color=0xff0000, title='')
        embed2.add_field(name='', value='# Чат и общение', inline=False)
        embed2.add_field(name='', value='```• Использование каналов не по назначению\n# мьют на 30 минут```', inline=False)
        embed2.add_field(name='', value='```• Спам, флуд, капс\n# мьют на 1 час```', inline=False)
        embed2.add_field(name='', value='```• Публикация и демонстрация любого вида контента NSFW в не предназначенных для этого каналах\n# мьют на 4 дня```', inline=False)
        embed2.add_field(name='', value='```• Публикация и демонстрация любого вида контента NSFL\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Нацизм, фашизм и т.д.\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Реклама\n# мьют на 7 дней - бан```', inline=False)
        embed2.add_field(name='', value='```• Публикация вредоносных материалов\n# мьют на 30 дней```', inline=False)
        embed2.add_field(name='', value='```• Публикация видео и ссылок, содержащих скримеры\n# мьют на 3 дня```', inline=False)
        embed2.add_field(name='', value='```• Публикация/демонстрация экстремистского контента на сервере\n# бан```', inline=False)

        await ctx.send(embeds=[embed_title, embed, embed2, embed_update_time])


def setup(bot):
    bot.add_cog(Rules(bot))
