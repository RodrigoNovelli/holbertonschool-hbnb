from flask_restx import Namespace, Resource, fields
from app.models.user import User
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

user_response_model = api.model('UserResponse',{
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    })

@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        current_user = get_jwt_identity()
        email = user_data.get('email')

        if current_user.get('is_admin'):
            if facade.get_user_by_email(email):
                return {'error': 'Email already registered'}, 400
            
            try:
                new_user = facade.create_user(user_data)
                return {'id': new_user.id, 'messagge': 'User succesfully created'}, 201
            except ValueError as e:
                return {'error': str(e)}, 400
                
        return {'error': 'Admin privileges required'}, 403
    
@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        print('user data is {}'.format(user_data['email']))
        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email, 'password': new_user.password}, 201
    
@api.route('/<user_id>')
@api.response(201, 'User', user_response_model)
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @jwt_required()
    @api.expect(user_response_model)
    @api.response(200, 'User updated successfully', user_model)
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put (self, user_id, user_data):
        user_data = api.payload
    
        user = facade.get_user(user_id)
    
        if not user:
            return {'error': 'User not found'}, 404
    
        current_user = get_jwt_identity()
    
        if current_user['id'] != user.id:
            return {'error': 'Denied access'}, 400
    
        if "email" in user_data:
            return {'error': 'Cannot modify email'}, 400
    
        if "password" in user_data:
            return {'error': 'Cannot modify password'}, 400
    
        correct_data = {
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name")
        }
    
        facade.update_user(user_id, correct_data)
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.route('/users/<user_id>')
    class AdminUserResource(Resource):
        @jwt_required()
        def put(self, user_id):
            current_user = get_jwt_identity()
        
            # If 'is_admin' is part of the identity payload
            if not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403

            data = request.json
            email = data.get('email')

            if email:
                # Check if email is already in use
                existing_user = facade.get_user_by_email(email)
                if existing_user and existing_user.id != user_id:
                    return {'error': 'Email is already in use'}, 400
            
            user_data['email'] = email
            
            password = user_data.get('password')
            
            if password:
                new_password = user.hash_password(password)
                user_data['password'] = new_password
            
            facade.update_user(user_id, user_data)
            return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
