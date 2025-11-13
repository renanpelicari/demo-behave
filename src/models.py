from pydantic import BaseModel
from uuid import UUID

class MovieModel(BaseModel):
    id: UUID
    name: str

class CreateMovieModel(BaseModel):
    name: str

class BookModel(BaseModel):
    id: UUID
    name: str

class CreateBookModel(BaseModel):
    name: str