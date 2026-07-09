import streamlit as st

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

st.write("---")

st.write("---")

st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")
st.write("---")


