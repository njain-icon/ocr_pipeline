"""
Routes for OCR Server
"""

from fastapi.responses import PlainTextResponse
from ocr_pipeline.app.api.v1 import APIv1

# Main API v1 router instance
api_v1_router_instance = APIv1(prefix="/api/v1")

api_v1_router_instance.router.add_api_route(
    "/ocr",
    APIv1.extract_text,
    methods=["POST"],
    response_model=dict,
    response_model_exclude_none=True,
)

api_v1_router_instance.router.add_api_route(
    "/health", APIv1.health, methods=["GET"], response_class=PlainTextResponse
)
