from app import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    __tablename__ = "product"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False, default=0)
