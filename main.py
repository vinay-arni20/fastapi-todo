from fastapi import FastAPI, HTTPException
from models import Task

app = FastAPI()

# In-memory task list
tasks = []

@app.get("/")
def root():
    return {"message": "Todo List API 🚀"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added!", "task": task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            tasks[index] = updated_task
            return {"message": "Task updated!", "task": updated_task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, t in enumerate(tasks):
        if t.id == task_id:
            deleted = tasks.pop(index)
            return {"message": "Task deleted!", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")
