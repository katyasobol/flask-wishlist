from flask import Blueprint

blueprint = Blueprint(
    'posts',
    __name__,
    url_prefix='/posts', template_folder='templates', static_folder='static'
)