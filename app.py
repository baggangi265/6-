import streamlit as st
from data_manager import init_data
from ui_components import (
    school_schedule_ui,
    performance_ui,
    show_data,
    show_upcoming
)
from ai_utils import ai_summary

st.set_page_config(
    page_title="5반 AI 학사비서",
    page_icon="📚",
    layout="wide"
)

st.title("📚 5반 AI 학사비서")

init_data()

col1, col2 = st.columns(2)

with col1:
    school_schedule_ui()

with col2:
    performance_ui()

st.divider()

show_data()

st.divider()

show_upcoming()

st.divider()

st.subheader("🤖 AI 공지 생성")

if st.button("AI 공지 만들기"):

    result = ai_summary(
        st.session_state.school_events,
        st.session_state.performance_tasks
    )

    st.text_area(
        "공지문",
        result,
        height=350
    )
