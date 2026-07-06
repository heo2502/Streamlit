import streamlit as st
 
st.set_page_config(page_title="5일 강의 실습노트", page_icon="📅", layout="wide")
 
# -----------------------------------------------------------------------
# 1) 사이드바 - 날짜(Day) 목록을 라디오 버튼으로 보여주기
# -----------------------------------------------------------------------
st.sidebar.title("📅 📆5일 강의 일정")
st.sidebar.caption("날짜를 클릭하면 그날의 실습/과제 화면으로 이동합니다.")
 
selected_day = st.sidebar.radio(
    "날짜를 선택하세요",
    [
        "Day 1 · 7월 6일 (월)",
        "Day 2 · 7월 7일 (화)",
        "Day 3 · 7월 8일 (수)",
        "Day 4 · 7월 9일 (목)",
        "Day 5 · 7월 10일 (금)",
    ],
)
 
# -----------------------------------------------------------------------
# 2) 화면 상단 - 오늘 선택된 날짜 제목 표시
# -----------------------------------------------------------------------
st.title(selected_day)
st.divider()
 
# -----------------------------------------------------------------------
# 3) 실습 / 과제 탭 만들기 (모든 날짜가 이 탭 두 개를 공통으로 사용)
# -----------------------------------------------------------------------
tab_practice, tab_assignment = st.tabs(["📘 실습", "📝 과제"])
 
# -----------------------------------------------------------------------
# 4) 선택된 날짜에 따라 다른 내용을 보여주기 (순차 구조 + if/elif)
#    ↓↓↓ 매일 수업이 끝나면, 아래 각 날짜 블록 안에 내용을 추가해주세요 ↓↓↓
# -----------------------------------------------------------------------
 
if selected_day == "Day 1 · 7월 6일 (월)":
 
    with tab_practice:
        st.header("Day 1 실습")
        st.write("여기에 Day 1 실습 내용을 작성하세요.")
        st.info("1일차 실습내용")
 
    with tab_assignment:
        st.header("Day 1 과제")
        st.write("여기에 Day 1 과제 내용을 작성하세요.")
        st.info("예: 오늘 배운 st.title, st.write를 이용해 자기소개 화면 만들어오기")
 
elif selected_day == "Day 2 · 7월 7일 (화)":
 
    with tab_practice:
        st.header("Day 2 실습")
        st.write("여기에 Day 2 실습 내용을 작성하세요.")
        st.info("예: 버튼, 슬라이더, 선택박스 등 입력 위젯 실습")
 
    with tab_assignment:
        st.header("Day 2 과제")
        st.write("여기에 Day 2 과제 내용을 작성하세요.")
        st.info("예: 슬라이더 값에 따라 다른 문구가 나오는 미니 앱 만들어오기")
 
elif selected_day == "Day 3 · 7월 8일 (수)":
 
    with tab_practice:
        st.header("Day 3 실습")
        st.write("여기에 Day 3 실습 내용을 작성하세요.")
        st.info("예: 컬럼, 탭, 표, 차트를 이용한 미니 대시보드 만들기")
 
    with tab_assignment:
        st.header("Day 3 과제")
        st.write("여기에 Day 3 과제 내용을 작성하세요.")
        st.info("예: 관심 있는 데이터를 표와 차트로 시각화해보기")
 
elif selected_day == "Day 4 · 7월 9일 (목)":
 
    with tab_practice:
        st.header("Day 4 실습")
        st.write("여기에 Day 4 실습 내용을 작성하세요.")
        st.info("예: st.form, session_state로 값이 계속 기억되는 앱 만들기")
 
    with tab_assignment:
        st.header("Day 4 과제")
        st.write("여기에 Day 4 과제 내용을 작성하세요.")
        st.info("예: 버튼을 누를 때마다 점수가 누적되는 카운터 앱 만들어오기")
 
elif selected_day == "Day 5 · 7월 10일 (금)":
 
    with tab_practice:
        st.header("Day 5 실습")
        st.write("여기에 Day 5 실습 내용을 작성하세요.")
        st.info("예: 설문조사 앱 + AI 챗봇 최종 프로젝트 완성하기")
 
    with tab_assignment:
        st.header("Day 5 과제")
        st.write("여기에 Day 5 과제 내용을 작성하세요.")
        st.info("예: 완성한 앱을 발표하고, 개선하고 싶은 점 1가지 적어오기")
