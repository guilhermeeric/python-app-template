from flask import jsonify
from flask_restful import Resource

class HelloWorld(Resource):
  def hello_world(self, name):
    return jsonify('Hello, ' + name)
