## STEP 1: BUILDING THE OCR PIPELINE


# Import libraries
import pytesseract
from PIL import Image
import cv2
import os

# Set tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Load and preprocess the image
def preprocess_image(image_path):

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}. Check the file path and integrity.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return binary


# Extracting text using tesseract
# Adding a function to extract text from the preprocessed image
def extract_text(image_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(processed_image)

    return text


def process_folder(folder_path):
    # Create a folder to save extracted text
    output_folder = os.path.join(folder_path, "extracted_text")
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            # Full path to the image
            image_path = os.path.join(folder_path, filename)

            # Extract text from the image
            extracted_text = extract_text(image_path)

            # Save the extracted text to a file
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            with open(output_file, "w") as file:
                file.write(extracted_text)

            print(f"Extracted text from {filename} and saved to {output_file}")


# Testing the OCR pipeline
if __name__ == "__main__":
    # Path to the folder containing images
    folder_path = "path_to_images_folder"  # Replace with the actual path to your image(s)

    # Calling the function process_folder to process all images in the folder
    process_folder(folder_path)







