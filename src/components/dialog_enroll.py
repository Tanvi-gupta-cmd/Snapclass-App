import streamlit as st

from src.database.config import supabase
from src.database.db import enroll_student_to_subject


@st.dialog("Enroll in Subject")
def enroll_dialog():

    subject_code = st.text_input(
        "Enter Subject Code",
        placeholder="e.g. DSA101"
    )

    if st.button("Enroll", type="primary", width="stretch"):

        if not subject_code:
            st.warning("Please enter subject code.")
            return

        response = (
            supabase
            .table("subjects")
            .select("subject_id, name, subject_code, section")
            .eq("subject_code", subject_code.strip())
            .execute()
        )

        if not response.data:
            st.error("Subject Code not found!")
            return

        subject = response.data[0]

        student_id = st.session_state.student_data["student_id"]

        check = (
            supabase
            .table("subject_students")
            .select("*")
            .eq("subject_id", subject["subject_id"])
            .eq("student_id", student_id)
            .execute()
        )

        if check.data:
            st.info("You are already enrolled in this subject.")
            return

        enroll_student_to_subject(
            student_id,
            subject["subject_id"]
        )

        st.success(
            f"Successfully enrolled in {subject['name']}!"
        )

        st.rerun()

    if st.button("Close"):
        st.rerun()