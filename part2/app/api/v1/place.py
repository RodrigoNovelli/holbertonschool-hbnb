#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from app.models.user import User
from cerberus import Validator


api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        place_data = api.payload
        owner = facade.get_user(user_id)
        if owner:
            place_data['owner'] = owner
        else:
            return {'error': 'Owner not found'}, 404

        list_amenities = []
        amenity_id_list = place_data.get('amenities')
        if not amenity_id_list:
            return {'error': 'Amenity not found'}, 404
        for amenity_id in amenity_id_list:
            amenity = facade.get_amenity(amenity_id)
            if not amenity:
                return {'error': 'Amenity not found'}
            list_amenities.append(amenity)    
        place_data['amenities'] = list_amenities
        
        try:
            new_place = facade.create_place(place_data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner_id': new_place.owner.id,
                'amenities': [
                    {'id': amen.id, 'name': amen.name}
                    for amen in new_place.amenities
                ]
                    }, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        list_places = facade.get_all_places()
        return marshal(list_places, place_model), 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': {'id': place.owner.id,
                          'first_name': place.owner.first_name,
                          'last_name': place.owner.last_name,
                          'email': place.owner.email
                          }, 
                'amenities': [
                    {'id': amenity.id,'name': amenity.name}
                    for amenity in place.amenities
                    ]
                }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        scheme = {
            'title': {'type': 'string'}, 
            'description': {'type': 'string'}, 
            'price': {'type': 'float'}, 
            'latitude': {'type': 'float'}, 
            'longitude': {'type': 'float'},
            'owner_id': {'type': 'string'}
            }
        validate = Validator(scheme)
        place_data = api.payload
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        if validate.validate(place_data):
            facade.update_place(place_id, place_data)
            return {"message": "Place updated successfully"}, 200
        return "Invalidate data", 400
    