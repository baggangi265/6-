import streamlit as st

st.set_page_config(
    page_title="5반 AI 학사비서",
    page_icon="📚"
)

if "school_events" not in st.session_state:
    st.session_state.school_events = []

if "performance_tasks" not in st.session_state:
    st.session_state.performance_tasks = []

st.title("📚 5반 AI 학사비서")

st.markdown("""
### 기능 안내

- 🏫 학사일정 등록
- 📝 수행평가 관리
- 🤖 AI 공지 생성
- ⏰ 중요 일정 확인

왼쪽 사이드바에서 메뉴를 선택하세요.
""")

st.info("5반 단톡방 공지용 AI 비서")
