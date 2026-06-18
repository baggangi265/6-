import streamlit as st
import json

try:
    from google import genai
except:
    genai = None


def create_notice(events, tasks):

    if genai is None:
        return "google-genai 설치 필요"

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(
            api_key=api_key
        )

        prompt = f"""
너는 5반 공지 AI이다.

학사일정:
{json.dumps(events, ensure_ascii=False)}

수행평가:
{json.dumps(tasks, ensure_ascii=False)}

학생들이 보기 쉬운 공지문으로 정리해줘.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"오류: {e}"
import streamlit as st
from ai_utils import create_notice

st.title("🤖 AI 알림")

st.write("학사일정과 수행평가를 AI가 자동 정리합니다.")

if st.button("AI 공지 생성"):

    result = create_notice(
        st.session_state.school_events,
        st.session_state.performance_tasks
    )

    st.text_area(
        "단톡방 공지",
        result,
        height=400
    )
  streamlit
google-genai
