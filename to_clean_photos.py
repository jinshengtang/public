import os
import shutil
import hashlib
import imagehash
import cv2
from PIL import Image, ExifTags
from tqdm import tqdm

# Configure paths
SOURCE_DIR = "D:\\photo"  # Change this to your photos directory
DEST_DIR = "C:\\data\\organized_photos"


def get_image_year(image_path):
    """Extracts the year from EXIF metadata."""
    try:
        image = Image.open(image_path)
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                if ExifTags.TAGS.get(tag) == "DateTimeOriginal":
                    return value[:4]  # Extract the year
    except Exception as e:
        print(f"Error reading EXIF from {image_path}: {e}")
    return "Unknown"  # If no date found

def get_hash(image_path):
    """Generates a perceptual hash for an image."""
    try:
        image = Image.open(image_path)
        return imagehash.average_hash(image)
    except Exception as e:
        print(f"Error hashing {image_path}: {e}")
        return None

def organize_photos():
    """Main function to sort photos by year, remove duplicates, and filter blurry images."""
    os.makedirs(DEST_DIR, exist_ok=True)
    os.makedirs(DUPLICATE_DIR, exist_ok=True)
    os.makedirs(BLURRY_DIR, exist_ok=True)
    
    hashes = {}
    for root, _, files in os.walk(SOURCE_DIR):
        for file in tqdm(files, desc="Processing Photos"):
            if not file.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            
            file_path = os.path.join(root, file)
            year = get_image_year(file_path)
            target_dir = os.path.join(DEST_DIR, year)
            os.makedirs(target_dir, exist_ok=True)
            
            # Move photo to the appropriate folder
            shutil.move(file_path, os.path.join(target_dir, file))
    
    print("Sorting complete!")

if __name__ == "__main__":
    organize_photos()
