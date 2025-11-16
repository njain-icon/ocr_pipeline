from fastapi import APIRouter, Request
from ocr_pipeline.app.models.models import ReqOCR
from ocr_pipeline.app.service.ocr_service import OCRPipeline
from ocr_pipeline.log import get_logger


cls_obj = OCRPipeline()
logger = get_logger(__name__)

class APIv1:
    """
    Controller Class for all the api endpoints for App resource.
    """

    def __init__(self, prefix: str):
        self.router = APIRouter(prefix=prefix)

    @staticmethod
    def extract_text(data: ReqOCR):
        # "/ocr" API entrypoint
        response = cls_obj.process_request(data)
        return response

    @staticmethod
    def health(request: Request):
        return f"Ocr pipeline is running"
    
