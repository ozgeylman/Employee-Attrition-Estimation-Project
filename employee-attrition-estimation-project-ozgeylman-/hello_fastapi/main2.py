from fastapi import FastAPI
import uvicorn
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/whoami")
def whoami():
    return "I am batman"


if __name__ == "__main__":
    
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")