"""
This is entry point for OCR
"""

import argparse
import os
import warnings

from tqdm import tqdm

from ocr_pipeline.app.config.config import (
    load_config,
    var_server_config,
    var_server_config_dict,
)
from importlib.metadata import PackageNotFoundError, version

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)



def start():
    """Entry point for ocr-server."""

    # For loading config file details
    parser = argparse.ArgumentParser(description="OCR  CLI")
    parser.add_argument("-c", "--config", type=str, help="config file path")
    parser.add_argument(
        "-v", "--version", action="store_true", help="display the version"
    )
    args = parser.parse_args()
    if args.version:
        print("OCR Server version")
        exit(0)

    path = args.config
    if path is not None and not os.path.exists(path):
        raise FileNotFoundError(
            f"'--config' was passed but config file '{path}' does not exist."
        )

    config_details, server_config = load_config(path)
    p_bar = tqdm(range(10))
    var_server_config_dict.set(config_details)
    var_server_config.set(server_config)
    server_start(config_details, p_bar)




def server_start(config: dict, p_bar: tqdm):
    """Start server."""
    p_bar.write(f"OCR service starting ...")

    # Starting Uvicorn Service Using config details
    from ocr_pipeline.app.config.service import Service

    p_bar.update(1)
    svc = Service(config_details=config)
    p_bar.update(2)
    p_bar.close()
    svc.start()
    print("OCR server stopped. BYE!")


if __name__ == "__main__":
    start()
