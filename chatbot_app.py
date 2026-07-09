import streamlit as st

st.set_page_config(page_title="Streamlit 챗봇", page_icon="🤖", layout="centered")

st.title("🤖 Streamlit 챗봇")
st.caption("간단한 질문응답 챗봇입니다. API 키 없이도 바로 테스트할 수 있어요.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

with st.sidebar:
    st.header("⚙️ 설정")
    mode = st.selectbox("모드", ["로컬 응답", "Gemini API (선택)"])
    st.info("Gemini를 쓰려면 API 키를 입력하세요. 없으면 로컬 모드로 실행됩니다.")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="입력하지 않아도 됨")


def local_reply(user_text: str) -> str:
    text = user_text.strip()
    lower = text.lower()

    if any(word in lower for word in ["안녕", "반가", "hi", "hello"]):
        return "안녕하세요! 저는 Streamlit으로 만든 챗봇이에요. 무엇이 궁금하신가요?"
    if any(word in lower for word in ["날씨", "기후"]):
        return "현재 날씨는 제가 직접 확인할 수는 없지만, 오늘의 날씨는 기상 앱에서 확인해보세요."
    if any(word in lower for word in ["이름", "누구"]):
        return "저는 Streamlit 기반의 챗봇입니다. 도움이 필요하면 편하게 질문해 주세요."
    if any(word in lower for word in ["파이썬", "코딩", "프로그램"]):
        return "파이썬과 Streamlit으로 웹 앱을 만들 수 있어요. 원하시면 예제 코드를 보여드릴게요."
    if any(word in lower for word in ["감사", "고마워"]):
        return "천만에요. 더 도와드릴 일이 있으면 말씀해 주세요."
    return "좋은 질문이네요. 조금 더 구체적으로 말해주시면 더 잘 도와드릴 수 있어요."


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if mode == "Gemini API (선택)" and api_key:
        try:
            from google import genai

            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            answer = response.text
        except Exception as e:
            answer = f"Gemini 호출 중 오류가 발생했어요: {e}\n\n로컬 모드로 다시 응답합니다."
    else:
        answer = local_reply(prompt)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
