# Meal Plan App Backend API Endpoints

This document describes the REST API endpoints provided by the backend FastAPI application.

## Ingredient Categories
- `GET /ingredient_categories/` — List all ingredient categories
- `GET /ingredient_categories/{category_id}` — Get a specific ingredient category by ID
- `POST /ingredient_categories/` — Create a new ingredient category
- `PUT /ingredient_categories/{category_id}` — Update an ingredient category
- `DELETE /ingredient_categories/{category_id}` — Delete an ingredient category

## Ingredients
- `GET /ingredients/` — List all ingredients
- `GET /ingredients/{ingredient_id}` — Get a specific ingredient by ID
- `POST /ingredients/` — Create a new ingredient
- `PUT /ingredients/{ingredient_id}` — Update an ingredient
- `DELETE /ingredients/{ingredient_id}` — Delete an ingredient

## Recipes
- `GET /recipes/` — List all recipes
- `GET /recipes/{recipe_id}` — Get a specific recipe by ID
- `POST /recipes/` — Create a new recipe
- `PUT /recipes/{recipe_id}` — Update a recipe
- `DELETE /recipes/{recipe_id}` — Delete a recipe

## Ingredient Specifics
- `GET /ingredient_specifics/` — List all ingredient specifics
- `GET /ingredient_specifics/{specific_id}` — Get a specific ingredient-specific entry by ID
- `POST /ingredient_specifics/` — Create a new ingredient-specific entry
- `PUT /ingredient_specifics/{specific_id}` — Update an ingredient-specific entry
- `DELETE /ingredient_specifics/{specific_id}` — Delete an ingredient-specific entry

## Meal Plan
- `GET /meal_plan/` — List all meal plans
- `GET /meal_plan/{meal_plan_id}` — Get a specific meal plan by ID
- `POST /meal_plan/` — Create a new meal plan entry
- `PUT /meal_plan/{meal_plan_id}` — Update a meal plan entry
- `DELETE /meal_plan/{meal_plan_id}` — Delete a meal plan entry

## Special Endpoints
- `GET /meal_plan/today` — Get today's meal plan
- `GET /meal_plan/{days_ahead}` — Get the meal plan for today + n days

---
All endpoints accept and return JSON. For details on request/response formats, see the models in `backend/app/models.py`.
