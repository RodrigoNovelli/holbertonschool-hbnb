#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields, marshal
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        review_data = api.payload
        place = facade.get_place(review_data['place_id'])
        if current_user == place.owner_id:
            return {'error': 'You have already reviewed this place'}, 400
        else:
            reviews = facade.get_reviews_by_place(review_data['place_id'])
            if any(current_user for review.user_id in reviews):
                return {'error': 'You have already reviewed this place'}, 400
            else:
                new_review = facade.create_review(review_data)
                return {
                    'id': new_review.id,
                    'text': new_review.text,
                    'rating': new_review.rating,
                    'user_id': new_review.user_id,
                    'place_id': new_review.place_id
                    }
                
        
    @api.response(201, 'List of reviews retrieved successfully')
    def get(self):
        all_reviews = facade.get_all_reviews()
        return marshal(all_reviews, review_model), 201
    
@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(201, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        else:
            return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user_id}, 201
        

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt_identity()
        """Update a review's information"""
        scheme = {
            'id': {'type': 'string'},
            'text': {'type': 'string'},
            'rating': {'type': 'int'},
            'user_id': {'type': 'string'},
            'place_id': {'type': 'string'}
            }
        review_data = api.payload
        validate = Validate(scheme)
        review = fecade.get_place(review.id)
        
        if current_user['id'] == review['user_id']:
            if not review:
                return {'error' ('Review not found')}, 404
            else:
                fecade.update_review(review_id, review_data)
                return {'message': 'Review updated succesfully'}, 201
        else:
            return {'error': "Unauthorized action."}, 403

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt_identity()
        """Delete a review"""
        if current_user['id'] == review['user_id']:
            facade.delete_review(review_id)
        else:
            return {'error': "Unauthorized action."}, 403

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        all_place_review = facade.get_reviews_by_place(place_id)
        if not all_place_review:
            return {'error': 'Reviews not found'}, 404
        else:
            return all_place_review
