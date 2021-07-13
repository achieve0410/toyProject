from . import myapikeys
from . import matchId
from . import encryptId
# import myapikeys
# import matchId
# import encryptId
import requests

def WinorLose(DEVELOPMENTAPIKEY,summonerName, gameId):
    encryptedId, accountId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    # gameId = matchId.getMatchId(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(gameId)
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    participantId = 0
    for i in range(0,10):
        if accountId == data["participantIdentities"][i]["player"]["accountId"]:
            participantId = i
    if(data["teams"][0]["win"]=="Win"):
        if(participantId > 5):
            # print(gameId, 0)
            return 0
        else:
            # print(gameId, 1)
            return 1
    else:
        if(participantId > 5):
            # print(gameId, 1)
            return 1
        else:
            # print(gameId, 0)
            return 0

# DEVELOPMENTAPIKEY = myapikeys.myapikey()
# summonerName = "HIDE ON BUSH"
# print(WinorLose(DEVELOPMENTAPIKEY,summonerName, gameId)) ## win:1 lose:0