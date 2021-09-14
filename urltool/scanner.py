import json
import urllib
from urllib.request import urlopen

class Scanner:

 def __init__(self, link):
     self.link = link

 def Scan(self):
     with urlopen(f"https://api.lrl.kr/v2/check/?url={self.link}&format=json") as url:
      data = url.read()
     load_data = json.loads(data.decode('utf-8'))
     result = load_data.get("safe")
     return f"{safe}"
