#!/usr/bin/env python3

import pyqrcode
from PIL import Image
import sys, getopt

def main(argv):
 
    input = None
    outputFile = None
    scale = 10

#SSID: MLP22

    try:
        #opts, args = getopt.getopt(argv,"hw:p:t:o:",["ifile=","ofile="])
        opts, args = getopt.getopt(argv,"ho:s:",["oFile=","scale="])
    except getopt.GetoptError:
        print ("qrGenerator.py -o <ruta_output> url/texto")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("qrGenerator.py -o <ruta_output> -s <size>[num] url/texto")
            sys.exit(0)
        elif opt in ("-o","--oFile"):
            outputFile = arg
        elif opt in ("-s","--scale"):
            scale = arg
        
    num_args = len(argv)
    input = argv[num_args-1]
    
    if input is None:
        print ("qrGenerator.py -o <ruta_output> url/texto")
        sys.exit(2)
    if ( outputFile is None ):
        outputFile = "./qr.png"

    qrImage = pyqrcode.create(input)
    qrImage.png(outputFile,scale=scale)
    #qrImage.save(outputFile)

if __name__ == "__main__":
   main(sys.argv[1:])
