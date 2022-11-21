from fastapi import APIRouter, status, Request
from routers.schemas import MessageSchema
from services.functions import QueueRabbit
from fastapi.encoders import jsonable_encoder

_QueueRabbit = QueueRabbit()
router = APIRouter(prefix="/main", tags=["Main"])

@router.post("/pub-message", status_code = status.HTTP_200_OK)
def health_check(payload: MessageSchema):
   
   return _QueueRabbit.sendMessage(jsonable_encoder(payload))
