import streamlit as st
import requests

st.set_page_config(page_title="취향 저격 음악 레이더",  layout="centered")

st.title("내 취향 음악 추천(작성자의 개인취향 기반)")
st.write("6가지 질문에 답하시면 가장 높은 일치율을 가진 음악 **2가지** 를 추천해 드립니다.")

st.markdown("---")

focus = st.radio("질문 1. 음악을 들을 때 더 중요하게 생각하는 요소는?", ["가사", "멜로디"], horizontal=True)
mood = st.radio("질문 2. 선호하는 곡의 분위기는?", ["화려함", "수수함"], horizontal=True)
vocal = st.radio("질문 3. 어떤 보컬의 음색을 더 선호하시나요?", ["여성보컬", "남성보컬"], horizontal=True)
sound = st.radio("질문 4. 음악에서 더 강조되었으면 하는 사운드는?", ["베이스", "고음"], horizontal=True)
nation = st.selectbox("질문 5. 선호하는 음악의 국가/장르는?", ["kpop", "jpop", "pop"])
tempo = st.radio("질문 6. 현재 선호하는 곡의 전반적인 분위기는?", ["나른함", "신남"], horizontal=True)

st.markdown("---")

if st.button("🎵 내 취향 분석 및 2곡 추천받기", use_container_width=True):

    BACKEND_URL = "http://34.204.68.3:8000/recommend"
    
    payload = {
        "focus": focus,
        "mood": mood,
        "vocal": vocal,
        "sound": sound,
        "nation": nation,
        "tempo": tempo
    }
    
    with st.spinner("당신의 답변을 분석하여 데이터베이스에서 매칭 중입니다..."):
        try:
            response = requests.post(BACKEND_URL, json=payload, timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                recommendations = result["recommendations"]
                
                st.success("🎯 당신의 취향과 가장 잘 맞는 음악 2가지를 찾았습니다!")
                st.write("")
                
                for idx, song in enumerate(recommendations, 1):
                    with st.container():
                        st.subheader(f"위 {idx}. **{song['title']}** - {song['artist']}")
                        st.progress(song['match_score'] / 6)
                        st.caption(f"취향 일치도: **{song['matched_percentage']}%** ({song['match_score']}/6 개 항목 일치)")
                        
                        if song.get("youtube_url") and song.get("youtube_kr_url"):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.link_button("🇺🇸 원곡 (Original) 감상하기", song["youtube_url"], use_container_width=True)
                            with col2:
                                st.link_button("🇰🇷 한국어 번안곡 감상하기", song["youtube_kr_url"], use_container_width=True)
                        elif song.get("youtube_url"):
                            st.link_button("📺 유튜브에서 음악 감상하기", song["youtube_url"], use_container_width=True)
                            
                        st.markdown("---")
            else:
                st.error("백엔드 서버 응답 오류가 발생했습니다.")
                
        except requests.exceptions.ConnectionError:
            st.error("백엔드 서버에 연결할 수 없습니다. 포트 설정이나 EC2 인바운드 규칙을 확인하세요.")