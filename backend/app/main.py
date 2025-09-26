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

# INGREDIENT CRUD
@app.get("/ingredients/")
def read_ingredients(db=Depends(get_db)):
    return db.query(Ingredient).all()

@app.get("/ingredients/{ingredient_id}")
def read_ingredient(ingredient_id: int, db=Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@app.post("/ingredients/")
def create_ingredient(ingredient: dict, db=Depends(get_db)):
    new_ingredient = Ingredient(**ingredient)
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

@app.put("/ingredients/{ingredient_id}")
def update_ingredient(ingredient_id: int, ingredient: dict, db=Depends(get_db)):
    db_ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    for key, value in ingredient.items():
        setattr(db_ingredient, key, value)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

@app.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db=Depends(get_db)):
    db_ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db.delete(db_ingredient)
    db.commit()
    return {"detail": "Deleted"}

# RECIPE CRUD
@app.get("/recipes/")
def read_recipes(db=Depends(get_db)):
    return db.query(Recipe).all()

@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int, db=Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.post("/recipes/")
def create_recipe(recipe: dict, db=Depends(get_db)):
    new_recipe = Recipe(**recipe)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: dict, db=Depends(get_db)):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in recipe.items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db=Depends(get_db)):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
    return {"detail": "Deleted"}

# INGREDIENT SPECIFIC CRUD
@app.get("/ingredient_specifics/")
def read_ingredient_specifics(db=Depends(get_db)):
    return db.query(IngredientSpecific).all()

@app.get("/ingredient_specifics/{specific_id}")
def read_ingredient_specific(specific_id: int, db=Depends(get_db)):
    specific = db.query(IngredientSpecific).filter(IngredientSpecific.id == specific_id).first()
    if not specific:
        raise HTTPException(status_code=404, detail="IngredientSpecific not found")
    return specific

@app.post("/ingredient_specifics/")
def create_ingredient_specific(specific: dict, db=Depends(get_db)):
    new_specific = IngredientSpecific(**specific)
    db.add(new_specific)
    db.commit()
    db.refresh(new_specific)
    return new_specific

@app.put("/ingredient_specifics/{specific_id}")
def update_ingredient_specific(specific_id: int, specific: dict, db=Depends(get_db)):
    db_specific = db.query(IngredientSpecific).filter(IngredientSpecific.id == specific_id).first()
    if not db_specific:
        raise HTTPException(status_code=404, detail="IngredientSpecific not found")
    for key, value in specific.items():
        setattr(db_specific, key, value)
    db.commit()
    db.refresh(db_specific)
    return db_specific

@app.delete("/ingredient_specifics/{specific_id}")
def delete_ingredient_specific(specific_id: int, db=Depends(get_db)):
    db_specific = db.query(IngredientSpecific).filter(IngredientSpecific.id == specific_id).first()
    if not db_specific:
        raise HTTPException(status_code=404, detail="IngredientSpecific not found")
    db.delete(db_specific)
    db.commit()
    return {"detail": "Deleted"}

# MEAL PLAN CRUD
@app.get("/meal_plan/")
def read_meal_plans(db=Depends(get_db)):
    return db.query(MealPlan).all()

@app.get("/meal_plan/{meal_plan_id}")
def read_meal_plan(meal_plan_id: int, db=Depends(get_db)):
    meal_plan = db.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
    if not meal_plan:
        raise HTTPException(status_code=404, detail="MealPlan not found")
    return meal_plan

@app.post("/meal_plan/")
def create_meal_plan(meal_plan: dict, db=Depends(get_db)):
    new_meal_plan = MealPlan(**meal_plan)
    db.add(new_meal_plan)
    db.commit()
    db.refresh(new_meal_plan)
    return new_meal_plan

@app.put("/meal_plan/{meal_plan_id}")
def update_meal_plan(meal_plan_id: int, meal_plan: dict, db=Depends(get_db)):
    db_meal_plan = db.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
    if not db_meal_plan:
        raise HTTPException(status_code=404, detail="MealPlan not found")
    for key, value in meal_plan.items():
        setattr(db_meal_plan, key, value)
    db.commit()
    db.refresh(db_meal_plan)
    return db_meal_plan

@app.delete("/meal_plan/{meal_plan_id}")
def delete_meal_plan(meal_plan_id: int, db=Depends(get_db)):
    db_meal_plan = db.query(MealPlan).filter(MealPlan.id == meal_plan_id).first()
    if not db_meal_plan:
        raise HTTPException(status_code=404, detail="MealPlan not found")
    db.delete(db_meal_plan)
    db.commit()
    return {"detail": "Deleted"}

# Meal plan custom function endpoints
@app.get("/meal_plan/today")
def get_today_meal_plan(db=Depends(get_db)):
    today = datetime.date.today()
    return db.query(MealPlan).filter(MealPlan.date == today).all()

@app.get("/meal_plan/{days_ahead}")
def get_meal_plan_days_ahead(days_ahead: int, db=Depends(get_db)):
    target_date = datetime.date.today() + datetime.timedelta(days=days_ahead)
    return db.query(MealPlan).filter(MealPlan.date == target_date).all()
