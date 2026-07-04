import os
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import tempfile

st.set_page_config(
    page_title="음성 입력·음성 출력 웹앱",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ 음성으로 입력하고, 음성과 텍스트로 출력하기")
st.caption("고등학생 Streamlit 미니프로젝트 예제")

st.info(
    "마이크 버튼을 눌러 말하면, 앱이 음성을 텍스트로 바꾸고 "
    "그 텍스트를 다시 음성으로 읽어줍니다."
)

audio_value = st.audio_input("여기를 눌러 음성을 녹음하세요")

# height = st.number_input('키(cm)', 100, 220)
# weight = st.number_input('몸무게(kg)', 20, 150)
# bmi = weight / ((height/100) ** 2)
# st.write(round(bmi, 2))

if audio_value is not None:
    st.subheader("1단계: 녹음된 음성")
    st.audio(audio_value)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_value.getvalue())
        audio_path = tmp_file.name

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language="ko-KR")

        st.subheader("2단계: 음성을 텍스트로 변환한 결과")
        st.success(text)

        st.subheader("3단계: 텍스트를 다시 음성으로 출력")

        tts = gTTS(text=text, lang="ko")
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        st.audio(mp3_fp, format="audio/mp3")

        st.write("💬 앱의 답변:")
        st.write(f"당신이 말한 내용은 **'{text}'** 입니다.")

    except sr.UnknownValueError:
        st.error("음성을 알아듣지 못했습니다. 조금 더 또렷하게 말해보세요.")

    except sr.RequestError:
        st.error("음성 인식 서비스에 연결할 수 없습니다. 인터넷 연결을 확인하세요.")

    except Exception as e:
        st.error("오류가 발생했습니다.")
        st.code(str(e))

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

st.divider()

st.markdown("""
### ✅ 실습 확장 아이디어

1. 음성으로 입력한 문장을 영어로 번역하기  
2. 음성으로 오늘의 기분을 말하면 감정 분석하기  
3. 음성으로 메뉴를 말하면 추천 결과 출력하기  
4. 음성 일기장 만들기  
5. 음성 퀴즈 앱 만들기  
""")