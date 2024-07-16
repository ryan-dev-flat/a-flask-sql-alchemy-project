from config import db
from sqlalchemy_serializer import SerializerMixin

class Author(db.Model, SerializerMixin):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Author id={self.id} name={self.name}>'