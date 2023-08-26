from typing import List
from sqlmodel import SQLModel
from sqlmodel import Field
from sqlmodel import Relationship


class Language(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str


class ResumeLanguage(SQLModel, table=True):
    __tablename__ = "languages_resumes"
    resume_id: int = Field(primary_key=True)
    language_id: int = Field(primary_key=True)


class Resume(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    body: str
    created_at: str

    languages: List[Language] = Relationship(back_populates="resumes")
