import discord
import asyncio
from discord.ext import commands

#TOKENをbotのトークンに差し替えること
token = "TOKEN"

bot = commands.Bot(command_prefix='!')

#音源ファイルのパス
music_dir = "music/"

#使用方法の記述
usage = (
    "!o：正解音を鳴らす",
    "!x：不正解音を鳴らす",
    "!ov：正解音を鳴らす(声ver)",
    "!xv：不正解音を鳴らす(声ver)",
    "!e-：驚きの声",
    "!cheer：拍手",
    "!wara：大勢の笑い声",
    "!bye：終了"
)

print("ログインしました")

#Botをボイスチャンネルに入室させる
@bot.command(aliases=["connect","join"])
async def start(ctx):
    #コマンド入力者のボイスチャンネル状態を確認
    voice_state = ctx.author.voice
    if (not voice_state) or (not voice_state.channel):
        await ctx.send("後で行くから先にボイスチャンネルに入ってて！")
        return
    channel = voice_state.channel
    #使用方法の説明
    usage_message = "===使い方===\n"
    for usg in usage:
        usage_message += usg + '\n'
    usage_message += "============\n"
    await ctx.send(usage_message)
    #ボイスチャンネルに接続
    await channel.connect()
    await ctx.send("起動しました！")
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"kidoushimashita.mp3")
    voice_client.play(ffmpeg_audio_source)
    print("connected to:",channel.name)

#Botをボイスチャンネルから切断する
@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("私は会話に参加していません（寂しい...）")
        return
    #終了のあいさつ
    await ctx.send("またのご利用お待ちしています！")
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"matanogoriyouwo.mp3")
    voice_client.play(ffmpeg_audio_source)
    await asyncio.sleep(3) #再生し終わってから次の処理に移る
    #切断
    await voice_client.disconnect()

#正解音を鳴らす
@bot.command(name='o')
async def correct(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("判定結果は音でお届けしたい...(\"!join\"を入力してね)")
        return

    await ctx.send(":o:")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"correct.mp3")
    voice_client.play(ffmpeg_audio_source)

#不正解音を鳴らす
@bot.command(name='x')
async def wrong(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("判定結果は音でお届けしたい...(\"!join\"を入力してね)")
        return

    await ctx.send(":x:")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"wrong.mp3")
    voice_client.play(ffmpeg_audio_source)

#正解音を鳴らす(声ver)
@bot.command(name='ov')
async def correct_voice(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("判定結果は声でお届けしたい...(\"!join\"を入力してね)")
        return

    await ctx.send("ピンポンピンポン！")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"correct_voice.mp3")
    voice_client.play(ffmpeg_audio_source)

#不正解音を鳴らす(声ver)
@bot.command(name='xv')
async def wrong_voice(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("判定結果は声でお届けしたい...(\"!join\"を入力してね)")
        return

    await ctx.send("ブッブー！")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"wrong_voice.mp3")
    voice_client.play(ffmpeg_audio_source)

#驚きの声を出す
@bot.command(name='e-')
async def bikkuri(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("私は会話に参加していません...(\"!join\"を入力してね)")
        return

    await ctx.send(":open_mouth: :open_mouth: :open_mouth:")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"e-.mp3")
    voice_client.play(ffmpeg_audio_source)

#拍手する
@bot.command(name='cheer')
async def cheer(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("私は会話に参加していません...(\"!join\"を入力してね)")
        return

    await ctx.send(":clap: :clap: :clap:")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"cheer.mp3")
    voice_client.play(ffmpeg_audio_source)

#笑い声を流す
@bot.command(name='wara')
async def laugh(ctx):
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("私は会話に参加していません...(\"!join\"を入力してね)")
        return

    await ctx.send(":rofl: :rofl: :rofl:")
    ffmpeg_audio_source = discord.FFmpegPCMAudio(music_dir+"laugh.mp3")
    voice_client.play(ffmpeg_audio_source)

#bot起動
bot.run(token)