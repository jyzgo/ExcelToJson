#!/usr/bin/env python
 
import os
import sys
import shutil
 
def convert_to_utf8(filename):
    # gather the encodings you think that the file may be
    # encoded inside a tuple
    print filename
    encodings = ('ansi','windows-1253', 'iso-8859-7', 'macgreek')
 
    # try to open the file and exit if some IOError occurs
    try:
        f = open(filename, 'r').read()
    except Exception:
        sys.exit(1)
 
    # now start iterating in our encodings tuple and try to
    # decode the file
    for enc in encodings:
        try:
            # try to decode the file with the first encoding
            # from the tuple.
            # if it succeeds then it will reach break, so we
            # will be out of the loop (something we want on
            # success).
            # the data variable will hold our decoded text
            data = f.decode(enc)
            print enc
            break
        except Exception:
            # if the first encoding fail, then with the continue
            # keyword will start again with the second encoding
            # from the tuple an so on.... until it succeeds.
            # if for some reason it reaches the last encoding of
            # our tuple without success, then exit the program.
            if enc == encodings[-1]:
                sys.exit(1)
            continue
 
    # now get the absolute path of our filename and append .bak
    # to the end of it (for our backup file)
    fpath = os.path.abspath(filename)
    newfilename = fpath + '.bak'
    # and make our backup file with shutil
    shutil.copy(filename, newfilename)
 
    # and at last convert it to utf-8
    f = open(filename, 'w')
    try:
        f.write(data.encode('utf-8'))
    except Exception, e:
        print e
    finally:
        f.close()

def main():
	for root, dirs, files in os.walk(os.getcwd()):
	       	for f in files:
	           	if f.lower().endswith('.conf') :#or f.lower().endswith('.md'):
		       		filename = os.path.join(root, f)
		       		# print filename
		            	try:
		                   	convert_to_utf8(filename)
		               	except Exception,e:
		                   	print e
		                   	print filename
		                   	continue

if __name__ == '__main__':
  	main()