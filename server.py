import os
from slideRemover import delete_duplicate_slides
from flask import Flask, request, render_template, send_file
app = Flask (__name__)

@app.route('/')
def home():
    return render_template("index.html");


@app.route('/fileUpload', methods=['POST'])
def fileUpload():

    if "fileUpload" not in request.files:
        return "<h1> File couldn't be accessed </h1>"
    
    file = request.files['fileUpload']

    if file.filename == "" or file.filename =="./":
        return "<h1> No File Selected </h1>"

    uploaded_file_path = os.path.join("./", file.filename)
    file.save("./temp/" + uploaded_file_path)
    # file.save(uploaded_file_path + uploaded_file_path)

    modifiedFilePath = delete_duplicate_slides(uploaded_file_path)

    return send_file(modifiedFilePath, as_attachment=True, download_name="modified_" + uploaded_file_path[2:], mimetype="application/pdf")
