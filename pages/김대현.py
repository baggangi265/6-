import streamlit as st
import json

try:
    from google import genai
except Exception:
    genai = None


def create_notice(events, tasks):

    if genai is None:
        return "google-genai 라이브러리가 설치되지 않았습니다."

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(api_key=api_key)

        prompt = f"""
너는 고등학교 5반 공지 AI이다.

학사일정:
{json.dumps(events, ensure_ascii=False)}

수행평가:
{json.dumps(tasks, ensure_ascii=False)}

학생들이 보기 쉬운 단톡방 공지문을 작성해라.

출력 형식:

📢 5반 공지

⚠️ 중요 일정

📝 수행평가
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except KeyError:
        return "GEMINI_API_KEY가 설정되지 않았습니다."

    except Exception as e:
        return f"오류 발생: {e}"


if "school_events" not in st.session_state:
    st.session_state.school_events = []

if "performance_tasks" not in st.session_state:
    st.session_state.performance_tasks = []

st.title("🤖 AI 알림")

st.write("학사일정과 수행평가를 AI가 자동으로 정리합니다.")

if st.button("AI 공지 생성"):

    if (
        not st.session_state.school_events
        and not st.session_state.performance_tasks
    ):
        st.warning("먼저 일정을 입력하세요.")

    else:

        result = create_notice(
            st.session_state.school_events,
            st.session_state.performance_tasks
        )

        st.text_area(
            "단톡방 공지",
            result,
            height=400
        )
