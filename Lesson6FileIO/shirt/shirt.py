import sys
from os.path import splitext
from PIL import Image, ImageOps

# Constants
VALID_EXTENSIONS = {".jpg", ".jpeg", ".png"}
DEFAULT_SHIRT_IMAGE = "shirt.png"

def main() -> None:
    """
    The main function orchestrates the image processing script. It validates command-line arguments,
    loads the muppet and shirt images, overlays the shirt on the muppet, and saves the resulting image.

    Parameters:
    None

    Returns:
    None

    Raises:
    SystemExit: If the command-line arguments are invalid or if the required files are not found.
    """
    # Validate command-line arguments
    input_image_path, output_image_path = validate_command_line_arguments(sys.argv)

    try:
        muppet = load_image(input_image_path)
        shirt = load_image(DEFAULT_SHIRT_IMAGE)
    except FileNotFoundError as e:
        sys.exit(f"Error: {e}")

    muppet = overlay_images(muppet, shirt)
    muppet.save(output_image_path)


def validate_command_line_arguments(args: List[str]) -> Tuple[str, str]:
    """
    Validate command-line arguments for the image processing script.

    The script expects exactly two command-line arguments: the input image path and the output image path.
    It checks if the input and output file extensions are valid and if they match.

    Parameters:
    args (list): A list of command-line arguments. The first argument is the script name, and the remaining arguments are the input and output image paths.

    Returns:
    tuple: A tuple containing the input image path and the output image path.

    Raises:
    SystemExit: If the command-line arguments are invalid.
    """
    if len(args) != 3:
        sys.exit("Error: Please provide exactly two command-line arguments: input image and output image.")

    input_ext = splitext(args[1])[1].lower()
    output_ext = splitext(args[2])[1].lower()

    if not is_valid_extension(input_ext) or not is_valid_extension(output_ext):
        sys.exit("Error: Valid file extensions are .jpg, .jpeg, and .png.")

    if input_ext != output_ext:
        sys.exit("Error: Input and output files must have the same extension.")

    return args[1], args[2]


def is_valid_extension(extension: str) -> bool:
    return extension in VALID_EXTENSIONS

def load_image(image_path: str) -> Image.Image:
    """Load an image and return it."""
    return Image.open(image_path)

def overlay_images(muppet: Image.Image, shirt: Image.Image) -> Image.Image:
    """
    Resize and overlay the shirt image on the muppet image.

    Parameters:
    muppet (PIL.Image): The original muppet image.
    shirt (PIL.Image): The shirt image to be overlaid on the muppet image.

    Returns:
    PIL.Image: The resized and overlaid muppet image with the shirt.
    """
    resized_muppet = ImageOps.fit(muppet, shirt.size)
    resized_muppet.paste(shirt, (0, 0), shirt)
    return resized_muppet


if __name__ == "__main__":
    main()
