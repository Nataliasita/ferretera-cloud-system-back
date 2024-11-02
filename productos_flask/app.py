from flask import Flask
from models.producto import db
from controllers.producto_controller import *

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://andres:arenas_20241101@34.48.77.79/productos'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://andres:andres@192.168.20.75:3306/productosdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + ':3306/' + DB_NAME
db.init_app(app)

app.register_blueprint(producto_api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
    
    
