from flask import request, jsonify
from flask_restful import Resource

from app import db
from model.product import Product


class ProductResource(Resource):
    def get(self):
        id = request.args.get("id")
        query = Product.query
        if id is not None:
            query = query.filter(Product.id == id)
        return {"products": query.all()}

    def post(self):
        name = request.json.get("name")
        quantity = request.json.get("quantity")
        product = Product(name=name, quantity=quantity)
        db.session.add(product)
        db.session.commit()
        return jsonify({"product": product})

    def put(self):
        id = request.json.get("id")
        quantity = request.json.get("quantity")
        product = Product.query.filter(Product.id == id).first()
        if product is None:
            return {"product": None}
        if isinstance(quantity, int):
            product.quantity = quantity
            db.session.add(product)
            db.session.commit()
        return jsonify({"product": product})

    def delete(self):
        id = request.json.get("id")
        product = Product.query.filter(Product.id == id).first()
        if product is not None:
            db.session.delete(product)
            db.session.commit()
        return {"product": product}
