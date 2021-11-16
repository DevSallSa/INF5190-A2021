from shared import db, ma
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    email = db.Column(db.String(100))
    salt = db.Column(db.String(32))
    hash = db.Column(db.String(128))

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'username', 'email')
