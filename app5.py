import streamlit as st
 
st.set_page_config(page_title="5일 강의 실습노트", page_icon="📅", layout="wide")
 
 
# =========================================================================
# 1) 함수 정의 구역 (def)
#    - 여기서는 "이런 화면을 만드는 방법"만 미리 적어둘 뿐, 아직 화면에 아무것도 그려지지 않습니다.
#    - 마치 요리 레시피를 적어두는 것과 같아서, 나중에 "이 레시피대로 만들어줘!"라고
#      호출(function_name())해야 그때 실제로 화면이 그려집니다.
# =========================================================================
 
def show_day1():
    tab_practice, tab_assignment1, tab_assignment2 = st.tabs(["📘 실습", "📝 과제1", "📝 과제2"])
    with tab_practice:
        st.header("Day 1 실습")
 
    
    with tab_assignment1:
        st.header("Day 1 과제1")
        st.write("여기에 Day 1 과제1 내용을 작성하세요.")
        import random
 
        st.set_page_config(page_title="나의 프로필 & 오늘의 명언", page_icon="✨", layout="wide")
        
        quotes = [
            ("시작이 반이다.", "아리스토텔레스"),
            ("천 리 길도 한 걸음부터.", "한국 속담"),
            ("가장 큰 위험은 위험 없는 삶이다.", "작자 미상"),
            ("오늘 할 수 있는 일을 내일로 미루지 마라.", "벤저민 프랭클린"),
            ("실패는 성공으로 가는 과정일 뿐이다.", "토마스 에디슨"),
            ("배움에 있어 늦은 때는 없다.", "작자 미상"),
            ("작은 습관이 큰 변화를 만든다.", "제임스 클리어"),
        ]
        
        if "quote_index" not in st.session_state:
            st.session_state.quote_index = random.randrange(len(quotes))
        
        st.title("나의 프로필 & 오늘의 명언")
        st.write("")
        
        col_profile, col_quote = st.columns(2)
        
        with col_profile:
            st.header("내 프로필")
            st.subheader("김수연")
            st.write("고등학교 2학년, 미래의 개발자")
            st.write("관심사: 게임, 음악, 파이썬, 디저트")
            st.info("위 이름과 소개, 관심사를 자기 것으로 바꿔보세요.")
        
        with col_quote:
            st.header("오늘의 명언")
            quote_text, quote_author = quotes[st.session_state.quote_index]
            st.success(quote_text)
            st.write(f"말한 사람: {quote_author}")
        
            if st.button("다른 명언 보기"):
                st.session_state.quote_index = random.randrange(len(quotes))
                st.rerun()
    with tab_assignment2:
        st.header("Day 1 과제2")
        st.write("여기에 Day 1 과제2 내용을 작성하세요.")
        st.info("예: 오늘 배운 st.title, st.write를 이용해 자기소개 화면 만들어오기")
 
 
def show_day2():
    tab_practice, tab_assignment1, tab_assignment2 = st.tabs(["📘 실습", "📝 과제1", "📝 과제2"])
    with tab_practice:
        st.header("Day 2 실습")
        st.write("여기에 Day 2 실습 내용을 작성하세요.")
        st.info("예: 버튼, 슬라이더, 선택박스 등 입력 위젯 실습")
    with tab_assignment1:
        st.header("Day 2 과제1")
        st.write("여기에 Day 2 과제1 내용을 작성하세요.")
        st.info("예: 슬라이더 값에 따라 다른 문구가 나오는 미니 앱 만들어오기")
    with tab_assignment2:
        st.header("Day 2 과제2")
        st.write("여기에 Day 2 과제2 내용을 작성하세요.")
        st.info("예: 슬라이더 값에 따라 다른 문구가 나오는 미니 앱 만들어오기")
 
 
def show_day3():
    tab_practice, tab_assignment1, tab_assignment2 = st.tabs(["📘 실습", "📝 과제1", "📝 과제2"])
    with tab_practice:
        st.header("Day 3 실습")
        st.write("여기에 Day 3 실습 내용을 작성하세요.")
        st.info("예: 컬럼, 탭, 표, 차트를 이용한 미니 대시보드 만들기")
    with tab_assignment1:
        st.header("Day 3 과제1")
        st.write("여기에 Day 3 과제1 내용을 작성하세요.")
        st.info("예: 관심 있는 데이터를 표와 차트로 시각화해보기")
    with tab_assignment2:
        st.header("Day 3 과제2")
        st.write("여기에 Day 3 과제2 내용을 작성하세요.")
        st.info("예: 관심 있는 데이터를 표와 차트로 시각화해보기")
 
 
def show_day4():
    tab_practice, tab_assignment1, tab_assignment2 = st.tabs(["📘 실습", "📝 과제1", "📝 과제2"])
    with tab_practice:
        st.header("Day 4 실습")
        st.write("여기에 Day 4 실습 내용을 작성하세요.")
        st.info("예: st.form, session_state로 값이 계속 기억되는 앱 만들기")
    with tab_assignment1:
        st.header("Day 4 과제1")
        st.write("여기에 Day 4 과제1 내용을 작성하세요.")
        st.info("예: 버튼을 누를 때마다 점수가 누적되는 카운터 앱 만들어오기")
    with tab_assignment2:
        st.header("Day 4 과제2")
        st.write("여기에 Day 4 과제2 내용을 작성하세요.")
        st.info("예: 버튼을 누를 때마다 점수가 누적되는 카운터 앱 만들어오기")      
 
 
def show_day5():
    tab_practice, tab_assignment1, tab_assignment2 = st.tabs(["📘 실습", "📝 과제1", "📝 과제2"])
    with tab_practice:
        st.header("Day 5 실습")
        st.write("여기에 Day 5 실습 내용을 작성하세요.")
        st.info("예: 설문조사 앱 + AI 챗봇 최종 프로젝트 완성하기")
    with tab_assignment1:
        st.header("Day 5 과제1")
        st.write("여기에 Day 5 과제1 내용을 작성하세요.")
        st.info("예: 완성한 앱을 발표하고, 개선하고 싶은 점 1가지 적어오기")
    with tab_assignment2:
        st.header("Day 5 과제2")
        st.write("여기에 Day 5 과제2 내용을 작성하세요.")
        st.info("예: 완성한 앱을 발표하고, 개선하고 싶은 점 1가지 적어오기")
 
 
# =========================================================================
# 2) 메인 코드 구역
#    - 여기서부터 실제로 화면에 무엇을 그릴지 "순서대로" 실행됩니다.
#    - 위에서 미리 적어둔 함수들 중, 선택된 날짜에 맞는 함수 하나만 "호출"합니다.
# =========================================================================
 
st.sidebar.title("📅 5일 강의 일정")
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
 
st.title(selected_day)
st.divider()
 
if selected_day == "Day 1 · 7월 6일 (월)":
    show_day1()          # ← 위에서 정의해둔 show_day1() 함수를 "호출"
elif selected_day == "Day 2 · 7월 7일 (화)":
    show_day2()
elif selected_day == "Day 3 · 7월 8일 (수)":
    show_day3()
elif selected_day == "Day 4 · 7월 9일 (목)":
    show_day4()
elif selected_day == "Day 5 · 7월 10일 (금)":
    show_day5()