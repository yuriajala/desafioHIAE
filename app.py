import os
from flask import Flask, render_template, request 
from werkzeug.utils import secure_filename
from pydicom import dcmread
import pandas as pd
#app start
app = Flask(__name__) 
#app configs
app.config['UPLOAD_EXTENSIONS'] = ['.dcm']
app.config['UPLOAD_PATH'] = 'uploads' 
#decorator to bring index page and check uploaded files                               
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html')
#decorator to call function when POST (upload button)    
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']   #request file
    filename = secure_filename(uploaded_file.filename) #secure filename against threats
    if filename != '':  #if filename is not empty, check extension
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in app.config['UPLOAD_EXTENSIONS']: #if extension is valid return error page
            return render_template('index.html', output = 'Invalid file')
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename)) #otherwise save file and get full path
        file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        try:    #try to read the file to check if it is a valid DICOM
            dicom_image = dcmread(file_path)
            dicom_panda = pd.DataFrame(data=dicom_image) #convert the header into a pandas dataframe
        except:
            return render_template('index.html', output = 'Invalid file') #if not readable return error page
    return render_template('index.html', output = dicom_panda.to_html()) #otherwise display the header as HTML pandas dataframe

#Create the main driver function
if __name__ == '__main__':
#call the run method
    app.run(host='0.0.0.0', port=80)