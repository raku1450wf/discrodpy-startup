# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODQzMzQ1Mjk1MzUzMDUzMTg1.YKCggw.8wzkVY9QHIvdZhm8LZOVQf7CMVg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(client.user.name)  # Botの名前
    print(client.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
#BOTのプレイ表記
    await client.change_presence(activity=discord.Game(name="開発中(らく)"))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

#コマンド受信時に動作する処理
    #コマンド「/link m」と入力したらミルダムリンクが返る処理
    if message.content == '/link m':
        await message.channel.send('https://www.mildom.com/profile/11053439')
    #コマンド「/link y」と入力したらYoutubeリンクが返る処理
    if message.content == '/link y':
        await message.channel.send('https://www.youtube.com/channel/UCKOtOcXnTyaglPDo1_9OaGg')
    #コマンド「/link t」と入力したらツイッターリンクが返る処理
    if message.content == '/link t':
        await message.channel.send('https://twitter.com/mukimukidamasii')

#管理者専用コマンド受信時に動作する処理
    #コマンド「/live 9」と入力したら配信予告が返る処理(9時から配信)
    if message.content == '/live 9':
        await message.channel.send('@everyone 21時から配信です！ https://www.mildom.com/profile/11053439')
    #コマンド「/live ?」と入力したら不定期配信予告が返る処理(何かしらアクシデントがあった場合)
    if message.content == '/live ?':
        await message.channel.send('@everyone もうすぐで配信です！ https://www.mildom.com/profile/11053439')

client.run(TOKEN)
