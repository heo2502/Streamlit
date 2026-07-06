import streamlit as st
 
st.set_page_config(page_title="BMI 계산기", page_icon="⚖️", layout="wide")
 
st.title("BMI 계산기")
st.write("키와 몸무게를 입력하고 버튼을 눌러 체질량지수(BMI)를 확인해보세요.")
st.divider()
 
col_input, col_result = st.columns(2)
 
with col_input:
    st.header("정보 입력")
    height_cm = st.slider("키 (cm)", min_value=100, max_value=220, value=165)
    weight_kg = st.slider("몸무게 (kg)", min_value=30, max_value=150, value=55)
    calculate = st.button("BMI 계산하기")
 
with col_result:
    st.header("결과")
 
    if calculate:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
 
        # 대한비만학회(KSSO) 기준: 저체중 <18.5 / 정상 18.5~22.9 / 과체중 23~24.9 / 비만 25 이상
        if bmi < 18.5:
            category = "저체중"
        elif bmi < 23:
            category = "정상 체중"
        elif bmi < 25:
            category = "과체중"
        else:
            category = "비만"
 
        st.metric(label="나의 BMI", value=f"{bmi:.1f}", delta=category, delta_color="off")
 
        # BMI 값을 0.0~1.0 사이 진행률로 환산 (15~35 범위를 기준으로)
        scale_min, scale_max = 15, 35
        progress_value = max(0.0, min(1.0, (bmi - scale_min) / (scale_max - scale_min)))
        st.progress(progress_value, text=f"저체중 ← BMI {bmi:.1f} → 비만")
 
        if category == "저체중":
            st.info("표준 체중보다 가벼운 편입니다. 균형 잡힌 식사가 도움이 될 수 있어요.")
        elif category == "정상 체중":
            st.success("건강한 범위의 체중입니다. 지금처럼 잘 유지해보세요.")
        elif category == "과체중":
            st.warning("표준보다 조금 높은 편입니다. 꾸준한 활동이 도움이 될 수 있어요.")
        else:
            st.error("전문가와 상담을 통해 건강 관리 계획을 세워보는 것을 권장합니다.")
 
        st.caption(
            "이 결과는 대한비만학회 성인 기준을 적용한 참고용 계산입니다. "
            "성장기 청소년은 나이·성별별 성장도표(퍼센타일)를 함께 보는 것이 더 정확합니다."
        )
    else:
        st.info("왼쪽에서 키와 몸무게를 입력하고 'BMI 계산하기' 버튼을 눌러주세요.")