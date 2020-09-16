from flask import Flask, render_template, request, send_file
import os
import docx
import PyPDF2
import secrets

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        file = request.files['pdf']
        doc = docx.Document()
        pdfReader = PyPDF2.PdfFileReader(file.stream)
        for pgnum in range(1, pdfReader.numPages):
            pgObject = pdfReader.getPage(pgnum)
            pdfContent = pgObject.extractText()
            doc.add_paragraph(pdfContent)
        random_hex = secrets.token_hex(8)
        doc.save("static/docx/" + random_hex + ".docx")
        return send_file("static/docx/" + random_hex + ".docx")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)