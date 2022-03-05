from fastapi import APIRouter, Request, Depends, Response, encoders
from typing import List

from app.db.crud import get_users, get_user, create_user, edit_user, delete_user
from app.db.session import get_db

from app.db.schemas import UserCreate, UserEdit, User, UserOut

users_router = r = APIRouter()


@r.get(
    "/users",
    response_model=List[User],
    response_model_exclude_none=True,
)
async def users_list(
        response: Response,
        db=Depends(get_db),
):
    """
    Get all users
    """
    users = get_users(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(users)}"
    return users


@r.get(
    "/users/{user_id}",
    response_model=User,
    response_model_exclude_none=True,
)
async def user_details(
        request: Request,
        user_id: int,
        db=Depends(get_db),
):
    """
    Get any user details
    """
    user = get_user(db, user_id)
    return user
    # return encoders.jsonable_encoder(
    #     user, skip_defaults=True, exclude_none=True,
    # )


@r.post("/users", response_model=User, response_model_exclude_none=True)
async def user_create(
        request: Request,
        user: UserCreate,
        db=Depends(get_db),
):
    """
    Create a new user
    """
    return create_user(db, user)


@r.put(
    "/users/{user_id}", response_model=User, response_model_exclude_none=True
)
async def user_edit(
        request: Request,
        user_id: int,
        user: UserEdit,
        db=Depends(get_db),
):
    """
    Update existing user
    """
    return edit_user(db, user_id, user)


@r.delete(
    "/users/{user_id}", response_model=User, response_model_exclude_none=True
)
async def user_delete(
        request: Request,
        user_id: int,
        db=Depends(get_db),
):
    """
    Delete existing user
    """
    return delete_user(db, user_id)
