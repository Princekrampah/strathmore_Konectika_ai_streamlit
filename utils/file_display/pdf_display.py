import base64


def displayPDF(file, st):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
