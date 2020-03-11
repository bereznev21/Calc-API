from api import db
from api.database import Database


def add_note(res):
    new_note = Database(result=int(res))
    db.session.add(new_note)
    db.session.commit()
    return {'expression_id': new_note.id}
