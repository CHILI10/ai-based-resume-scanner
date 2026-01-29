
import streamlit as st
import tempfile
import os
from resume_scanner import process_resume

st.set_page_config(
    page_title="AI Resume Scanner",
    page_icon="📄"
)

st.title("AI-Based Resume Scanner")
st.write("Upload a resume PDF or DOCX to extract details.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    file_extension = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp:
         temp.write(uploaded_file.read())
         temp_path = temp.name

   


    with st.spinner("Scanning resume..."):
        result = process_resume(temp_path)

    st.success("Resume scanned successfully!")

    st.subheader("Extracted Information")

    if result is not None:
        st.subheader("Extracted Information")

        st.write("👤 Name:", result.get("Name", "Not Found"))
        st.write("📧 Email:", result.get("Email", "Not Found"))
        st.write("📞 Phone:", result.get("Phone", "Not Found"))
        st.write("🛠 Skills:", result.get("Skills", "Not Found"))
        skills = result.get("Skills", [])
        st.markdown("### 🛠 Skills")
        if skills and skills != "Not Found":
             cols = st.columns(3)
             for idx, skill in enumerate(skills):
                 cols[idx % 3].markdown(
                     f"""
                     <div style="
                        padding:8px 12px;
                        margin:6px;
                        background-color:#262730;
                        border-radius:8px;
                        text-align:center;
                        font-weight:500;"> 
                        {skill}
                     </div>
                     """,
                     unsafe_allow_html=True   
                )   
        else: 
             st.write("Not Found")          

    else:
        st.error("Resume processing failed.")

    
        
    
   

