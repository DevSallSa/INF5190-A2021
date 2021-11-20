from shared import db, ma
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))

class SessionSchema(md.SQLAlchemyAutoSchema):
    class Meta:
        model = Session
        load_instance = True
