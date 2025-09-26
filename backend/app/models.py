from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add other fields as per CSV schema

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('ingredient_categories.id'))
    category = relationship('IngredientCategory')
    # Add other fields as per CSV schema

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add other fields as per CSV schema

class IngredientSpecific(Base):
    __tablename__ = 'ingredient_specifics'
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(String)
    recipe = relationship('Recipe')
    ingredient = relationship('Ingredient')
    # Add other fields as per CSV schema

class MealPlan(Base):
    __tablename__ = 'meal_plan'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe')
    # Add other fields as per CSV schema
