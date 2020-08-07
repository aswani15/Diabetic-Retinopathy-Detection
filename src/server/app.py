from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from sys import argv
from models.alexnet import AlexNetModel
import werkzeug
import time
from os import remove

app = Flask(__name__)
cors = CORS(app, resources={"*": {"origins": "*"}})
api = Api(app)
alexnet_model = AlexNetModel("models/alexnet_model.pth")
class Blindness(Resource):
    def get(self):
        return {'module' : 'Blindness detection', 'version': '1.0'}

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        imageFile = args['file']
        
        # generate a name
        fileName = "input_" + str(int(time.time())) + ".png"

        # generate file path
        filePath = "queue/" + fileName
        # save the file
        imageFile.save(filePath)
        
        output = alexnet_model.predict(filePath)

        # processing done...now remove the file
        remove(filePath)
        
        return {"output": output}

api.add_resource(Blindness, '/')

if __name__ == '__main__':
    app.run(debug=True, port=argv[1])