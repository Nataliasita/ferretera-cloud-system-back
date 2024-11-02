from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):

    id_producto = db.Column(db.Integer, primary_key=True)
    id_proveedor = db.Column(db.Integer, nullable=False)
    id_marca = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.Text, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric, nullable=True)
    unidad_medida = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    
    def serialize(self):
        return {"id_producto": self.id_producto,
                "id_proveedor": self.id_proveedor,
                "id_marca": self.id_marca,
                "nombre": self.nombre,
                "descripcion": self.descripcion,
                "precio": self.precio,
                "unidad_medida": self.unidad_medida,
                "fecha_creacion": self.fecha_creacion                
                }
   
