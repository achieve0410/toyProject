from . import myapikeys
from . import encryptId
# import myapikeys
# import encryptId
import requests

def getMatchId(DEVELOPMENTAPIKEY,summonerName):
    encryptedId, encryptedAccountId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedAccountId
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data["matches"][0]["gameId"]

# DEVELOPMENTAPIKEY = myapikeys.myapikey()
# summonerName = "Hide on bush"

# print(getMatchId(DEVELOPMENTAPIKEY,summonerName))