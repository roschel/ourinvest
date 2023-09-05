import json

from fastapi import APIRouter, UploadFile

from model.models import DocOut, DocIn
from service.service import PeopleService


class Controller:

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(
            path="/file",
            endpoint=self.run_by_file,
            methods=["POST"]
        )
        self.router.add_api_route(
            path="/body",
            endpoint=self.run_by_request_body,
            methods=["POST"],
            response_model=DocOut
        )

    async def run_by_file(self, file: UploadFile):
        """
        Process the client's operations by json file
        """
        return PeopleService(DocIn(**json.load(file.file))).calculate()

    async def run_by_request_body(self, body: DocIn):
        """
        Process the client's operations by request body
        """
        return PeopleService(body).calculate()
