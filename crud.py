from sqlalchemy.orm import Session
from models import Recipe, Category, Tag
from schemas import RecipeCreate, CategoryCreate, TagCreate

# Создание
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(
        name=recipe.name,
        description=recipe.description,
        ingredients=recipe.ingredients,
        instructions=recipe.instructions,
        category_id=recipe.category_id
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    if recipe.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(recipe.tag_ids)).all()
        db_recipe.tags = tags
        db.commit()
    return db_recipe

# Чтение
def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Recipe).offset(skip).limit(limit).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

# Обновление
def update_recipe(db: Session, recipe_id: int, recipe: RecipeCreate):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db_recipe.name = recipe.name
        db_recipe.description = recipe.description
        db_recipe.ingredients = recipe.ingredients
        db_recipe.instructions = recipe.instructions
        db_recipe.category_id = recipe.category_id
        if recipe.tag_ids:
            tags = db.query(Tag).filter(Tag.id.in_(recipe.tag_ids)).all()
            db_recipe.tags = tags
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)
    return db_category

def update_tag(db: Session, tag_id: int, tag: TagCreate):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag:
        db_tag.name = tag.name
        db.commit()
        db.refresh(db_tag)
    return db_tag

# Удаление
def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag