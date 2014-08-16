from app import db
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    
    def __str__(self):
        return "name {}, email {}".format(self.username, self.email)
    
    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username
        }