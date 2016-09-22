from flask import Flask, request, jsonify, json, Response
import os

app = Flask(__name__)

@app.route('/directory/<dir_name>', methods=['GET','POST'])
def hello_dir(dir_name):
    if request.method == 'POST':
        os.makedirs("/home/user/Software/"+dir_name)
        return dir_name + " : directory created successfully"
    else:
        d = os.listdir("/home/user/Software/"+dir_name)
        return Response(json.dumps(d),  mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
