
# import gzip 
# import bz2 

import time 
import bz2
import os

FILE_NAME = "program-of-study.pdf"

print("Original file size: ", os.path.getsize(FILE_NAME))

compress_start_time = time.time()

with open("program-of-study.pdf", "rb") as f_in, bz2.open("compress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed file size: ", os.path.getsize("compress.pdf"))

decompress_start_time = time.time()

with bz2.open("compress.pdf", "rb") as f_in, open("uncompress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)
