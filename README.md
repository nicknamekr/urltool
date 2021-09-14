Notice : You have to download 1.1.0a0 verson.
=> https://pypi.org/project/urltool/1.1.0a0/
# urltool
A simple url shortener that made with python.
## Developer
Seeun (* Nickname)
## Example
### Url shortener
#### Introduce
urltool/shortener is a simple url shortener that powered by lrl.kr api.
#### Simple Code
```py
from urltool import shortener

data = shortener.Generator('https://example.com') # Edit example.com to real url.
result = data.Generate()

print(f'URL: {result}')
```
#### Discord Bot
```py
from urltool import shortener
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Login as {bot.user.name}')

@bot.command()
async def 단축(ctx, *, link):
    """
    !단축 <URL>
    """
    data = shortener.Generator(link)
    result = data.Generate()
    await ctx.send(f'URL: {result}')

bot.run('token')
```
### Url Safe Scanner
#### Introduce
urltool/scanner is a simple url safe-scanner that powered by lrl.kr api.
#### Simple
Soontm
#### Discord Bot
Soontm
## Support
Please send DM to Nickname#1234 or send message in https://discord.gg/VdxBGuJpjk (Seeun Lab).
