from fastapi import FastAPI
from controller.controller import Controller

app = FastAPI(
    title="API Ourinvest",
    description="API para contabilizar transações cambiais de entrada e saída"
)

route_controller = Controller()
app.include_router(route_controller.router)
