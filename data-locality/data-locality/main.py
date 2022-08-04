# Python Omegalul

# "organize your data structures so that the things you’re processing are next to each other in memory."

# "Modern computers have a little chunk of memory right inside the chip. The CPU can pull data from this much faster than it can from main memory."

# "Whenever your chip needs a byte of data from RAM, it automatically grabs a whole chunk of contiguous memory — usually around 64 to 128 bytes — and puts it in the cache.
# This dollop of memory is called a cache line."

# cpu hit / miss

# "Take advantage of that to improve performance by increasing data locality — keeping data in contiguous memory in the order that you process it."

# "Cachegrind - free tool to test this"

# "In C++, using interfaces implies accessing objects through pointers or references.
# But going through a pointer means hopping across memory, which leads to the cache misses this pattern works to avoid."
# "The more you design your program around data locality, the more you will have to give up inheritance, interfaces, and the benefits those tools can provide."
