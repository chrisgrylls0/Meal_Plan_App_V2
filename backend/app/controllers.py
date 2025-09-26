from sqlalchemy.orm import Session
from .models import IngredientCategory, Ingredient, Recipe, IngredientSpecific, MealPlan

# CRUD operations for each model
def get_all_ingredient_categories(db: Session):
    return db.query(IngredientCategory).all()

def get_ingredient_category(db: Session, category_id: int):
    return db.query(IngredientCategory).filter(IngredientCategory.id == category_id).first()

def create_ingredient_category(db: Session, category: IngredientCategory):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_ingredient_category(db: Session, category_id: int, new_data: dict):
    category = get_ingredient_category(db, category_id)
    for key, value in new_data.items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

def delete_ingredient_category(db: Session, category_id: int):
    category = get_ingredient_category(db, category_id)
    db.delete(category)
    db.commit()

# Repeat similar CRUD functions for Ingredient, Recipe, IngredientSpecific, MealPlan
# ...