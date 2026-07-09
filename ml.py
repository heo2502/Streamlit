import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
st.set_page_config(page_title="ML 모델 데모 (sklearn)", layout="wide")
 
st.markdown("## 08-05. ML 모델 데모 (sklearn)")
st.info("분류/회귀 모델을 학습하고 입력값으로 즉시 예측해보는 데모 앱입니다.")
 
AUTHOR_NAME = "에드윈"
 
 
@st.cache_resource
def load_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    return model, iris, acc
 
 
model, iris, accuracy = load_model()
feature_names_kr = ["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)"]
target_names_kr = {"setosa": "세토사", "versicolor": "베르시컬러", "virginica": "버지니카"}
species_order = ["virginica", "versicolor", "setosa"]
 
st.markdown("### 🤖 ML 모델 데모 — Iris 분류")
st.caption(f"sklearn RandomForestClassifier · 정확도 {accuracy*100:.1f}% · 작성: {AUTHOR_NAME}")
 
col_input, col_result = st.columns(2)
 
with col_input:
    st.markdown("#### 입력 특성")
    sepal_length = st.slider(feature_names_kr[0], 4.3, 7.9, 5.8, 0.1)
    sepal_width = st.slider(feature_names_kr[1], 2.0, 4.4, 3.0, 0.1)
    petal_length = st.slider(feature_names_kr[2], 1.0, 6.9, 4.4, 0.1)
    petal_width = st.slider(feature_names_kr[3], 0.1, 2.5, 1.3, 0.1)
    predict_clicked = st.button("🔍 예측", use_container_width=True, type="primary")
 
    input_df = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=iris.feature_names,
    )
    proba = model.predict_proba(input_df)[0]
    pred_idx = int(np.argmax(proba))
    pred_species = iris.target_names[pred_idx]
    pred_proba_pct = proba[pred_idx] * 100
 
with col_result:
    st.markdown("#### 예측 결과")
 
    fig1, ax1 = plt.subplots(figsize=(5, 2.2))
    values = [proba[list(iris.target_names).index(sp)] * 100 for sp in species_order]
    colors = ["#e57373" if sp == pred_species else "#f8c9c9" for sp in species_order]
    bars = ax1.barh(species_order, values, color=colors, height=0.6)
    for bar, v in zip(bars, values):
        ax1.text(v + 2, bar.get_y() + bar.get_height() / 2, f"{v:.0f}%", va="center", fontsize=9)
    ax1.set_xlim(0, 100)
    ax1.spines[["top", "right", "left"]].set_visible(False)
    ax1.tick_params(left=False)
    ax1.set_xlabel("")
    fig1.tight_layout()
    st.pyplot(fig1)
 
    st.success(
        f"🌸 {pred_species} ({target_names_kr[pred_species]} · 확률 {pred_proba_pct:.0f}%) — "
        f"{target_names_kr[pred_species]} 종으로 분류"
    )
 
st.markdown("#### 특성 중요도")
importances = model.feature_importances_
order = np.argsort(importances)
sorted_feats = [feature_names_kr[i].split(" (")[0] for i in order]
sorted_vals = importances[order]
 
fig2, ax2 = plt.subplots(figsize=(9, 2.5))
ax2.barh(sorted_feats, sorted_vals, color="#2e7d32", height=0.55)
ax2.set_xlim(0, max(sorted_vals) * 1.2)
ax2.spines[["top", "right"]].set_visible(False)
fig2.tight_layout()
st.pyplot(fig2)