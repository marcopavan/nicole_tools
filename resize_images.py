import os
import shutil
from PIL import Image
import argparse

# Functions

def resize_img_pil(img_pil, new_width):
	width, height = img_pil.size
	img_scale = new_width/width
	new_x, new_y = img_pil.size[0]*img_scale, img_pil.size[1]*img_scale
	img_pil = img_pil.resize((int(new_x),int(new_y)),Image.ANTIALIAS)
	height, width = img_pil.size
	return img_pil

# Main

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str, required=True)
parser.add_argument('-w', type=str, required=True)
args = parser.parse_args()

dataset_path = args.p
resized_dataset_path = dataset_path+"_RESIZED"

if os.path.exists(resized_dataset_path):
	shutil.rmtree(resized_dataset_path)

os.makedirs(resized_dataset_path)
os.chmod(resized_dataset_path, 0o775)

listing = [f for f in os.listdir(dataset_path) if ".jpg" in f or ".png" in f]
for img in listing:
	img_pil = Image.open(dataset_path+os.sep+img)
	resized_img_pil = resize_img_pil(img_pil, int(args.w))
	resized_img_pil.save(resized_dataset_path+os.sep+img)