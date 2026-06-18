import streamlit as st
from datetime import datetime

st.title("📝 수행평가 알림")

# 수행평가 등록
date = st.date_input("수행평가 날짜")

subject = st.text_input("과목")

content = st.text_input(
    "수행 내용",
    placeholder="예: 독서 발표"
)

if st.button("등록"):

    if subject and content:

        st.session_state.performance_tasks.append({
            "date": str(date),
            "subject": subject,
            "content": content
        })

        st.success("등록 완료")

st.divider()

# 등록된 수행평가
st.subheader("등록된 수행평가")

if st.session_state.performance_tasks:
    st.dataframe(st.session_state.performance_tasks)
else:
    st.info("등록된 수행평가가 없습니다.")

today = datetime.today().date()

# -------------------------
# 수행평가 임박 알림
# -------------------------
st.divider()
st.subheader("⏰ 7일 이내 수행평가")

found_task = False

for task in st.session_state.performance_tasks:

    try:
        d = datetime.strptime(
            task["date"],
            "%Y-%m-%d"
        ).date()

        diff = (d - today).days

        if 0 <= diff <= 7:

            found_task = True

            st.warning(
                f"D-{diff} | {task['subject']} - {task['content']} ({task['date']})"
            )

    except:
        pass

if not found_task:
    st.success("7일 이내 수행평가가 없습니다.")

# -------------------------
# 학사일정 임박 알림
# -------------------------
st.divider()
st.subheader("🏫 7일 이내 학사일정")

found_event = False

for event in st.session_state.school_events:

    try:
        d = datetime.strptime(
            event["date"],
            "%Y-%m-%d"
        ).date()

        diff = (d - today).days

        if 0 <= diff <= 7:

            found_event = True

            st.info(
                f"D-{diff} | {event['content']} ({event['date']})"
            )

    except:
        pass

if not found_event:
    st.success("7일 이내 학사일정이 없습니다.")
