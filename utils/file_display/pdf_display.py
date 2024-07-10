import base64

# /home/prince/Desktop/content/projects/strathmore_connectika/ai_section/streamlit_app/generated_html/generated_pdf.pdf
# /home/prince/Desktop/content/projects/strathmore_connectika/ai_section/streamlit_app/utils/file_display/pdf_display.py
# /home/prince/Desktop/content/projects/strathmore_connectika/ai_section/streamlit_app/1_🏴󠁲󠁯󠁣󠁶󠁿_app.py
def displayPDF(file, st):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
