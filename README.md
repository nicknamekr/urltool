# urltool
A simple url shortener that made with python.
## Install
### PyPi
```cs
pip install urltool
```
### Git
```
pip install git + https://github.com/seeundev/urltool
```
## Example
### Url shortener
#### Introduce
urltool/shortener is a simple url shortener that powered by lrl.kr api.<br>
It must contain https:// or http://.
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
urltool/scanner is a simple url safe-scanner that powered by lrl.kr api.<br>
It must contain https:// or http://.
#### Simple Code
```py
from urltool import scanner

data = scanner.Scanner('https://example.com') # Edit example.com to real url.
result = data.Scan()

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
async def 검사(ctx, *, link):
    """
    !검사 <URL>
    """
    data = scanner.Scanner(link)
    result = data.Scan()
    await ctx.send(f'Safe: {result}')

bot.run('token')
```
## Support
Please send DM to Nickname#1234 or send message in https://discord.gg/VdxBGuJpjk (Seeun Lab).
## Developers
Nickname#1234
