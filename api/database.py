from api import db


class Database(db.Model):
    __tablename__ = 'database'
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer)

    def __repr__(self):
        return f'<Result{self.id, self.result}>'
