import streamlit as st
from PIL import Image
import pandas as pd
 
st.set_page_config(page_title="YOLO 이미지 분류 앱", page_icon="🧠", layout="wide")
 
st.title("🧠 YOLO 기반 이미지 분류 앱")
st.write("내가 직접 학습시킨 YOLO 분류 모델(best.pt) 또는 기본 사전학습 모델로 이미지를 분류해보세요.")
 
 
# -----------------------------------------------------------------------
# 모델 로딩 (한 번 로딩한 모델은 캐시에 저장 -> 다시 안 만들어도 됨)
# -----------------------------------------------------------------------
@st.cache_resource(show_spinner="모델을 불러오는 중입니다...")
def load_model(model_path_or_name: str):
    from ultralytics import YOLO
    return YOLO(model_path_or_name)
 
 
with st.sidebar:
    st.header("⚙️ 모델 설정")
    model_choice = st.radio(
        "사용할 모델을 선택하세요",
        ["내가 학습시킨 모델 (best.pt)", "기본 사전학습 모델 (yolo11n-cls.pt)"],
    )
 
    if model_choice.startswith("내가"):
        model_path = st.text_input(
            "학습된 모델 파일 경로",
            value="runs/classify/train/weights/best.pt",
            help="train_yolo_classifier.py 실행 후 생성된 best.pt 경로를 입력하세요.",
        )
    else:
        model_path = "yolo11n-cls.pt"
        st.caption("ImageNet 1000개 클래스로 미리 학습된 기본 모델입니다. (예: golden retriever, banana 등)")
 
    top_k = st.slider("상위 몇 개 결과를 보여줄까요?", 1, 10, 5)
 
# -----------------------------------------------------------------------
# 이미지 업로드 & 분류
# -----------------------------------------------------------------------
uploaded_file = st.file_uploader("분류할 이미지를 업로드하세요", type=["png", "jpg", "jpeg"])
 
col_left, col_right = st.columns([1, 1.4])
 
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
 
    with col_left:
        st.subheader("📷 업로드한 이미지")
        st.image(image, use_container_width=True)
 
    with col_right:
        st.subheader("🔍 분류 결과")
        try:
            model = load_model(model_path)
            results = model.predict(image, verbose=False)
            result = results[0]
 
            names = result.names  # {인덱스: 클래스명}
            probs = result.probs.data.cpu().numpy()  # 클래스별 확률 배열
 
            df = pd.DataFrame(
                {"클래스": [names[i] for i in range(len(probs))], "확률(%)": probs * 100}
            ).sort_values("확률(%)", ascending=False).head(top_k)
 
            top1_name = df.iloc[0]["클래스"]
            top1_prob = df.iloc[0]["확률(%)"]
            st.success(f"✅ 가장 유사한 클래스: **{top1_name}** ({top1_prob:.1f}%)")
 
            st.bar_chart(df.set_index("클래스"))
            with st.expander("📄 전체 확률 표로 보기"):
                st.dataframe(df.reset_index(drop=True), use_container_width=True)
 
        except FileNotFoundError:
            st.error(
                f"모델 파일을 찾을 수 없습니다: `{model_path}`\n\n"
                "먼저 `train_yolo_classifier.py`로 모델을 학습시키거나, "
                "사이드바에서 '기본 사전학습 모델'을 선택해보세요."
            )
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
else:
    with col_left:
        st.info("이미지를 업로드하면 여기에 미리보기가 표시됩니다.")
    with col_right:
        st.info("이미지를 업로드하면 오른쪽에 분류 결과(클래스별 확률)가 표시됩니다.")