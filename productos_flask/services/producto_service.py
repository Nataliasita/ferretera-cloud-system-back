from repositories.producto_repository import ProductoRepository

class ProductoService:

    #@staticmethod
    #def create_task(name, description):
    #    return TaskRepository.create_task(name, description)
        
    @staticmethod
    def list_all_productos():
        return ProductoRepository.list_all_productos()        
        
    #@staticmethod
    #def update_task(name, description, id):
    #    return TaskRepository.update_task(name, description, id)        