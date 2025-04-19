from pydantic import BaseModel
from typing import List, Optional

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    category_id: int
    tag_ids: Optional[List[int]] = []

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    category: Category
    tags: List[Tag]
    class Config:
        orm_mode = True