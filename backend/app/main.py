from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, IngredientCategory, Ingredient, Recipe, IngredientSpecific, MealPlan
from .controllers import (
    get_all_ingredient_categories, get_ingredient_category, create_ingredient_category,
    update_ingredient_category, delete_ingredient_category
    # Add other CRUD imports here
)
import datetime

DATABASE_URL = "sqlite:///../mealplan.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ingredient_categories/")
def read_ingredient_categories(db=Depends(get_db)):
    return get_all_ingredient_categories(db)

@app.get("/ingredient_categories/{category_id}")
def read_ingredient_category(category_id: int, db=Depends(get_db)):
    category = get_ingredient_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# Add similar endpoints for Ingredient, Recipe, IngredientSpecific, MealPlan
# ...

# Placeholder for meal plan endpoints
@app.get("/meal_plan/today")
def get_today_meal_plan(db=Depends(get_db)):
    today = datetime.date.today()
    return db.query(MealPlan).filter(MealPlan.date == today).all()

@app.get("/meal_plan/{days_ahead}")
def get_meal_plan_days_ahead(days_ahead: int, db=Depends(get_db)):
    target_date = datetime.date.today() + datetime.timedelta(days=days_ahead)
    return db.query(MealPlan).filter(MealPlan.date == target_date).all()
