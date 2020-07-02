
""" 
json-prettify.py
========================

This script reads in a JSON file, and outputs a prettified version of it.



Date          Author       Description
------------  ------------ -----------------------------
2020-06-19    T QUIRKE     Created this script. 


"""

import argparse
import json
import sys


def prettify_json(pyargs):
    infile = pyargs.infile
    outfile = pyargs.outfile

    if outfile == None:
        outfile = infile.replace('.json', '_pretty.json')
    
    try:
        print(f'Opening file {infile}')
        with open(infile, 'r') as r:
            file_in = json.load(r)
            pretty = json.dumps(file_in, indent=4, sort_keys=True)
            pretty.replace("\n", "\r\n")
    except:
        print(f'Failed to open file {infile}. Exiting.')
        sys.exit(1)
    
    try:
        print(f'Writing file {outfile}')
        with open(outfile, 'w', encoding='utf-8', newline="\r\n" ) as w:
            w.writelines(pretty)
    except:
        print(f'Failed to write file {outfile}. Exiting.')
        sys.exit(1)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Prettify a JSON file!') 
    
    arg_parser.add_argument('-i', '--infile', action='store', default=None, required=True,\
        help='Path to the input JSON file.', type=str) 
    
    arg_parser.add_argument('-o', '--outfile', action='store', default=None, required=False,\
        help='Path to the output JSON file.', type=str) 
    
    pyargs = arg_parser.parse_args()
    prettify_json(pyargs)



