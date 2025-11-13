import uuid

from fastapi import APIRouter, status, HTTPException
from uuid import UUID
from models import MovieModel, CreateMovieModel

router = APIRouter(prefix="/api/v1/movies", tags=["Movies"])

movie_list: list[MovieModel] = [
    MovieModel(id=UUID("12345678-9012-3456-7890-1234567890e1"), name="Central Station"),
    MovieModel(id=UUID("12345678-9012-3456-7890-1234567890e2"), name="Bacurau"),
    MovieModel(id=UUID("12345678-9012-3456-7890-1234567890e3"), name="City of God"),
    MovieModel(id=UUID("12345678-9012-3456-7890-1234567890e4"), name="A Dog's Will"),
]

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get all movies",
)
def find_all() -> list[MovieModel]:
    return movie_list

@router.get(
    "/{movie_id}",
    status_code=status.HTTP_200_OK,
    summary="Get a movie by ID",
)
def find_by_id(movie_id: UUID) -> MovieModel:
    for movie in movie_list:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new movie",
)
def create(movie: CreateMovieModel) -> MovieModel:
    movie_new = MovieModel(id=uuid.uuid4(), name=movie.name)
    movie_list.append(movie_new)
    return movie_new


@router.put(
    "/{movie_id}",
    status_code=status.HTTP_200_OK,
    summary="Update a movie",
)
def update(movie_id: UUID, movie: CreateMovieModel) -> MovieModel:
    for m in movie_list:
        if m.id == movie_id:
            m.name = movie.name
            return m
    raise HTTPException(status_code=404, detail="Movie not found")


@router.delete(
    "/{movie_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a movie",
)
def delete(movie_id: UUID) -> None:
    global movie_list
    if not any(m.id == movie_id for m in movie_list):
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_list = [m for m in movie_list if m.id != movie_id]