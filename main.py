from fastapi import FastAPI
from controllers import chat
import uvicorn

app = FastAPI()

# Include the chat router
app.include_router(chat.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastBot API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
