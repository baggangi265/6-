import streamlit as st

st.title("🏫 학사일정")

date = st.date_input("날짜")

content = st.text_input(
    "일정 내용",
    placeholder="예: 체육대회"
)

if st.button("저장"):

    if content:

        st.session_state.school_events.append({
            "date": str(date),
            "content": content
        })

        st.success("저장 완료")

st.divider()

st.subheader("등록된 일정")

if st.session_state.school_events:
    st.dataframe(st.session_state.school_events)
else:
    st.info("일정이 없습니다.")
