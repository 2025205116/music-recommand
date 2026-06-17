from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Music Recommendation API")

class MusicQuery(BaseModel):
    focus: str       # 가사 vs 멜로디
    mood: str        # 화려함 vs 수수함
    vocal: str       # 여성보컬 vs 남성보컬
    sound: str       # 베이스 vs 고음
    nation: str      # jpop vs kpop vs pop
    tempo: str       # 나른함 vs 신남 (느림 vs 빠름)

MUSIC_DATABASE = [
    {
        "title": "Waving Through a Window",
        "artist": "Dear Evan Hansen OST",
        "youtube_url": "https://youtu.be/kfnMvo87fQU?si=8f_ImYchvKYu86wk",               
        "youtube_kr_url": "https://youtu.be/go3MQCP6UdU?si=3dfecaw9MfqiwPLG",            
        "tags": {"focus": "가사", "mood": "화려함", "vocal": "남성보컬", "sound": "고음", "nation": "kpop", "tempo": "신남"}
    },
    {
        "title": "Love Bombs",
        "artist": "Diana Deeb",
        "youtube_url": "https://youtu.be/NbkyfMNk31M?si=7Ze-uW2tZUHPckfP",
        "youtube_kr_url": None, 
        "tags": {"focus": "멜로디", "mood": "화려함", "vocal": "여성보컬", "sound": "베이스", "nation": "pop", "tempo": "신남"}
    },
    {
        "title": "HYDE",
        "artist": "Sion",
        "youtube_url": "https://youtu.be/sE11fWOE-0E",
        "youtube_kr_url": None,
        "tags": {"focus": "멜로디", "mood": "수수함", "vocal": "남성보컬", "sound": "베이스", "nation": "pop", "tempo": "나른함"}
    },
    {
        "title": "3am",
        "artist": "Halsey",
        "youtube_url": "https://youtu.be/ab_Bbg4LLOc",
        "youtube_kr_url": None,
        "tags": {"focus": "멜로디", "mood": "화려함", "vocal": "여성보컬", "sound": "베이스", "nation": "pop", "tempo": "신남"}
    },
        {
        "title": "Dear God",
        "artist": "confetti",
        "youtube_url": "https://youtu.be/N1sLNQwCrMo?si=QyamaIpOvS0jbIx5",              
        "youtube_kr_url": None,            
        "tags": {"focus": "가사", "mood": "수수함", "vocal": "남성보컬", "sound": "베이스", "nation": "pop", "tempo": "신남"}
    },
    {
        "title": "밤산책 (Night Walk)",
        "artist": "SHAUN (숀)",
        "youtube_url": "https://youtu.be/St8bnQbnwTg?si=AjbjjCLEATGxpQRa",
        "youtube_kr_url": None, 
        "tags": {"focus": "가사", "mood": "수수함", "vocal": "남성보컬", "sound": "베이스", "nation": "kpop", "tempo": "나른함"}
    },
     {
        "title": "거울(MIRROR)",
        "artist": "한로로",
        "youtube_url": "https://youtu.be/_TnsZ71zaxU?si=B0sFsv149WA5D5tT",
        "youtube_kr_url": None, 
        "tags": {"focus": "가사", "mood": "수수함", "vocal": "여성보컬", "sound": "고음", "nation": "kpop", "tempo": "나른함"}
    },
     {
        "title": "romeo n juliet (feat. youra)",
        "artist": "죠지",
        "youtube_url": "https://youtu.be/rHLGjbz-yls?si=pTJH_pP6CWLFGUwN",
        "youtube_kr_url": None, 
        "tags": {"focus": "멜로디", "mood": "수수함", "vocal": "남성보컬", "sound": "베이스", "nation": "kpop", "tempo": "나른함"}
    },
     {
        "title": "시 쓰기와 커피(詩書きとコーヒー)",
        "artist": "요루시카(ヨルシカ)",
        "youtube_url": "https://youtu.be/TQv9pgD9pXQ?si=XsfJ9kGyXB8wyP_W",
        "youtube_kr_url": None, 
        "tags": {"focus": "가사", "mood": "화려함", "vocal": "여성보컬", "sound": "베이스", "nation": "jpop", "tempo": "신남"}
    },
     {
        "title": "귀신의 잔치 (鬼ノ宴)",
        "artist": "토모나리 소라(友成空)",
        "youtube_url": "https://youtu.be/_Yh8MRwfwck?si=EyOTAOHtbxFr_ETl",
        "youtube_kr_url": None, 
        "tags": {"focus": "멜로디", "mood": "화려함", "vocal": "남성보컬", "sound": "베이스", "nation": "jpop", "tempo": "신남"}
    },
     {
        "title": "ACTOR",
        "artist": "토모나리 소라(友成空)",
        "youtube_url": "https://youtu.be/aHDrVWJrgGU?si=bFai_AsLDPGfdA1P",
        "youtube_kr_url": None, 
        "tags": {"focus": "가사", "mood": "수수함", "vocal": "남성보컬", "sound": "베이스", "nation": "jpop", "tempo": "나른함"}
    },
     {
        "title": "눈싸움 (睨めっ娘 - Niramekko)",
        "artist": "토모나리 소라(友成空)",
        "youtube_url": "https://youtu.be/GTT77PuKxq0?si=RM_oFUgTWgrwXTfO",
        "youtube_kr_url": None, 
        "tags": {"focus": "멜로디", "mood": "화려함", "vocal": "남성보컬", "sound": "베이스", "nation": "jpop", "tempo": "신남"}
    },
     {
        "title": "타임캡슐",
        "artist": "다비치",
        "youtube_url": "https://youtu.be/0Pey6Y-xogE?si=DG5I9AB6wVX4bfkj",
        "youtube_kr_url": None,
        "tags": {"focus": "멜로디", "mood": "화려함", "vocal": "여성보컬", "sound": "고음", "nation": "kpop", "tempo": "신남"}
    },
     {
      "title": "폭탄마 (爆弾魔)",
        "artist": "요루시카(ヨルシカ)",
        "youtube_url": "https://youtu.be/tHfgoDgTxR4?si=iLLc5GallkikirXY",
        "youtube_kr_url": None,
        "tags": {"focus": "가사", "mood": "화려함", "vocal": "여성보컬", "sound": "고음", "nation": "jpop", "tempo": "신남"}
    },
    {
      "title": "Play Sick",
        "artist": "요루시카(ヨルシカ)",
        "youtube_url": "https://youtu.be/RM5D8ogCKE0?si=8Om2nH9ewVNoMt-O",
        "youtube_kr_url": None,
        "tags": {"focus": "가사", "mood": "수수함", "vocal": "여성보컬", "sound": "베이스", "nation": "jpop", "tempo": "나른함"}
    }
    
    
]

@app.post("/recommend")
def recommend_music(query: MusicQuery):
    user_preferences = {
        "focus": query.focus,
        "mood": query.mood,
        "vocal": query.vocal,
        "sound": query.sound,
        "nation": query.nation,
        "tempo": query.tempo
    }
    
    scored_songs = []
    
    for song in MUSIC_DATABASE:
        match_count = 0
        for key, value in user_preferences.items():
            if song["tags"].get(key) == value:
                match_count += 1
        
        scored_songs.append({
            "title": song["title"],
            "artist": song["artist"],
            "youtube_url": song.get("youtube_url"),
            "youtube_kr_url": song.get("youtube_kr_url"), 
            "match_score": match_count,
            "matched_percentage": int((match_count / 6) * 100)
        })
    
    scored_songs.sort(key=lambda x: x["match_score"], reverse=True)
    
    if len(scored_songs) >= 2:
        final_recommendations = scored_songs[:2]
    elif len(scored_songs) == 1:
        final_recommendations = scored_songs
    else:
        final_recommendations = [{
            "title": "등록된 곡이 없습니다.",
            "artist": "데이터를 채워주세요",
            "youtube_url": None,
            "youtube_kr_url": None,
            "match_score": 0,
            "matched_percentage": 0
        }]
        
    return {
        "status": "success",
        "recommendations": final_recommendations
    }
