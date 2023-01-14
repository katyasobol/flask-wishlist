import os
from flask_migrate import Migrate
from sys import exit
from flask import render_template

from app.config import config_dict
from app import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Недопустимый <config_mode>. Ожидаемые значения [Debug, Production]')

app = create_app(app_config)
Migrate(app, db)
    
if DEBUG:
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('layout/index.html')

if __name__ == "__main__":
    app.run()