from fastapi import FastAPI
from api import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="SalaryTracker")
origins = ["*"] #позволили всем сайтам обращаться к бэку
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],#все запросы
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


