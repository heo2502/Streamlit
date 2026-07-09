import streamlit as st
from datetime import datetime
from io import BytesIO
from pathlib import Path
 
st.set_page_config(page_title="이력서 생성기", layout="wide")
 
st.info("폼 입력으로 마크다운/PDF 이력서를 즉시 생성합니다.")
 
AUTHOR_NAME = "에드윈"
 
TEMPLATES = {
    "미니멀": "#e53935",
    "모던": "#1e88e5",
    "클래식": "#37474f",
    "크리에이티브": "#8e24aa",
}
 
if "template" not in st.session_state:
    st.session_state.template = "미니멀"
 
col_form, col_preview, col_side = st.columns([1, 1.6, 1])
 
# ----------------------------- 왼쪽: 기본 정보 입력 -----------------------------
with col_form:
    st.markdown("#### 👤 기본 정보")
    name = st.text_input("이름", value="에드윈")
    job_title = st.text_input("직무", value="데이터 분석가 / Streamlit 엔지니어")
    email = st.text_input("이메일", value="edwin@example.com")
    phone = st.text_input("연락처", value="010-1234-5678")
    github = st.text_input("GitHub", value="github.com/edwin")
 
    st.markdown("#### ✍️ 자기소개")
    intro = st.text_area(
        "소개",
        value="데이터로 비즈니스 문제를 빠르게 검증하고 자동화하는 일을 좋아합니다. "
        "Streamlit으로 6개월간 12개의 사내 도구를 만들어 운영 시간을 주당 18시간 단축했습니다.",
        height=100,
    )
 
    st.markdown("#### 🛠️ 스킬")
    skills_raw = st.text_input(
        "기술 (쉼표 구분)",
        value="Python, SQL, Streamlit, pandas, scikit-learn, Docker, AWS",
    )
    skills = [s.strip() for s in skills_raw.split(",") if s.strip()]
 
    st.markdown("#### 💼 경력")
    company = st.text_input("회사 · 부서", value="테크컴퍼니 · 데이터 플랫폼팀")
    period = st.text_input("근무 기간", value="2024.03 - 현재")
    achievements_raw = st.text_area(
        "성과 (한 줄에 하나씩)",
        value="Streamlit + DuckDB 기반 사내 BI 12개 운영, 월 평균 사용자 280명\n"
        "A/B 테스트 분석 자동화로 PM 분석 시간 60% 단축",
        height=90,
    )
    achievements = [a.strip() for a in achievements_raw.split("\n") if a.strip()]
 
# ----------------------------- 이력서 콘텐츠 조립 -----------------------------
accent = TEMPLATES[st.session_state.template]
skill_count = len(skills)
career_years = 1
try:
    start_year = int(period.split(".")[0])
    career_years = max(1, datetime.now().year - start_year + 1)
except (ValueError, IndexError):
    pass
total_pages = 1 if (len(intro) + len(achievements_raw)) < 600 else 2
 
 
def build_markdown() -> str:
    lines = [f"# {name}", f"**{job_title}**", ""]
    lines.append(f"📧 {email} · 📱 {phone} · 🔗 {github}")
    lines.append("")
    lines.append("---")
    lines.append("## 소개")
    lines.append(intro)
    lines.append("")
    lines.append("## 스킬")
    lines.append(" · ".join(skills))
    lines.append("")
    lines.append("## 경력")
    lines.append(f"**{company}** · {period}")
    for a in achievements:
        lines.append(f"- {a}")
    return "\n".join(lines)
 
 
def find_korean_font() -> Path | None:
    """한글을 지원하는 트루타입 폰트를 앱 폴더와 OS의 대표적인 위치에서 찾는다."""
    candidates = [
        Path(__file__).parent / "fonts" / "NanumGothic.ttf",
        Path("/usr/share/fonts/truetype/nanum/NanumGothic.ttf"),
        Path("/usr/share/fonts/truetype/nanum-gothic/NanumGothic.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("C:/Windows/Fonts/malgun.ttf"),
        Path("/System/Library/Fonts/AppleSDGothicNeo.ttc"),
    ]
    for c in candidates:
        if c.exists() and c.suffix.lower() == ".ttf":
            return c
    return None
 
 
def build_pdf_bytes() -> bytes:
    from fpdf import FPDF
 
    pdf = FPDF()
    pdf.add_page()
 
    font_path = find_korean_font()
    if font_path is not None:
        pdf.add_font("Nanum", "", str(font_path))
        base_font = "Nanum"
    else:
        # 한글 트루타입 폰트를 찾지 못했습니다. Helvetica는 한글을 지원하지 않으므로
        # 이 상태에서 한글이 포함된 텍스트를 쓰면 fpdf2가 예외를 발생시킵니다.
        # fonts/NanumGothic.ttf 파일을 이 스크립트와 같은 폴더의 fonts 하위 폴더에 넣어주세요.
        raise RuntimeError(
            "한글 폰트를 찾을 수 없습니다. fonts/NanumGothic.ttf 파일을 앱 폴더에 추가해 주세요. "
            "(다운로드: https://hangeul.naver.com/font 또는 Google Fonts의 Nanum Gothic)"
        )
 
    pdf.set_font(base_font, size=20)
    pdf.cell(0, 12, text=name, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(base_font, size=12)
    pdf.cell(0, 8, text=job_title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(base_font, size=10)
    pdf.cell(0, 8, text=f"{email} | {phone} | {github}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
 
    pdf.set_font(base_font, size=13)
    pdf.cell(0, 8, text="소개", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(base_font, size=10)
    pdf.multi_cell(0, 6, text=intro)
    pdf.ln(2)
 
    pdf.set_font(base_font, size=13)
    pdf.cell(0, 8, text="스킬", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(base_font, size=10)
    pdf.multi_cell(0, 6, text=" · ".join(skills))
    pdf.ln(2)
 
    pdf.set_font(base_font, size=13)
    pdf.cell(0, 8, text="경력", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(base_font, size=10)
    pdf.cell(0, 6, text=f"{company}  ({period})", new_x="LMARGIN", new_y="NEXT")
    for a in achievements:
        pdf.multi_cell(0, 6, text=f"- {a}")
 
    return bytes(pdf.output())
 
 
# ----------------------------- 가운데: 실시간 미리보기 -----------------------------
with col_preview:
    st.markdown("### 📝 이력서 생성기")
    st.caption(f"실시간 미리보기 · MD/PDF 즉시 다운로드 — 작성: {AUTHOR_NAME}")
 
    st.markdown("#### 👁️ 미리보기")
    with st.container(border=True):
        st.markdown(f"## {name}")
        st.markdown(f"**{job_title}**")
        st.caption(f"✉️ {email}  ·  📞 {phone}  ·  🔗 {github}")
        st.markdown(
            f"<hr style='border:2px solid {accent}; margin:6px 0 14px 0;'>",
            unsafe_allow_html=True,
        )
 
        st.markdown("**소개**")
        st.write(intro)
 
        st.markdown("**스킬**")
        badge_html = " ".join(
            f"<span style='background:{accent}20;color:{accent};padding:3px 10px;"
            f"border-radius:12px;margin-right:6px;font-size:0.85em;'>{s}</span>"
            for s in skills
        )
        st.markdown(badge_html, unsafe_allow_html=True)
 
        st.markdown("**경력**")
        st.markdown(f"{company} · {period}")
        for a in achievements:
            st.markdown(f"- {a}")
 
    md_text = build_markdown()
    col_md, col_pdf = st.columns(2)
    with col_md:
        st.download_button(
            "⬇️ Markdown 다운로드",
            data=md_text.encode("utf-8"),
            file_name=f"{name}_이력서.md",
            mime="text/markdown",
            use_container_width=True,
            key="download_md_btn",
        )
    with col_pdf:
        try:
            pdf_bytes = build_pdf_bytes()
        except ImportError:
            st.warning("PDF 생성을 위해 터미널에서 uv add fpdf2 를 실행한 뒤 앱을 완전히 재시작해 주세요.")
        except Exception as e:
            st.error("PDF 생성 중 오류가 발생했습니다.")
            st.exception(e)
        else:
            st.download_button(
                "⬇️ PDF 다운로드",
                data=pdf_bytes,
                file_name=f"{name}_이력서.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_pdf_btn",
            )
 
# ----------------------------- 오른쪽: 템플릿 + 통계 -----------------------------
with col_side:
    st.markdown("#### 🎨 템플릿")
    template_names = list(TEMPLATES.keys())
    for i in range(0, len(template_names), 2):
        row = st.columns(2)
        for j, tname in enumerate(template_names[i : i + 2]):
            with row[j]:
                is_selected = st.session_state.template == tname
                label = f"✓ {tname}" if is_selected else tname
                if st.button(label, key=f"tpl_{tname}", use_container_width=True):
                    st.session_state.template = tname
                    st.rerun()
 
    st.markdown("#### 📊 통계")
    st.metric("총 페이지", total_pages)
    st.metric("스킬 수", skill_count)
    st.metric("경력 연수", f"{career_years}년")