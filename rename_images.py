import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Insert folder path', type=str, required=False)
parser.add_argument('-i', help='Insert images', type=str, required=False, nargs="+")
parser.add_argument('-n', help='Insert prefix name', type=str, required=False)
args = parser.parse_args()

if args.p:
	files = sorted([f for f in os.listdir(args.p) if ".jpg" in f or ".JPG" in f or ".png" in f])
elif args.i:
	files= args.i
print("Trovate "+str(len(files))+" immagini.")

i=0
for f in files:
	i+=1

	if args.p:
		path = args.p
		file_name = f
	elif args.i:
		path, file_name = os.path.split(f)

	file_ext = file_name.split(".")[-1]
	new_file_name = str(i)+"."+file_ext
	if args.n:
		new_file_name = args.n+"_"+new_file_name
	os.rename(path+os.sep+file_name, path+os.sep+new_file_name)

print("Rinominate "+str(i)+" immagini.")