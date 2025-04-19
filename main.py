from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from schemas import Recipe, RecipeCreate, Category, CategoryCreate, Tag, TagCreate
from crud import (create_recipe, get_recipes, get_recipe, update_recipe, delete_recipe,
                 create_category, get_category, update_category, delete_category,
                 create_tag, get_tag, update_tag, delete_tag)

app = FastAPI(title="Retseptlar Ombori")

Base.metadata.create_all(bind=engine)

# Рецепты
@app.post("/recipes/", response_model=Recipe)
def create_new_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return create_recipe(db, recipe)

@app.get("/recipes/", response_model=list[Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_recipes(db, skip=skip, limit=limit)

@app.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.put("/recipes/{recipe_id}", response_model=Recipe)
def update_existing_recipe(recipe_id: int, recipe: RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = update_recipe(db, recipe_id, recipe)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

@app.delete("/recipes/{recipe_id}", response_model=Recipe)
def delete_existing_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_recipe = delete_recipe(db, recipe_id)
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_recipe

# Категории
@app.post("/categories/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@app.get("/categories/", response_model=list[Category])
def read_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.put("/categories/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.delete("/categories/{category_id}", response_model=Category)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    db_category = delete_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# Теги
@app.post("/tags/", response_model=Tag)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@app.get("/tags/", response_model=list[Tag])
def read_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()

@app.get("/tags/{tag_id}", response_model=Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@app.put("/tags/{tag_id}", response_model=Tag)
def update_existing_tag(tag_id: int, tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = update_tag(db, tag_id, tag)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@app.delete("/tags/{tag_id}", response_model=Tag)
def delete_existing_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = delete_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag