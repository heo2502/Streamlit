import streamlit as st
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