# API de Gestión de Usuarios - Google Cloud Function

Esta API proporciona métodos para gestionar usuarios en una base de datos Firestore utilizando Google Cloud Functions. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los usuarios.

## Endpoints

### 1. **Crear un Usuario**
- **Método**: `POST`
- **URL**: `/user_management`
- **Descripción**: Crea un nuevo usuario en la base de datos.
- **Cuerpo de la solicitud** (JSON):
    ```json
    {
        "nombre":"Juan Perez",
        "email":"juan.perez@example.com",
        "celular":"3252463656",
        "rol":"empleado almacen",
        "permisos":["crear_usuario", "realizar_ordenes"],
        "fecha_creacion": "2023-08-15T14:30:00Z",
        "estado":"activo"
    }
    ```
- **Respuesta**:
    - **Código 201 (Creado)**: Usuario creado exitosamente.
    - **Cuerpo de la respuesta**:
    ```json
    {
      "message": "Usuario agregado",
      "id": "USER_ID"
    }
    ```
---

## 2. **Consulta de Todos los Usuarios**
- **Método**: `GET`
- **URL**: `/user_management`
- **Descripción**: Obtiene todos los usuarios almacenados en la base de datos de Firestore.

### Respuesta Exitosa (Código 200)
Si la consulta se realiza correctamente y hay usuarios en la base de datos, la respuesta será un array de objetos, donde cada objeto representa un usuario.

#### Ejemplo de respuesta:

```json
[
{
    "id":"1",
    "nombre":"Juan Perez",
    "email":"juan.perez@example.com",
    "celular":"3252463656",
    "rol":"empleado almacen",
    "permisos":["crear_usuario", "realizar_ordenes"],
    "fecha_creacion": "2023-08-15T14:30:00Z",
    "estado":"activo"
},
{
    "id":"12112",
    "nombre":"Juan Perez",
    "email":"juan.perez@example.com",
    "celular":"3252463656",
    "rol":"empleado almacen",
    "permisos":["crear_usuario", "realizar_ordenes"],
    "fecha_creacion": "2023-08-15T14:30:00Z",
    "estado":"activo"
}
]
```
---
## 3. **Consulta de usuario por id**
- **Método**: `GET`
- **URL**: `/user_management?id=USER_ID`
- **Descripción**: Obtiene los detalles de un único usuario basado en el `id` proporcionado como parámetro en la URL.

### Parámetros de la URL
- **id** (string): El identificador único del usuario que se desea consultar.

### Respuesta Exitosa (Código 200)
Si el id proporcionado corresponde a un usuario existente en la base de datos, la respuesta será un objeto JSON con los detalles del usuario solicitado.

#### Ejemplo de respuesta:

    ```json
    {
        "nombre":"Juan Perez",
        "email":"juan.perez@example.com",
        "celular":"3252463656",
        "rol":"empleado almacen",
        "permisos":["crear_usuario", "realizar_ordenes"],
        "fecha_creacion": "2023-08-15T14:30:00Z",
        "estado":"activo"
    }
    ```

