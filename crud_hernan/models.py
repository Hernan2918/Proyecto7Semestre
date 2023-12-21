from database import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date


class Registros(Database):
    __tablename__= 'mensaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    modelo = Column(String(10))
    costo = Column(String(50))
    cantidad = Column(String(100))
    


# def deleteregistro(personaid):
#     persona = get_Persona(personaid)

#     db_session.delete(persona)
#     db_session.commit()

