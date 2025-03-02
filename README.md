# public
# introduction
to_clean_photos.py can traverse SOURCE_DIR = "D:\\photo" , read the year taken from the photos meta data, and add to a folder named by the year under DEST_DIR = "C:\\data\\organized_photos".

# notes
DUPLICATE_DIR = os.path.join(DEST_DIR, "Duplicates")
BLURRY_DIR = os.path.join(DEST_DIR, "Blurry")
BLUR_THRESHOLD = 100  # Adjust as needed

Duplicate photos and blurry photos detection are removed because:
## not so many photos are blur.
## no duplicate photos after organization.
if a photo was put into 2 different folder, then the 2 copies will be in the same folder (name by the year). Since the 2 photos most likely use the same file name, there is no duplication any more.

# TODOs:
# To test iphone photos
# To include video files.



