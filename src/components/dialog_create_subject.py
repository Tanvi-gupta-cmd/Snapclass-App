import streamlit as st

from src.database.db import create_subject


@st.dialog("Create Subject")
def create_subject_dialog(teacher_id):

    subject_name = st.text_input("Subject Name")
    subject_code = st.text_input("Subject Code")
    section = st.text_input("Section")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cancel"):
            st.rerun()

    with col2:
        if st.button("Create", type="primary"):
            if not subject_name or not subject_code or not section:
                st.warning("Please fill all fields.")
                return

            create_subject(
                subject_code,
                subject_name,
                section,
                teacher_id
            )

            st.success("Subject created successfully!")
            st.rerun()