# backend/src/api/debris_routes.py
from flask_restful import Resource
from models.debris import SpaceDebris

class DebrisResource(Resource):
    def get(self):
        debris = SpaceDebris.query.all()
        return {'debris': [d.to_dict() for d in debris]}

api.add_resource(DebrisResource, '/api/debris')