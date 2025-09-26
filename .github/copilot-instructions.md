---
applyTo: "**"
---
# Project Context
I want to create a locally hosted Meal Plan App, hosted on a Raspberry Pi Zero on my local network and accessible with a web browser, and also viewable from a mounted eInk screen. I want to deploy it using Docker. I want to use the Model View Controller paradigm.

# Model and Controller context
Starting with the Model and Controller parts, I want to set up a series of databases, accessible through a REST API. I would like to use SQLite as the database technology, SQLAlchemy as the ORM, FastAPI as the REST API endpoints, and Python for any surrounding functions. 

## Database schemas
Inside /backend/schemas are csv tables describing the schemas for the five databases required: 'recipes', 'ingredients', 'ingredient_categories', 'ingredient_specifics' and 'meal_plan'.

These are related; for example, each recipe is a row in the 'recipes' table, each ingredient is a row in the 'ingredients' table, and ingredients are associated to a given recipe in the 'ingredient_specifics' table. Ingredients are categorised as per the 'ingredient_categories' table as a lookup.

## API endpoints
The API endpoints should allow for CRUD operations on each of the five databases, and also some additional endpoints to allow for more complex operations, including:
- return today's meal plan (from the 'meal_plan' table)
- return today+n's meal plan (from the 'meal_plan' table)

# View context
[to be added later]

## Web application View
[to be added later]

## eInk View
[to be added later]