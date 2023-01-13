from flask import Blueprint

blueprint = Blueprint(
    'profiles',
    __name__,
    url_prefix='/profiles', template_folder='templates', static_folder='static'
)