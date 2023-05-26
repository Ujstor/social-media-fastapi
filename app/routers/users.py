from .. import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. database import get_db
from .. import oauth2

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash password - user.password
    #todo ---> check if user exists
    user = db.query(models.User).filter(models.User.email == user.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with email {user.email} already exists")
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return user