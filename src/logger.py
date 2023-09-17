import logging
import sys
from pathlib import Path
from datetime import datetime


def find_project_root(marker_file='src'):
    """
    Find the root path of the project based on the presence of a marker file.

    Args:
        marker_file (str, optional): The name of the marker file or directory. Default is 'README.md'.

    Returns:
        pathlib.Path: The root path of the project.
    """
    current_dir = Path.cwd()
    
    while not (current_dir / marker_file).is_dir():
        current_dir = current_dir.parent

    return current_dir


LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
logs_path = find_project_root(marker_file='src') / "logs"
logs_path.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = logs_path / LOG_FILE

logging.basicConfig(
    # filename=LOG_FILE_PATH, # 'stream' or 'filename' should not be specified together with 'handlers'
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlprojectLogger")