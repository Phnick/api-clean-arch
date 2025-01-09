from fastapi import FastAPI
from main.routers import routers_users
from main.routers import routers_users2


app = FastAPI()
app.include_router(routers_users.router)
app.include_router(routers_users2.router)
