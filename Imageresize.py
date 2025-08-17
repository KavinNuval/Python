from PIL import Image
import os

input_folder = "images"
output_folder = "resized"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
new_size = (width, height)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)
        print(f"Resized and saved: {output_path}")

print("✅ All images resized successfully!")
