import io
import webbrowser
import flask
import PIL.Image
from os import getcwd
import base64

app = flask.Flask(import_name="FlaskUpload")
cam_width = 0
cam_height = 0


@app.route('/camSize', methods=['POST'])
def cam_size():
    global cam_width
    global cam_height
    cam_width = int(float(flask.request.args["width"]))
    cam_height = int(float(flask.request.args["height"]))
    print('Width', cam_width, '& Height', cam_height, 'Received Successfully.')
    return "OK"


@app.route('/', methods=['POST'])
def upload_file():
    global cam_width
    global cam_height
    file_to_upload = flask.request.files['media'].read()
    image = PIL.Image.frombytes(mode="RGBA",
                                size=(cam_width, cam_height),
                                data=file_to_upload)
    # image.save('out.png')

    print('File Uploaded Successfully.')

    # Convert again to bytes since the two formats seem to be different
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Then encode to base64
    im_base64 = base64.b64encode(img_byte_arr)

    # html_code = '<html><head><title>Displaying Uploaded Image</title></head><body><h1>Displaying Uploaded ' \
    #             'Image</h1><img src="out.png" alt = "Uploaded Image at the Flask Server"/></body></html>'
    html_code = '<html><head><meta http-equiv="refresh" content="1"><title>Displaying Uploaded ' \
                'Image</title></head><body><h1>Displaying Uploaded Image</h1><div><img src="data:;base64,' \
                '' + im_base64.decode() + '" alt = "Uploaded Image at the Flask Server"/></div></body></html>'
    
    html_url = getcwd() + '/test.html'
    f = open(html_url, 'w')
    f.write(html_code)
    f.close()
    webbrowser.open(html_url)
    return 'SUCCESS'


app.run(host="0.0.0.0", port=6666, debug=True)
