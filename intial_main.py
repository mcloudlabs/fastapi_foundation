from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id':1, 'todo_name':'Sports', 'todo_description':'Play football'},
    {'todo_id':2, 'todo_name':'Study', 'todo_description':'Read books'},
    {'todo_id':3, 'todo_name':'Work', 'todo_description':'Complete project'},
    {'todo_id':4, 'todo_name':'Shopping', 'todo_description':'Buy groceries'},
    {'todo_id':5, 'todo_name':'Exercise', 'todo_description':'Go to the gym'},
]

# GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD

@api.get("/")
def index():
    return {"message": "Hello, World!"}

#Provide the todo_id as a path parameter eg: http://localhost:8000/todos/3



@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'Result': todo}
    return {"error": "Todo not found"}, 404

#Provide the todo_id as a query parameter eg: http://localhost:8000/todos?first_n=3
@api.get("/todos")
def get_todo_query(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return {'Result': all_todos}

@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(existing_todo['todo_id'] for existing_todo in all_todos) + 1

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)
    return new_todo

@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_description'] = updated_todo['todo_description']
            return todo
    return {"error": "Todo not found"}, 404

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return {"message": "Todo deleted successfully", "deleted_todo": deleted_todo}
    return {"error": "Todo not found"}, 404

        