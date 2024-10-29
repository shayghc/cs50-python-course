import sys
from os.path import splitext
from PIL import Image, ImageOps

# Constants
VALID_EXTENSIONS = {".jpg", ".jpeg", ".png"}
DEFAULT_SHIRT_IMAGE = "shirt.png"

def main():
    # Validate command-line arguments
    input_image_path, output_image_path = validate_command_line_arguments(sys.argv)

    try:
        muppet = load_image(input_image_path)
        shirt = load_image(DEFAULT_SHIRT_IMAGE)
    except FileNotFoundError as e:
        sys.exit(f"Error: {e}")

    muppet = overlay_images(muppet, shirt)
    muppet.save(output_image_path)

def validate_command_line_arguments(args):
    if len(args) != 3:
        sys.exit("Error: Please provide exactly two command-line arguments: input image and output image.")
    
    input_ext = splitext(args[1])[1].lower()
    output_ext = splitext(args[2])[1].lower()
    
    if not is_valid_extension(input_ext) or not is_valid_extension(output_ext):
        sys.exit("Error: Valid file extensions are .jpg, .jpeg, and .png.")
    
    if input_ext != output_ext:
        sys.exit("Error: Input and output files must have the same extension.")

    return args[1], args[2]

def is_valid_extension(extension):
    return extension in VALID_EXTENSIONS

def load_image(image_path):
    """Load an image and return it."""
    return Image.open(image_path)

def overlay_images(muppet, shirt):
    """Resize and overlay the shirt image on the muppet image."""
    resized_muppet = ImageOps.fit(muppet, shirt.size)
    resized_muppet.paste(shirt, (0, 0), shirt)
    return resized_muppet

if __name__ == "__main__":
    main()
