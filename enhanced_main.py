from email.policy import HTTP
from fastapi import FastAPI
from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name : str = Field (..., min_length=3, max_length=512, description = 'Name of the todo')
    todo_description: str = Field (..., description='Description fo the todo')
    priority: Priority = Field (default=Priority.LOW, description='Ppriorirty of the todo')

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique Identifier of the todo")

class TodoUpdate (BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description = 'description of the todo')
    priority: Optional[Priority] = Field(None, description= 'Priority of the todo')

    

all_todos = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Play football', priority=Priority.LOW),
    Todo(todo_id=2, todo_name='Study', todo_description='Read books', priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name='Work', todo_description='Complete project', priority=Priority.HIGH),
    Todo(todo_id=4, todo_name='Shopping', todo_description='Buy groceries', priority=Priority.LOW),
    Todo(todo_id=5, todo_name='Exercise', todo_description='Go to the gym', priority=Priority.MEDIUM),
]


# GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD


@api.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    return {"error": "Todo not found"}, 404

#Provide the todo_id as a query parameter eg: http://localhost:8000/todos?first_n=3
@api.get("/todos")
def get_todo_query(first_n: int = None, response_model=List[Todo]):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(existing_todo.todo_id for existing_todo in all_todos) + 1

    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )

    all_todos.append(new_todo)
    return new_todo
    raise HTTPException(status_code=400, detail="Todo already exists")


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_description = updated_todo.todo_description
            todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@api.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")
        