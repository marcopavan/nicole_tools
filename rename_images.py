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
	print("Trovate "+str(len(files))+" immagini.")

	i=0
	for f in files:
		i+=1
		file_ext = f.split(".")[-1]
		newname = str(i)+"."+file_ext
		if args.n:
			newname = args.n+"_"+newname
		os.rename(args.p+os.sep+f, args.p+os.sep+newname)
	print("Rinominate "+str(i)+" immagini.")

elif args.i:
	print("Trovate "+str(len(args.i))+" immagini.")

	i=0
	for f in args.i:
		i+=1
		file_ext = f.split(".")[-1]
		file_path = f.rsplit("/", 1)[1]
		path, file = os.path.split(f)
		newname = str(i)+"."+file_ext
		if args.n:
			newname = args.n+"_"+newname
		os.rename(f, path+os.sep+newname)
	print("Rinominate "+str(i)+" immagini.")