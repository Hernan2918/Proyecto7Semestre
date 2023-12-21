from models import Registros
from database import db_session
from flask import render_template
import models


def get_persona(id):
    personas = db_session.query(models.Registros).all()
    return render_template("vista.html", personas=personas)

def delete_persona(id):
    persona = get_persona(id)
    db_session.delete(persona)
    db_session.commit()

    