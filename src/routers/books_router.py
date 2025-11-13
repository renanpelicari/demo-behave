import uuid

from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from models import BookModel, CreateBookModel

router = APIRouter(prefix="/api/v1/books", tags=["Books"])

book_list: list[BookModel] = [
    BookModel(id=UUID("12345678-9012-3456-7890-1234567890e1"), name="Dom Casmurro"),
    BookModel(id=UUID("12345678-9012-3456-7890-1234567890e2"), name="Barren Lives"),
    BookModel(id=UUID("12345678-9012-3456-7890-1234567890e3"), name="Captains of the Sands"),
]

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get all books",
)
def find_all() -> list[BookModel]:
    return book_list

@router.get(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Get a book by ID",
)
def find_by_id(book_id: UUID) -> BookModel:
    for book in book_list:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
)
def create(book: CreateBookModel) -> BookModel:
    book_new = BookModel(id=uuid.uuid4(), name=book.name)
    book_list.append(book_new)
    return book_new


@router.put(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Update a book",
)
def update(book_id: UUID, book: CreateBookModel) -> BookModel:
    for m in book_list:
        if m.id == book_id:
            m.name = book.name
            return m
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a book",
)
def delete(book_id: UUID) -> None:
    global book_list
    book_list = [m for m in book_list if m.id != book_list]