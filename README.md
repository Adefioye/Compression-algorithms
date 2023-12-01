# COMPARISON OF COMPRESSION ALGORITHM

### FOR STRING DATA

- For `lzma`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```
import time
import lzma

string_data = b"Technical" * 999999

print("Original data size: ", len(string_data))

compress_start_time = time.time()
compressed_lzma_data = lzma.compress(string_data)
compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed data size: ", len(compressed_lzma_data))

decompress_start_time = time.time()
lzma.decompress(compressed_lzma_data)
decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)

```

- For `gzip`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```
import time 
import gzip

string_data = b"Technical" * 999999

print("Original data size: ", len(string_data))

compress_start_time = time.time()
compressed_lzma_data = gzip.compress(string_data)
compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed data size: ", len(compressed_lzma_data))

decompress_start_time = time.time()
gzip.decompress(compressed_lzma_data)
decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)

```

- For `bzip2`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```
import time 
import bz2

string_data = b"Technical" * 999999

print("Original data size: ", len(string_data))

compress_start_time = time.time()
compressed_lzma_data = bz2.compress(string_data)
compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed data size: ", len(compressed_lzma_data))

decompress_start_time = time.time()
bz2.decompress(compressed_lzma_data)
decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)

```

### FOR PDF FILE
- For `lzma`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```
import time 
import lzma
import os

FILE_NAME = "program-of-study.pdf"

print("Original file size: ", os.path.getsize(FILE_NAME))

compress_start_time = time.time()

with open("program-of-study.pdf", "rb") as f_in, lzma.open("compress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed file size: ", os.path.getsize("compress.pdf"))

decompress_start_time = time.time()

with lzma.open("compress.pdf", "rb") as f_in, open("uncompress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)
```

- For `gzip`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```
import time 
import gzip
import os

FILE_NAME = "program-of-study.pdf"

print("Original file size: ", os.path.getsize(FILE_NAME))

compress_start_time = time.time()

with open("program-of-study.pdf", "rb") as f_in, gzip.open("compress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

compress_end_time = time.time()

print("Time to compress data (s): ", compress_end_time - compress_start_time)

print("Compressed file size: ", os.path.getsize("compress.pdf"))

decompress_start_time = time.time()

with gzip.open("compress.pdf", "rb") as f_in, open("uncompress.pdf", "wb") as f_out:
    f_out.write(f_in.read())

decompress_end_time = time.time()

print("Time to decompress data (s): ", decompress_end_time - decompress_start_time)

```
- For `bzip`, the code below is used and data for original data size, compressed data size, compression time and decompression time were noted.

```

```


