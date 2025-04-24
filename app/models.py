from . import db

class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    percentage_change = db.Column(db.Float, nullable=False)
