from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from database import Database
from database import engine
from database import db_session

import models
from services import delete_persona
app = Flask(__name__)

Database.metadata.create_all(engine)

@app.get('/')
def home():
    return render_template("home.html")

@app.get('/crear')
def crear():
    return render_template("registro.html")

@app.get('/act/<id>/update')
def act(id):
    persona = db_session.query(models.Registros).get(id)
    return render_template("actualizar.html", persona=persona)

    

@app.get('/vista')
def inicio():
    personas = db_session.query(models.Registros).all()
    return render_template("vista.html", personas=personas)

@app.post('/registro')
def registro():
    _nombre = request.form['txtnombre']
    _modelo = request.form['txtmodelo']
    _costo = request.form['txtcosto']
    _cantidad = request.form['txtcantidad']
    

    nuevo_persona = models.Registros(
        nombre = _nombre,
        modelo = _modelo,
        costo = _costo,
        cantidad = _cantidad
    )
    db_session.add(nuevo_persona)
    db_session.commit()
    return redirect(url_for('inicio'))


@app.get('/eliminar/<id>/delete')
def eliminar(id):
    persona = db_session.query(models.Registros).get(id)

    db_session.delete(persona)
    db_session.commit()

    return redirect(url_for('inicio'))

@app.post('/actualizar/<id>/update')
def actualizar(id):
    persona = db_session.query(models.Registros).get(id)

    nuevo_id = request.form['id_a'] 
    nuevo_nombre = request.form['txtnombre_a']
    nuevo_modelo = request.form['txtmodelo_a']
    nuevo_costo = request.form['txtcosto_a']
    nuevo_cantidad = request.form['txtcantidad_a']
    
    

    persona.id = nuevo_id
    persona.nombre = nuevo_nombre
    persona.modelo = nuevo_modelo
    persona.costo = nuevo_costo
    persona.cantidad = nuevo_cantidad
    
    db_session.add(persona)
    db_session.commit()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
