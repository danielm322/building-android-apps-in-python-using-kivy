import flask
# import werkzeug
from werkzeug.utils import secure_filename

app = flask.Flask(import_name="PyCamL23_24")


@app.route('/', methods=['POST'])
def upload_file():
    file_to_upload = flask.request.files['media']
    file_to_upload.save(secure_filename(file_to_upload.filename))
    print('File Uploaded Successfully.')
    return 'SUCCESS'


# Run on 0.0.0.0 on local pc, then get the full address from the run output
app.run(host="0.0.0.0", port=6666, debug=True)
