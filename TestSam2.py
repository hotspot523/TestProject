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

@app.route('/directory/<dir>/files/<file_name>', methods=['GET','POST'])
def hello_file(dir, file_name):
    if request.method == 'POST':
        file=open("/home/user/Software/"+dir+"/"+file_name,'a')
        file.close()
        return dir+"/"+file_name
    else:
        file=open("/home/user/Software/"+dir+"/"+file_name,'r')
        return file.read()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
    
    
