# Statement for enabling the development environment
import os
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))



# local host
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@123@localhost/treasure_hunt' #mysql://username:password@server/d

SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'connect_timeout': 15
    }
}

DATABASE_CONNECT_OPTIONS = {}
UPLOAD_FOLDER = "."
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
