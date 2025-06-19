import numpy as np

def read_image(image_path: str) -> np.ndarray:
    """
    Reads an image from the specified file path using OpenCV.
    Args:
        image_path (str): The path to the image file to be loaded.
    Raises:
        ValueError: If the image cannot be loaded from the given path.
    Returns:
        np.ndarray: The loaded image as a NumPy array.
    """