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
parser.add_argument('-p', help='Insert folder path', type=str, required=False)
parser.add_argument('-i', help='Insert images', type=str, required=False, nargs="+")
parser.add_argument('-w', type=str, required=True)
args = parser.parse_args()

if args.p:
	dataset_path = args.p
	resized_dataset_path = dataset_path+"_RESIZED"

	if os.path.exists(resized_dataset_path):
		shutil.rmtree(resized_dataset_path)

	os.makedirs(resized_dataset_path)
	os.chmod(resized_dataset_path, 0o775)

	listing = [f for f in os.listdir(dataset_path) if ".jpg" in f or ".png" in f]
elif args.i:
	listing = args.i

print("Trovate "+str(len(listing))+" immagini.")

i=0
for f in listing:
	i+=1
	
	if args.p:
		path = args.p
		file_name = f
	elif args.i:
		path, file_name = os.path.split(f)

	img_pil = Image.open(path+os.sep+file_name)
	resized_img_pil = resize_img_pil(img_pil, int(args.w))

	if args.p:
		destination_path = resized_dataset_path
	elif args.i:
		destination_path = path
		file_name = "RESIZED_w"+args.w+"_"+file_name
	resized_img_pil.save(destination_path+os.sep+file_name)

print("Rinominate "+str(i)+" immagini.")