from flask import Flask, render_template ,request, send_from_directory,Response
from flask import jsonify
import time
import profilematch 
import detection
import json


app = Flask(__name__)
@app.route('/')
def hii():
    return '<h1> " this is my app"</h1>'
@app.route('/compareimages',methods=['POST'])
def hello():
    target = request.files['target']
    faces = request.files['face']
    result=profilematch.verification(target,faces)
    responses=[]
    print(result)
    json_contect={
                'result': str(result)           
                }
    responses.append(json_contect)
    python2json = json.dumps(responses)
    return app.response_class(python2json, content_type='application/json') 

if __name__ == "__main__":
    app.debug=True
    app.run()