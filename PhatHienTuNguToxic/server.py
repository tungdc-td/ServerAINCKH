from flask import Flask 
from flask import jsonify
import json
import os.path
from flask import request    
app = Flask(__name__)


#Goi cac thu vien
#from TD_friend_recommendation_system import main
#from TD_face_recognition import run_image
#from TD_toxic_word_detection import demo
import demo1

@app.route('/toxicdetection/<text>',methods=['GET', 'POST'])
def detection(text):
    return demo1.detection(text)

if __name__ == '__main__':
        app.run(debug=True, host= '0.0.0.0', port='9999')
        #app.run()





























