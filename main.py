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
    {"day": 1, "date": "7월 6일 (월)", "title": "준비중",
     "desc": "Day 1 실습 내용이 곧 업데이트됩니다."},
    {"day": 2, "date": "7월 7일 (화)", "title": "준비중",
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
# Day 1 (7/6) : 설문조사 + AI 챗봇 앱
# =========================================================================
def day1_app():
    st.title("📅 Day 1 · 7월 6일 (월) — 설문조사 & AI 챗봇")
 
    sub_tab1, sub_tab2 = st.tabs(["📊 설문조사", "🤖 AI 챗봇"])
 
    with sub_tab1:
        _day1_survey()
    with sub_tab2:
        _day1_chatbot()
 
 
def _day1_survey():
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
 
 
def _day1_chatbot():
    st.subheader("고등학생 진로/학습 AI 챗봇")
    st.write(
        "궁금한 진로, 공부법, 고민을 편하게 물어보세요! (Google **Gemini API** 사용 — "
        "결제수단 등록 없이 무료로 발급받은 키로 바로 테스트할 수 있어요.)"
    )
 
    with st.sidebar:
        st.markdown("### 🔑 Day1 챗봇 설정 (Gemini)")
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            value="AIzaSyDTnhwV0b6nJDkRubLX_w11pbjt1p_HaO4",
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
        if st.button("Day1 대화 초기화 🔄"):
            st.session_state.day1_chat_messages = []
            st.session_state.pop("day1_gemini_chat", None)
            st.session_state.pop("day1_gemini_chat_key", None)
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
 
    if "day1_chat_messages" not in st.session_state:
        st.session_state.day1_chat_messages = []
 
    for msg in st.session_state.day1_chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
 
    prompt = st.chat_input("궁금한 것을 물어보세요!", key="day1_chat_input")
 
    if prompt:
        if not api_key:
            st.error("먼저 사이드바에 Gemini API Key를 입력해주세요! 🔑 (https://aistudio.google.com/apikey)")
            st.stop()
 
        st.session_state.day1_chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
 
        try:
            from google import genai
            from google.genai import types
 
            # 모델/페르소나가 바뀌면 채팅 세션을 새로 만들고, 그렇지 않으면 기존 세션(대화 맥락)을 재사용
            chat_key = f"{model_name}::{persona}"
            if st.session_state.get("day1_gemini_chat_key") != chat_key:
                client = genai.Client(api_key=api_key)
                st.session_state.day1_gemini_chat = client.chats.create(
                    model=model_name,
                    config=types.GenerateContentConfig(
                        system_instruction=persona_prompts[persona],
                    ),
                )
                st.session_state.day1_gemini_chat_key = chat_key
 
            chat = st.session_state.day1_gemini_chat
 
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                for chunk in chat.send_message_stream(prompt):
                    if chunk.text:
                        full_response += chunk.text
                        placeholder.markdown(full_response + "▌")
                placeholder.markdown(full_response)
 
            st.session_state.day1_chat_messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"오류가 발생했어요: {e}")
 
 
# =========================================================================
# Day 2~5 : 아직 준비중 (자리만 잡아둔 스텁 함수)
# =========================================================================
def day2_app():
    coming_soon(SCHEDULE[1])
 
 
def day3_app():
    coming_soon(SCHEDULE[2])
 
 
def day4_app():
    coming_soon(SCHEDULE[3])
 
 
def day5_app():
    coming_soon(SCHEDULE[4])
 
 
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