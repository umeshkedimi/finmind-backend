from fastapi import FastAPI

app = FastAPI(
    title="FinMind - Personal Finance API",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to FinMind API"}

