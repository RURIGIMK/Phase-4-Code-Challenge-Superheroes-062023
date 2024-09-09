from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import User, Recipe

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class RecipeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
