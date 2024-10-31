import sys, os
import calculateHash

if len(sys.argv) != 2:
    sys.exit("AMAS usage: amas.py <malware name>")

malwareFullPath = os.path.abspath(sys.argv[1])

if os.path.exists(malwareFullPath) == False:
    raise FileNotFoundError("File not found in the specified directory. Exiting.")

malwareAbsPath = os.path.split(malwareFullPath)[0]
malwareFilename = os.path.split(malwareFullPath)[1]

# calculate md5 hash of a file
malwareMD5hash = calculateHash.md5(malwareFilename)

print(malwareMD5hash)