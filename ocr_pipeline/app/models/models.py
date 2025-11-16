from typing import Dict, Optional, Union
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field


class ResponseDataModel(BaseModel):
    extracted_text: Optional[str] = None
    ocr_dict: Optional[dict] = {}

class ReqOCR(BaseModel):
    imagePath: str

class OCRJsonResponse:
    """
    Response class for custom json response
    """

    @classmethod
    def build(
        cls,
        body: Optional[dict] = None,
        status_code: int = 200,
    ):
        return JSONResponse(status_code=status_code, content=jsonable_encoder(body))
