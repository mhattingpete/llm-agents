import uvicorn
from fastapi import FastAPI

from src.routers import answer

app = FastAPI()
app.include_router(answer.router)


@app.get("/health")
def get_health() -> dict[str, str]:
    return {"Status": "Running"}


def main():
    uvicorn.run("app:app", log_level="debug")


if __name__ == "__main__":
    main()
