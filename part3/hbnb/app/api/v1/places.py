from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

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

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String(description='List of amenities'))
})


place_response_model = api.model('PlaceResponse',
    place_model.clone('PlaceResponse', {
        'owner': fields.Nested(user_model, description='Owner of the place'),
        'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
        'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
    })
)


@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created', place_response_model)
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        current_user = get_jwt_identity()
        place_data = api.payload
        owner = facade.get_user(current_user['id'])
        if owner:
            place_data['owner'] = owner
        else:
            return {'error': 'Owner not found'}, 404

        list_amenities = []  # Cambiado a lista vacía
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
                    {'id': amenity.id, 'name': amenity.name}
                    for amenity in list_amenities  # Usar list_amenities
                ]
            }, 201
            
        except ValueError as e:
            return {"error": str(e)}, 400


    @api.response(200, 'List of places retrieved successfully', [place_response_model])
    def get(self):
        """Retrieve a list of all places"""
        list_places = facade.get_all_places()
        return marshal(list_places, place_response_model), 200

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
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        scheme = {
            'title': {'type': 'string'}, 
            'description': {'type': 'string'}, 
            'price': {'type': 'float'}, 
            'latitude': {'type': 'float'}, 
            'longitude': {'type': 'float'},
            'owner_id': {'type': 'string'}
            }
        
        val = Validator(scheme)
        place_data = api.payload
        place = facade.get_place(place_id)
        current_user = get_jwt_identity()
        if current_user is not place.owner or current_user is not is_admin :
            return {'error': "Unauthorized action"}, 403
        else:
            if not place:
                return {'error': 'Place not found'}, 404
            else:
                facade.update_place(place_id, place_data)
                return {"message": "Place updated successfully"}, 200

    @api.response(200, 'Place deleted successfully')
    @api.response(404, 'Place not found')
    @jwt_required()
    def delete(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}
        current_user = get_jwt_identity()
        is_admin = current_user.get('is_admin')
        if is_admin or current_user['id'] == place['user_id']:
            facade.delete_place(place_id)
            return {'message': 'Place deleted succesfully'}, 201
        return {'error': 'Permission denied'}, 403

        