import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', help='Insert folder path', type=str, required=True)
parser.add_argument('-n', help='Insert prefix name', type=str, required=False)
args = parser.parse_args()

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