from flask import Blueprint, request, jsonify
from services.producto_service import ProductoService

producto_api = Blueprint('producto_api', __name__)

#@task_blueprint.route('/tasks', methods=['POST'])
#def create_task():

#    data = request.form
#    name = data.get('name')
#    description = data.get('description')

#    if not name:
#        return jsonify({'error': 'Name is required'}), 400

#    TaskService.create_task(name, description)
#    return redirect(url_for('tasks.index'))

@producto_api.route('/api/producto', methods=['GET'])
def list_all_productos_controller():
    productos =  ProductoService.list_all_productos()
    return jsonify(prods=[p.serialize() for p in productos] ), 200
    
#@task_blueprint.route('/update', methods=['POST'])
#def update_task():

#    data = request.form
#    id = data.get('id')    
#    name = data.get('newname')
#    description = data.get('newdescription')

#    if not name:
#        return jsonify({'error': 'Name is required'}), 400

#    TaskService.update_task(name, description, id)
#    return redirect(url_for('tasks.index'))  