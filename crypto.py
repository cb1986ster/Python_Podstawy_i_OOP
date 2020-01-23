#!/usr/bin/env python3.6
import sys
import argparse

from libs.FancyCryptoTextFile import FancyCryptoTextFile
from libs.FancyTextFile import FancyTextFile

def file_crypt(input_file,output_file,password):
    in_file = FancyTextFile(input_file)
    out_file = FancyCryptoTextFile(output_file, password)
    out_file.put_content(in_file.get_content())

def file_decrypt(input_file,output_file,password):
    in_file = FancyCryptoTextFile(input_file, password)
    out_file = FancyTextFile(output_file)
    out_file.put_content(in_file.get_content())

def main():
    # https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description='Crypt or decrypt text file')
    parser.add_argument('-p', '--password', help='password', required=True)
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file(if not given "[INPUT].enc" or "[INPUT].dec")', default=None)
    parser.add_argument('-d', '--decrypt',help='default behvior is to crypt, use this option to decrypt', action='store_true')
    args = parser.parse_args(sys.argv[1:])
    # If output not given
    if args.output == None:
        if args.decrypt:
            args.output = args.input+'.dec'
        else:
            args.output = args.input+'.enc'

    # Do work :)
    if args.decrypt:
        print('{} =Decrypt({})=> {}'.format(args.input,args.password,args.output))
        file_decrypt(args.input,args.output,args.password)
    else:
        print('{} =Crypt({})=> {}'.format(args.input,args.password,args.output))
        file_crypt(args.input,args.output,args.password)

if __name__ == '__main__':
    main()
