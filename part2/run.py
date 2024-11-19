from app import create_app
from app.services import facade
from app.models.amenity import Amenity
from app.models.user import User

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)