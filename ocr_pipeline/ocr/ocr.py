from __future__ import annotations

from typing import Dict, Optional, Tuple, Any

# Note: legacy get_entities not used in YAML-driven v2 aggregation
from ocr_pipeline.log import get_logger
from paddleocr import PaddleOCR


logger = get_logger(__name__)


class TextExtraction:
    """
    Class for performing OCR on images and extracting text.
    """

    def __init__(self):
        self.paddle_obj = PaddleOCR(
                            use_doc_orientation_classify=False,
                            use_doc_unwarping=False,
                            use_textline_orientation=False,
                            return_word_box=True)
            

    
    
    def ocr_image(
        self, image_path: str
    ) -> Tuple[Dict, str]:
        """
        Perform OCR on the given image and extract text.
        Returns a tuple containing a dictionary of extracted bounding boxes and the full extracted text.
        """
        try:
            result = self.paddle_obj.predict(image_path)
            result_dict = result[0]
            rec_texts = result_dict.get('rec_texts', [])
            return result_dict, " ".join(rec_texts)
        except Exception as e:
            import traceback
            logger.error(f"Error during OCR processing:{traceback.format_exc()}")
            return {}, ""