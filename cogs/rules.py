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
        embed.add_field(name='', value='```• Оскорбления/унижение/угрозы в адрес участников\n# мьют на 4 часа```', inline=False)
        embed.add_field(name='', value='```• Неадекватное/токсичное поведение\n# мьют на 1 день```', inline=False)
        embed.add_field(name='', value='```• Разведение/поддержка конфликтных ситуаций\n# мьют на 7 дней```', inline=False)
        embed.add_field(name='', value='```• Провокация участников на совершение нарушений\n# бан```', inline=False)
        embed.add_field(name='', value='```• Слив личных данных участников\n# бан```', inline=False)
        embed.add_field(name='', value='```• Оскорбление родственников участников\nмьют на 7 дней```', inline=False)
        embed.add_field(name='', value='```• Обсуждение и публикация политических и военных тем, а также провокационные высказывания своих взглядов на эти темы и т.д.\n# бан```', inline=False)
        embed.add_field(name='', value='```• Откровенная травля, клевета, распускание ложных слухов об участниках сервера\n# бан```', inline=False)
        embed.add_field(name='', value='```• Разногласия на тему расы, национальности и т.д.\n# мьют на 30 дней```', inline=False)
        embed.add_field(name='', value='```• Злоупотребление правами специальных ролей, если таковые имеются\n# удаление роли у участника```', inline=False)
        embed.add_field(name='', value='```• Оскорбление создателя сервера/модератора (исключение: Создатель, модератор расценил ваше сообщение как шутку)\n# бан```', inline=False)
        embed.add_field(name='', value='```• Шумы/посторонние звуки, мешающие участникам голосового чата\n# мьют до исправления```', inline=False)
        embed.add_field(name='', value='```• Использование звука. устройства без разрешения участников голосового канала\n# мьют на 4 часа```', inline=False)
        
        embed2 = disnake.Embed(color=0xff0000, title='')
        embed2.add_field(name='', value='# Чат и общение', inline=False)
        embed2.add_field(name='', value='```• Использование каналов для других целей\n# мьют на 1 час```', inline=False)
        embed2.add_field(name='', value='```• Рассылка спама\n# мьют на 4 часа```', inline=False)
        embed2.add_field(name='', value='```• Флуд\n# мьют на 3 часа```', inline=False)
        embed2.add_field(name='', value='```• Капс\n# мьют на 3 часа```', inline=False)
        embed2.add_field(name='', value='```• Публикация и демонстрация любого вида контента NSFW\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Публикация и демонстрация любого вида контента NSFL\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Нацизм, фашизм и т.д.\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Реклама\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Публикация вредоносных материалов\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Публикация видео и ссылок, содержащих скримеры\n# мьют на 30 дней```', inline=False)
        embed2.add_field(name='', value='```• Публикация/демонстрация экстремистского контента на сервере\n# бан```', inline=False)
        embed2.add_field(name='', value='```• Множественные упоминания участников сервера\n# мьют на 1 день```', inline=False)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed_title)
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed_update_time)


def setup(bot):
    bot.add_cog(Rules(bot))
