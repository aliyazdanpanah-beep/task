from fastapi import APIRouter, Depends, HTTPException, Path, Query
from models import Project
from database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from pydantic import BaseModel, Field


router = APIRouter(
     prefix='/project',
     tags=['project']
)


def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()

db_dependency = Annotated[Session, Depends(get_db)]


class ProjectRequest(BaseModel) :
     title: str = Field(min_length=3)
     location: str = Field(min_length=3 ,max_length=100)
     start_date: int = Field(gt=0, lt=31)
     budget: int = Field(gt=0)


@router.get('/', status_code=status.HTTP_200_OK)
async def read_all_project(db: db_dependency):
    return db.query(Project).all()


@router.get('/{project_id}', status_code=status.HTTP_200_OK)
async def find_project_by_id(db: db_dependency, project_id: int = Path(gt=0)):     
     project_model = db.query(Project).filter(Project.id == project_id).first()
     if project_model is not None:
          return project_model
     raise HTTPException(status_code=404, detail='this Project is not exise')


@router.get('/get/location', status_code=status.HTTP_200_OK)
async def find_project_by_location(db: db_dependency, location: str = Query(min_length=1)):
    project_model = db.query(Project).filter(Project.location == location).all()
    if not project_model:
        raise HTTPException(status_code=404, detail='No project found in this location')
    return project_model


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_project(db: db_dependency, project_request: ProjectRequest):
     project_model = Project(**project_request.dict())

     db.add(project_model)
     db.commit()


@router.put('/update/{project_id}', status_code=status.HTTP_200_OK)
async def update_project(db: db_dependency,
                     project_request: ProjectRequest,
                     project_id: int = Path(gt=0)):
       
     project_model = db.query(Project).filter(Project.id == project_id).first()
     
     if project_model is None:
          raise HTTPException(status_code=404, detail='project not found')
     
     project_model.title = project_request.title
     project_model.location = project_request.location
     project_model.start_date = project_request.start_date
     project_model.budget = project_request.budget

     db.add(project_model)
     db.commit()

     
@router.delete('/delete/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(db: db_dependency, project_id: int = Path(gt=0)):
     project_model = db.query(Project).filter(Project.id == project_id).delete()
     if project_model is None:
          raise HTTPException(status_code=404, detail='project not found')
     db.query(Project).filter(Project.id == project_id).delete()
     db.commit()

