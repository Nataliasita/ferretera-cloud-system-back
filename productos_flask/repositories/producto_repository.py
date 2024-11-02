from models.producto import Producto, db

class ProductoRepository:

    @staticmethod
   # def create_task(name, description):
   #     task = Task(name=name, description=description)
   #     db.session.add(task)
   #     db.session.commit()
   #     return task
    
    def list_all_productos():
        productos = Producto.query.all()
        return productos

        
    #@staticmethod
    #def update_task(name, description, oldid):
    #    task = Task.query.filter_by(id=oldid).first()
    #    task.name = name
    #    task.description = description
    #    db.session.commit()    
    
    #    return task             