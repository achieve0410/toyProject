import json
import requests

api_key = "RGAPI-02988fc3-11dc-40d0-aa61-3a27504fc1a0"

print("1: 플레이어 검색")
selectnum = input("번호를 입력해주세요: ")

if selectnum == "1":
    name = input("소환사의 닉네임을 입력해주세요: ")
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        #코드가 200일때
        print(res.text)
        resobj = json.loads(res.text)

        # ## 숙련도 관련        
        # URL = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+resobj["id"]
        # res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # rankinfo = json.loads(res.text)
        # print("소환사 이름: "+name)
        # for i in rankinfo:
        #     print(i)

        # ## 유저 게임 기록 관련        
        # URL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/"+resobj["accountId"]
        # res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # rankinfo = json.loads(res.text)
        # print("소환사 이름: "+name)
        # for i in rankinfo:
        #     print(i)
        #     if i=='matches':
        #         for match in rankinfo[i]:
        #             print(match)

        # ## 특정 게임 관련        
        # URL = "https://kr.api.riotgames.com/lol/match/v4/matches/5276697339"
        # res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # rankinfo = json.loads(res.text)
        # # print(rankinfo)
        # print("소환사 이름: "+name)
        # for i in rankinfo:
        #     print(i, ":", rankinfo[i])


        # ## 랭크 게임 전적 관련        
        # URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]
        # res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # print(res.text)
        # rankinfo = json.loads(res.text)
        # print(rankinfo)
        # # print(rankinfo)
        # print("소환사 이름: "+name)
        # for i in rankinfo:
        #     print(i, ":", rankinfo[i])

        
        ## 챔피언 관련        
        # URL = "https://kr.api.riotgames.com/lol/platform/v3/champion-rotations"
        # res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # print(res.text)
        # rankinfo = json.loads(res.text)
        # print(rankinfo)
        # # print(rankinfo)
        # print("소환사 이름: "+name)
        # for i in rankinfo:
        #     print(i, ":", rankinfo[i])



        ## 인게임 관련
        # URL = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+resobj["id"]
        URL = "https://kr.api.riotgames.com/lol/spectator/v4/featured-games"
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        # print(res.text)
        rankinfo = json.loads(res.text)
        # print(rankinfo)
        print("소환사 이름: "+name)
        for i in rankinfo:
            if i=='gameList':
                for j in rankinfo['gameList']:
                    for k in j['participants']:
                        print(k['summonerName'])
            else:
                print(i, ":", rankinfo[i])



    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")