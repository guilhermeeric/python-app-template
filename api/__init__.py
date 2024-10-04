from flask import jsonify
from flask_restful import Api, Resource
import config
from service.hello_world import hello_world

api = Api(prefix=config.API_PREFIX)

# data processing endpoint
api.add_resource(hello_world, '/hello_world')

