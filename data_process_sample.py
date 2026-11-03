import json

def get_default_match_data(match,timeline,challengers):
    data = {}

    data["matchId"] = match["metadata"]["matchId"]
    data["gameDurationSec"] = match["info"]["gameDuration"]
    data["numFrames"] = len(timeline["info"]["frames"])
    tmp_teamId = match["info"]["participants"][0]["teamId"]
    tmp_win    = match["info"]["participants"][0]["win"]
    data["blueWin"] = tmp_win if tmp_teamId == 100 else (not tmp_win)

    # 데이터 툴 초기화
    lanes = ["TOP","MIDDLE","JUNGLE","BOTTOM"]
    for lane in lanes:
        data[lane] = {"blue":{"feature" : {}}, "red":{"feature" : {}}}
    data["BOTTOM"]["blue"]["participantID"] = {}
    data["BOTTOM"]["red"]["participantID"] = {}
    data["BOTTOM"]["blue"]["challengerPuuID"] = {}
    data["BOTTOM"]["red"]["challengerPuuID"] = {}

    # lane별로 feature를 제외한 기본정보를 입력해준다.
    # 기본정보는 participantId, challengerPUUID, teamID(Blue / Red)
    # lane을 구분하기 위해서 match["info"]["participants"]를 참조해보면
    # lane, indivisualPosition, teamPosition, role 등이 있는데
    # 서로 구분되는 역할을 명시한 키 값은 teamPositon이다.
    for p in match["info"]["participants"]:
        team = p["teamId"]
        side = "blue" if team == 100 else "red"
        pos = p["teamPosition"]
        pid = p["participantId"]
        puid = p["puuid"]
        is_chall = puid in challengers
        chall = puid if is_chall else None

        if pos == "TOP":
            data["TOP"][side]["teamId"] = team
            data["TOP"][side]["participantId"] = pid
            data["TOP"][side]["challengerPuuID"] = chall
        elif pos == "MIDDLE":
            data["MIDDLE"][side]["teamId"] = team
            data["MIDDLE"][side]["participantId"] = pid
            data["MIDDLE"][side]["challengerPuuID"] = chall
        elif pos == "JUNGLE":
            data["JUNGLE"][side]["teamId"] = team
            data["JUNGLE"][side]["participantId"] = pid
            data["JUNGLE"][side]["challengerPuuID"] = chall
        elif pos == "BOTTOM":
            data["BOTTOM"][side]["teamId"] = team
            data["BOTTOM"][side]["participantId"] = pid
            data["BOTTOM"][side]["challengerPuuID"] = chall
        elif pos == "UTILITY":
            data["BOTTOM"][side]["teamId"] = team
            data["BOTTOM"][side]["participantId"] = pid
            data["BOTTOM"][side]["challengerPuuID"] = chall
        else:
            print(f"Something error: {pos}")
            pass
    return data

def get_top_features(match, timeline, data):
    pass

def main():
    with open("match_0.json", "r" , encoding="utf-8") as f:
        match = json.load(f)
    with open("timeline_0.json", "r" , encoding="utf-8") as f:
        timeline = json.load(f)
    with open("puuid_challengers.txt", "r" , encoding="utf-8") as f:
        challengers = f.read().splitlines()


    #for m, tl in zip(match,timeline):
    m=match[0]
    tl = timeline[0]
    data = get_default_match_data(m,tl,challengers)
    print(json.dumps(data, indent=2, ensure_ascii=False))
    Top_blue, Top_red = (get_top_features
                         (m,tl,data))

if __name__=="__main__":
    main()