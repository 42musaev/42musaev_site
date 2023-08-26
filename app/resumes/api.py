from fastapi import APIRouter

route_resumes = APIRouter(prefix="/resumes", tags=["resumes"])


@route_resumes.get('/')
def get_resumes():
    return {"resumes": [{"resume": "1"}, {"resume": "2"}, {"resume": "3"}]}
