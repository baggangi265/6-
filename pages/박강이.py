import streamlit as st
from datetime import datetime

st.title("📝 수행평가 알림")

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

st.subheader("등록된 수행평가")

if st.session_state.performance_tasks:
    st.dataframe(st.session_state.performance_tasks)

today = datetime.today().date()

st.divider()
st.subheader("⏰ 임박한 수행평가")

for task in st.session_state.performance_tasks:

    try:
        d = datetime.strptime(
            task["date"],
            "%Y-%m-%d"
        ).date()

        diff = (d - today).days

        if 0 <= diff <= 7:

            st.warning(
                f"{task['subject']} - {task['content']} ({task['date']})"
            )

    except:
        pass
