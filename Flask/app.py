import imp
import json
from flask import Flask, jsonify
from flask_cors import CORS
from config.db_connector import Database
from api.testBoard import testBoard
 
app = Flask(__name__)
CORS(app) #Cross-Origin Resource Sharing) 모든 요청에 대해 cors를 적용한다는 의미
#동일 출처 정책(Same-origin policy)에 따라,
#다른 호스트(ip및 포트가 다른)에서 리소스에 접근할 수 없도록 함.
#CORS는 교차 출처 리소스 공유(cors)를 처리하기 위한 패키지

#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#/api/로 들어오는 모든 요청에 대해서만 cors를 적용한다는 의미

db_testBoard = testBoard()

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api/board/')
#@cross_origin() #해당 요청에 대해서만 cors를 적용한다는 의미
def getBoardList():
    print('넘어옴')
    
    result = db_testBoard.getTestBoardList()

    print(result)
    data = {"result_code": "success", "result_data": result}
    return jsonify(data)    

app.run(debug=True)