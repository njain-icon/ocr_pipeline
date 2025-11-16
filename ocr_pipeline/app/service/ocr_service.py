"""
Module for text classification
"""


import traceback

from pydantic import ValidationError

from ocr_pipeline.app.models.models import ReqOCR
from ocr_pipeline.app.models.models import OCRJsonResponse
from ocr_pipeline.app.models.models import ResponseDataModel
from ocr_pipeline.ocr.ocr import TextExtraction
from ocr_pipeline.log import get_logger


logger = get_logger(__name__)
text_extraction_obj = TextExtraction()

class OCRPipeline:
    """
    Classification wrapper class for Entity and Semantic classification with anonymization
    """

    def process_request(self, request_data: ReqOCR) -> OCRJsonResponse:
        """
        Processes the user request for classification and returns a structured response.

        Returns:
            OCRResponse: The response object containing ocr results
        """
        try:
            response = ResponseDataModel(
                extracted_text=None,
                ocr_dict={}

            )

            response.ocr_dict, response.extracted_text = text_extraction_obj.ocr_image(
                request_data.imagePath
            )
            return response.model_dump(exclude_none=True)
        
        except ValidationError as e:
            logger.error(
                f"Validation error in Classification API process_request:{e}\n{traceback.format_exc()}"
            )
            return OCRJsonResponse.build(
                body={"error": f"Validation error: {e}"}, status_code=400
            )
        except Exception:


            logger.error(
                f"Error in OCR API process_request: {traceback.format_exc()}"
            )
            return OCRJsonResponse.build(
                body=response.model_dump(exclude_none=True), status_code=500
            )
