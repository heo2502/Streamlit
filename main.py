import random

import streamlit as st
import pandas as pd
import datetime
import os
 
st.set_page_config(
    page_title="7월 특강 5일 실습 모음",
    page_icon="📅",
    layout="wide",
)
 
# -----------------------------------------------------------------------
# 강의 일정 정의 (날짜, 제목, 한줄 설명) -> 여기에 내용만 계속 채워나가면 됩니다.
# -----------------------------------------------------------------------
SCHEDULE = [
    {"day": 1, "date": "7월 6일 (월)", "title": "위젯만들기",
     "desc": "Day 1 실습 내용이 곧 업데이트됩니다."},
    {"day": 2, "date": "7월 7일 (화)", "title": "음성입출력",
     "desc": "Day 2 실습 내용이 곧 업데이트됩니다."},
    {"day": 3, "date": "7월 8일 (수)", "title": "준비중",
     "desc": "Day 3 실습 내용이 곧 업데이트됩니다."},
    {"day": 4, "date": "7월 9일 (목)", "title": "준비중",
     "desc": "Day 4 실습 내용이 곧 업데이트됩니다."},
    {"day": 5, "date": "7월 10일 (금)", "title": "준비중",
     "desc": "Day 5 실습 내용이 곧 업데이트됩니다."},
]
 
SURVEY_FILE = "survey_results.csv"
 
 
# =========================================================================
# 공통 유틸: 아직 준비되지 않은 날짜용 안내 화면
# =========================================================================
def coming_soon(day_info):
    st.title(f"📅 Day {day_info['day']} · {day_info['date']}")
    st.info(f"🚧 {day_info['desc']}\n\n이 자리에는 해당 날짜의 실습용 앱이 채워질 예정입니다.")
    st.caption("교수자 Tip: 이 함수(day{}_app) 내부에 그날의 실습 코드를 채워 넣으면 됩니다.".format(day_info["day"]))
 
 
# =========================================================================
# Day 1 (7/6) : 위젯만들기
# =========================================================================
def day1_app():
    st.title("나의 첫 번째 웹앱")
    st.write("VSCode, uv, Streamlit을 이용해서 만든 웹앱입니다.")
    name = st.text_input("이름을 입력하세요", key="name1")

    if name:
        st.success(f"{name}님, 반갑습니다!")

    age1 = st.slider("나이를 선택하세요", 0, 100, 0, key='age1')
    st.write(f"선택한 나이는 {age1}세입니다.")

    st.header("관심 분야 선택")
    interest = st.selectbox(
        "관심 있는 분야를 선택하세요",
        ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]
    )
    st.write(f"선택한 관심 분야는 {interest}입니다.")

    st.write("---")
    st.title('자기소개')
    st.header('기본 정보')
    st.subheader('취미')
    st.write('저는 축구를 좋아합니다.')
    
    st.write("---")
    if st.button('인사하기'):
        st.write('안녕하세요!')

    st.write("---")
    st.success('성공했습니다!')
    st.info('안내 메시지입니다.')
    st.warning('주의하세요!')
    st.error('오류가 발생했습니다.')
    
    st.write("---")
    import random
    luck=['대박','행운','평범','조심','최고']
    if st.button('운세 보기'):
        st.write(random.choice(luck))

    st.write("---")
    st.image('images/그림1.png')
    st.video('https://www.youtube.com/watch?v=xxxx')

    st.write("---")
    name2 = st.text_input('이름을 입력하세요', key='name2')
    if name2:
        st.write(f'{name2}님, 환영합니다!')

    age2 = st.number_input('나이', min_value=0, max_value=100, key='age2')
    st.write('내년 나이:', age2+1)

    st.write("---")
    score = st.slider('집중도', 0, 100, 50)
    st.write('현재 집중도:', score)

    st.write("---")
    subject = st.selectbox('좋아하는 과목', ['국어','수학','영어','정보'])
    st.write('선택:', subject)

    st.write("---")
    menu = st.radio('점심 메뉴', ['김밥','라면','돈가스'])
    st.write(menu, '선택!')

    st.write("---")
    if st.checkbox('축구','야구', '배구'):
        st.write('축구를 좋아합니다!')

    items = ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]

    selected_items = []

    for item in items:
        checked = st.checkbox(item)
        if checked:
            selected_items.append(item)

    st.subheader("선택한 항목")

    if selected_items:
        st.write(selected_items)
    else:
        st.write("아직 선택한 항목이 없습니다.")
    
    st.write("---")
    score = st.number_input('점수', 0, 100)
    if score >= 60:
        st.success('합격')
    else:
        st.warning('다시 도전')

    st.write("---")
    name3=st.text_input('이름', key='name3')
    age3=st.number_input('나이',0,100, key='age3')
    field3=st.selectbox('관심분야',['AI','게임','디자인'], key='field3')
    st.write(name3, age3, field3)

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write('왼쪽')
    with col2:
        st.write('오른쪽')

    st.write("---")
    menu = st.sidebar.selectbox('메뉴', ['홈','분석','설정'])
    st.write('선택한 메뉴:', menu)

    st.write("---")
    tab1, tab2 = st.tabs(['소개','실습'])
    with tab1:
        st.write('소개 화면')
    with tab2:
        st.write('실습 화면')

    st.write("---")
    if 'count' not in st.session_state:
        st.session_state.count = 0
        if st.button('증가'):
            st.session_state.count += 1
            st.write(st.session_state.count)

    st.write("---")

    st.write("---")


 
# =========================================================================
# Day 2 (7/7) : 음성입출력
# =========================================================================
def day2_app():
    import streamlit as st
    import re
    from streamlit_mic_recorder import speech_to_text
    from gtts import gTTS
    from io import BytesIO

    def classify_bmi(bmi: float) -> tuple[str, str, str]:
        """대한비만학회(아시아-태평양) 기준 BMI 분류
        반환: (분류명, 이모지, 건강정보 안내문)
        """
        if bmi < 18.5:
            return ("저체중", "🟦",
                    "체중이 표준보다 적은 상태입니다. 단백질과 탄수화물을 골고루 갖춘 "
                    "규칙적인 식사를 하고, 근육량을 늘리는 가벼운 근력 운동을 권장합니다. "
                    "급격한 체중 감소가 있었다면 병원 진료를 받아보세요.")
        elif bmi < 23:
            return ("정상", "🟩",
                    "건강한 체중 범위입니다. 지금의 식습관과 활동량을 잘 유지하세요. "
                    "주 3회 이상, 30분 이상의 유산소 운동을 꾸준히 하면 "
                    "현재의 건강 상태를 오래 지킬 수 있습니다.")
        elif bmi < 25:
            return ("과체중", "🟨",
                    "정상 범위를 조금 넘어선 상태입니다. 야식과 당분 섭취를 줄이고, "
                    "걷기·자전거 같은 유산소 운동을 주 4회 이상 실천해 보세요. "
                    "지금 관리하면 비만으로의 진행을 충분히 막을 수 있습니다.")
        elif bmi < 30:
            return ("비만 1단계", "🟧",
                    "체중 조절이 필요한 단계입니다. 식사량을 조금 줄이고 "
                    "규칙적인 운동을 병행하면 개선할 수 있습니다. 고혈압, 당뇨 등 "
                    "동반 질환 여부를 확인하기 위해 건강검진을 권장합니다.")
        else:
            return ("비만 2단계 이상", "🟥",
                    "적극적인 체중 관리가 필요한 단계입니다. 혼자 하기보다는 "
                    "의사, 영양사 등 전문가와 상담하여 체계적인 계획을 세우는 것이 "
                    "안전하고 효과적입니다. 가까운 병원이나 보건소를 방문해 보세요.")

    def speak(text: str) -> BytesIO:
        """텍스트를 한국어 음성(mp3 바이트)으로 변환"""
        tts = gTTS(text=text, lang="ko")
        buf = BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return buf

    text = "마이크 버튼을 누르고 키와 몸무게를 말하면, BMI와 건강정보를 음성으로 알려드립니다."
    if st.button("🎵 음성 BMI 건강 도우미 클릭"):
        audio = speak(text)
        st.audio(audio, format="audio/mp3", autoplay=True)

    # if st.button("🎵 음성 BMI 건강 도우미"):
    #     tts = gTTS(text=text, lang='ko')     # 한국어 설정
    #     audio_bytes = BytesIO()               # 파일 저장 없이 메모리에서 처리
    #     tts.write_to_fp(audio_bytes)
    #     audio_bytes.seek(0)
    #     st.audio(audio_bytes, format='audio/mp3')   # 재생 플레이어 표시


    st.write("마이크 버튼을 누르고 키를 숫자를 말해보세요. 예: '삼십오' 또는 '35'")

    # 1단계: 음성 → 텍스트 (한국어 설정: language='ko')
    height_text = speech_to_text(
        language='ko',              # 한국어 인식
        start_prompt="🎙️ 녹음 시작",
        stop_prompt="⏹️ 녹음 종료",
        just_once=True,             # 한 번 인식 후 초기화
        use_container_width=True,
        key='stt1'
    )

    # 2단계: 텍스트 → 숫자 추출
    if height_text:
        st.info(f"인식된 말: **{height_text}**")
        numbers = re.findall(r'\d+\.?\d*', height_text)   # 아라비아 숫자 추출
        if numbers:
            height_value = float(numbers[0])
            st.success(f"✅ 입력된 숫자: **{height_value}**")
            st.session_state.height = height_value
            #st.session_state['voice_number'] = height_value
        else:
            st.warning("⚠️ 숫자를 찾지 못했어요. '35'처럼 또박또박 말해보세요.")

    # 3단계: 입력받은 숫자를 위젯에 반영
    # default = st.session_state.get('voice_number', 0.0)
    # num = st.number_input("확인/수정", value=default)

    st.write("마이크 버튼을 누르고 몸무게를 숫자를 말해보세요. 예: '칠십오' 또는 '75'")

    # 1단계: 음성 → 텍스트 (한국어 설정: language='ko')
    weight_text = speech_to_text(
        language='ko',              # 한국어 인식
        start_prompt="🎙️ 녹음 시작",
        stop_prompt="⏹️ 녹음 종료",
        just_once=True,             # 한 번 인식 후 초기화
        use_container_width=True,
        key='stt2'
    )

    # 2단계: 텍스트 → 숫자 추출
    if weight_text:
        st.info(f"인식된 말: **{weight_text}**")
        numbers = re.findall(r'\d+\.?\d*', weight_text)   # 아라비아 숫자 추출
        if numbers:
            weight_value = float(numbers[0])
            st.success(f"✅ 입력된 숫자: **{weight_value}**")
            st.session_state.weight = weight_value
            #st.session_state['voice_number'] = weight_value
        else:
            st.warning("⚠️ 숫자를 찾지 못했어요. '75'처럼 또박또박 말해보세요.")


    if st.button("🧮 BMI 계산하고 음성으로 듣기", use_container_width=True, type="primary"):
        height = st.number_input(
            "키 (cm)", min_value=0.0, max_value=250.0,
            value=float(st.session_state.height or 0.0), step=0.1,
        )
        weight = st.number_input(
            "몸무게 (kg)", min_value=0.0, max_value=300.0,
            value=float(st.session_state.weight or 0.0), step=0.1
        )

        if height <= 0 or weight <= 0:
            st.warning("⚠️ 키와 몸무게를 먼저 입력해 주세요.")
        else:
            bmi = weight / ((height / 100) ** 2)
            category, emoji, advice = classify_bmi(bmi)
    
            # 화면 표시
            st.metric(label="당신의 BMI", value=f"{bmi:.1f}", delta=category)
            st.markdown(f"### {emoji} 판정: **{category}**")
            st.info(advice)


            message = (
                f"측정 결과를 알려드립니다. 키 {height:.0f} 센티미터, "
                f"몸무게 {weight:.0f} 킬로그램으로, "
                f"비엠아이 수치는 {bmi:.1f} 입니다. {category}에 해당합니다. {advice}"
            )
            with st.spinner("음성을 생성하는 중..."):
                audio = speak(message)
            st.audio(audio, format="audio/mp3")
            st.caption("▶️ 재생 버튼을 눌러 결과를 들어보세요.")

 
# =========================================================================
# Day 3 (7/8) : 위젯만들기
# ========================================================================= 
def day3_app():
    coming_soon(SCHEDULE[2])
 

# =========================================================================
# Day 4 (7/9) : 위젯만들기
# ========================================================================= 
def day4_app():
    coming_soon(SCHEDULE[3])
 
 
# =========================================================================
# Day 5 (7/10) : 설문조사 + AI 챗봇 앱
# =========================================================================
def day5_app():
    st.title("📅 Day 1 · 7월 6일 (월) — 설문조사 & AI 챗봇")
 
    sub_tab1, sub_tab2 = st.tabs(["📊 설문조사", "🤖 AI 챗봇"])
 
    with sub_tab1:
        _day5_survey()
    with sub_tab2:
        _day5_chatbot()
 
 
def _day5_survey():
    st.subheader("고등학생 관심사 설문조사")
    st.write(
        "여러분의 진로, 학업, 관심사에 대한 생각을 솔직하게 답해주세요! "
        "응답은 익명으로 저장되며, 제출 후 바로 전체 통계를 확인할 수 있어요."
    )
 
    with st.form("survey_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            grade = st.selectbox("학년", ["고1", "고2", "고3"])
        with col2:
            gender = st.selectbox("성별", ["선택 안 함", "남", "여"])
 
        career_interest = st.multiselect(
            "관심 있는 진로 분야를 모두 선택하세요",
            ["IT/개발", "의료/보건", "예술/디자인", "경영/경제", "교육",
             "과학/공학", "미디어/콘텐츠", "스포츠", "공무원/행정", "아직 잘 모르겠음"],
        )
        stress_level = st.slider("학업 스트레스 (1~10)", 1, 10, 5)
        study_hour = st.slider("하루 평균 자율 학습 시간(시간)", 0, 12, 3)
        sns_time = st.slider("하루 평균 SNS/유튜브 사용 시간(시간)", 0, 10, 3)
        hobby = st.selectbox(
            "가장 즐기는 취미는 무엇인가요?",
            ["게임", "운동", "음악감상/연주", "웹툰/독서", "영상 시청", "그림/사진", "친구와 대화", "기타"],
        )
        ai_usage = st.radio(
            "AI 챗봇을 얼마나 자주 사용하나요?",
            ["거의 안 씀", "가끔 씀(주 1~2회)", "자주 씀(거의 매일)"],
        )
        comment = st.text_area("고등학생 생활에서 가장 고민되는 점 (선택)")
 
        submitted = st.form_submit_button("설문 제출하기 🚀")
 
    if submitted:
        new_row = {
            "timestamp": datetime.datetime.now().isoformat(),
            "grade": grade, "gender": gender,
            "career_interest": ";".join(career_interest) if career_interest else "없음",
            "stress_level": stress_level, "study_hour": study_hour,
            "sns_time": sns_time, "hobby": hobby, "ai_usage": ai_usage,
            "comment": comment,
        }
        df_new = pd.DataFrame([new_row])
        if os.path.exists(SURVEY_FILE):
            df_new.to_csv(SURVEY_FILE, mode="a", header=False, index=False)
        else:
            df_new.to_csv(SURVEY_FILE, mode="w", header=True, index=False)
        st.success("설문 제출 완료! 소중한 응답 감사합니다 🙌")
 
    st.markdown("---")
    st.subheader("📈 지금까지의 설문 결과")
 
    if os.path.exists(SURVEY_FILE):
        df = pd.read_csv(SURVEY_FILE)
        st.write(f"총 응답 수: **{len(df)}명**")
 
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**학년별 응답 분포**")
            st.bar_chart(df["grade"].value_counts())
            st.markdown("**AI 챗봇 사용 빈도**")
            st.bar_chart(df["ai_usage"].value_counts())
        with c2:
            st.markdown("**평균 스트레스 / SNS / 학습시간**")
            st.bar_chart(pd.DataFrame(
                {"평균값": [df["stress_level"].mean(), df["sns_time"].mean(), df["study_hour"].mean()]},
                index=["학업 스트레스", "SNS 사용시간", "자율학습시간"],
            ))
            st.markdown("**관심 진로 분야 (전체 집계)**")
            st.bar_chart(df["career_interest"].str.split(";").explode().value_counts())
 
        with st.expander("📄 원본 응답 데이터 보기"):
            st.dataframe(df, use_container_width=True)
    else:
        st.info("아직 제출된 설문이 없어요. 위 설문을 먼저 작성해보세요!")
 
 
def _day5_chatbot():
    st.subheader("고등학생 진로/학습 AI 챗봇")
    st.write(
        "궁금한 진로, 공부법, 고민을 편하게 물어보세요! (Google **Gemini API** 사용 — "
        "결제수단 등록 없이 무료로 발급받은 키로 바로 테스트할 수 있어요.)"
    )
 
    with st.sidebar:
        st.markdown("### 🔑 Day5 챗봇 설정 (Gemini)")
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            value="",
            help="https://aistudio.google.com/apikey 에서 Google 계정으로 로그인 후 무료 발급. "
                 "키는 서버에 저장되지 않고 이 세션에서만 사용됩니다.",
        )
        model_name = st.selectbox(
            "모델 선택",
            ["gemini-2.5-flash", "gemini-2.5-flash-lite"],
            help="Flash / Flash-Lite 계열은 무료 티어(RPM/RPD 한도 내)에서 사용할 수 있는 모델입니다.",
        )
        persona = st.selectbox(
            "챗봇 성격 선택",
            ["친절한 진로상담 선생님", "논리적인 스터디 코치", "유머러스한 친구 같은 챗봇"],
        )
        if st.button("Day5 대화 초기화 🔄"):
            st.session_state.day5_chat_messages = []
            st.session_state.pop("day5_gemini_chat", None)
            st.session_state.pop("day5_gemini_chat_key", None)
            st.rerun()
 
    persona_prompts = {
        "친절한 진로상담 선생님": (
            "당신은 따뜻하고 친절한 고등학교 진로상담 선생님입니다. "
            "학생의 눈높이에 맞춰 쉽고 구체적으로, 격려하는 말투로 답변하세요."
        ),
        "논리적인 스터디 코치": (
            "당신은 체계적이고 논리적인 학습 코치입니다. "
            "학생의 질문에 단계별로, 근거를 들어 명확하게 답변하세요."
        ),
        "유머러스한 친구 같은 챗봇": (
            "당신은 학생과 친구처럼 편하게 대화하는 유쾌한 챗봇입니다. "
            "가볍고 재미있는 말투를 쓰되, 유용한 정보는 정확히 전달하세요."
        ),
    }
 
    if "day5_chat_messages" not in st.session_state:
        st.session_state.day5_chat_messages = []
 
    for msg in st.session_state.day5_chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
 
    prompt = st.chat_input("궁금한 것을 물어보세요!", key="day5_chat_input")
 
    if prompt:
        if not api_key:
            st.error("먼저 사이드바에 Gemini API Key를 입력해주세요! 🔑 (https://aistudio.google.com/apikey)")
            st.stop()
 
        st.session_state.day5_chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
 
        try:
            from google import genai
            from google.genai import types
 
            # 모델/페르소나가 바뀌면 채팅 세션을 새로 만들고, 그렇지 않으면 기존 세션(대화 맥락)을 재사용
            chat_key = f"{model_name}::{persona}"
            if st.session_state.get("day5_gemini_chat_key") != chat_key:
                client = genai.Client(api_key=api_key)
                st.session_state.day5_gemini_chat = client.chats.create(
                    model=model_name,
                    config=types.GenerateContentConfig(
                        system_instruction=persona_prompts[persona],
                    ),
                )
                st.session_state.day5_gemini_chat_key = chat_key
 
            chat = st.session_state.day5_gemini_chat
 
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                for chunk in chat.send_message_stream(prompt):
                    if chunk.text:
                        full_response += chunk.text
                        placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
 
            st.session_state.day5_chat_messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"오류가 발생했어요: {e}")
 
 
DAY_FUNCS = {1: day1_app, 2: day2_app, 3: day3_app, 4: day4_app, 5: day5_app}
 
 
# =========================================================================
# 사이드바 - 날짜(Day) 선택 네비게이션
# =========================================================================
with st.sidebar:
    st.title("📅 7월 특강 실습 모음")
    st.caption("2026.07.06 (월) ~ 2026.07.10 (금)")
    st.markdown("---")
 
    day_labels = [f"Day {s['day']} · {s['date']}" for s in SCHEDULE]
    selected_label = st.radio("날짜를 선택하세요", day_labels, index=0)
    selected_day = int(selected_label.split(" ")[1])
 
    st.markdown("---")
    st.markdown("**📋 전체 일정 한눈에 보기**")
    for s in SCHEDULE:
        mark = "✅" if s["day"] == 1 else "🔜"
        st.caption(f"{mark} Day{s['day']} ({s['date']}) — {s['title']}")
 
# -----------------------------------------------------------------------
# 선택된 날짜의 앱 실행
# -----------------------------------------------------------------------
DAY_FUNCS[selected_day]()