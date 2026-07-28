import cv2
import os

print("="*70)
print("            ENTERPRISE EMPLOYEE IMAGE PROCESSING SYSTEM")
print("="*70)

#------------------------------------------------------------------
# File Path Configuration
#------------------------------------------------------------------
image_path = r"C:\Users\ADMIN\OneDrive\Pictures\Camera Roll\WhatsApp Image 2026-07-17 at 6.33.23 PM.jpeg"

#------------------------------------------------------------------
# Check Image Existence
#------------------------------------------------------------------
if not os.path.exists(image_path):
    print("\nEmployee image not found")
    print("Please check if the file path is correct or if the image exists.")
    exit()

#-------------------------------------------------------------------
# Read Image
#-------------------------------------------------------------------
image = cv2.imread(image_path)
print("\nImage loaded successfully")

#-------------------------------------------------------------------
# Image Properties Extraction
#-------------------------------------------------------------------
height = image.shape[0]
width = image.shape[1]
channel = image.shape[2]

print("\nImage Information")
print("----------------------------------------")
print("Height  :", height)
print("Width   :", width)
print("Channel :", channel)

#-------------------------------------------------------------------
# Resize Image
#-------------------------------------------------------------------
resized_image = cv2.resize(image, (500, 700))
print("\nImage Resized to 500x700")

#-----------------------------------------------------------------
# Convert to Gray
#------------------------------------------------------------------
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
print("Converted to gray")

#------------------------------------------------------------------
# Gaussian Blur Noise Reduction
#-------------------------------------------------------------------
blur = cv2.GaussianBlur(gray, (7, 7), 0)
print("Noise removed")

#------------------------------------------------------------------
# Canny Edge Detection
#------------------------------------------------------------------
edge = cv2.Canny(blur, 50, 150)
print("Edges Detected")

#-----------------------------------------------------------------
# Rotate Image Clockwise
#-----------------------------------------------------------------
rotate = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
print("Image Rotated")

#--------------------------------------------------------------------
# Flip Image Horizontally
#---------------------------------------------------------------------
flip = cv2.flip(resized_image, 1)
print("Image Flipped")

#-------------------------------------------------------------------
# Create Output Folder
#-------------------------------------------------------------------
output_folder = "Output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("\nCreated folder: 'Output'")

#-------------------------------------------------------------------
# Save Processed Images
#-------------------------------------------------------------------
cv2.imwrite(os.path.join(output_folder, "1_resized.jpg"), resized_image)
cv2.imwrite(os.path.join(output_folder, "2_gray.jpg"), gray)
cv2.imwrite(os.path.join(output_folder, "3_blur.jpg"), blur)
cv2.imwrite(os.path.join(output_folder, "4_edge.jpg"), edge)
cv2.imwrite(os.path.join(output_folder, "5_rotate.jpg"), rotate)
cv2.imwrite(os.path.join(output_folder, "6_flip.jpg"), flip)
print("\nAll 6 processed images saved successfully into the 'Output' folder!")

#-------------------------------------------------------------------
# Display Graphical Windows
#-------------------------------------------------------------------
cv2.imshow("1. Resized Image", resized_image)
cv2.imshow("2. Grayscale Image", gray)
cv2.imshow("3. Blurred Image", blur)
cv2.imshow("4. Edge Detection", edge)
cv2.imshow("5. Rotated Image", rotate)
cv2.imshow("6. Flipped Image", flip)

#-------------------------------------------------------------------
# Window Termination Control
#-------------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
print("\nProgramme Created Successfully")
