# DistinctElementsInStreamsPy

This algorithm provides an unbiased estimator for the number of unique
elements in a stream given a limited buffer size. Proposed by Sourav Chakraborty, Kuldeep S. Meel., and N. V. Vinodchandran in the paper [Distinct Elements in Streams: An Algorithm for the Textbook](DistinctElementsInStreams.pdf)







Step 1 : Create C file

Step 2 : compile C file to a shared library `.so` file with

`gcc -arch x86_64 -shared -o cmvinterface/cmv.so -fPIC cmv.c`

then can run code with 

`python runcode.py`
