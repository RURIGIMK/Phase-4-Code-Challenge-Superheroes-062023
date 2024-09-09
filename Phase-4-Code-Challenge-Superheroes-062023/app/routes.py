from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Recipe
from app.schemas import UserSchema, RecipeSchema

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to my API!. I do really hope you will enjoy consuming it."

@main.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_schema = UserSchema()
    try:
        user = user_schema.load(data, session=db.session)
        db.session.add(user)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@main.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_schema = UserSchema()
    return jsonify(user_schema.dump(user))

@main.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    recipe_schema = RecipeSchema()
    try:
        recipe = recipe_schema.load(data, session=db.session)
        db.session.add(recipe)
        db.session.commit()
        return jsonify(recipe_schema.dump(recipe)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@main.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    recipe_schema = RecipeSchema()
    return jsonify(recipe_schema.dump(recipe))
