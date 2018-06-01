#! /usr/bin/env python3
# coding: utf-8
from reader import read
from alpha import Alpha
from petri_net import PetriNet
import sys
import os

def main(argv):
    log = read(argv[1])
    filename = os.path.splitext(os.path.basename(argv[1]))[0]
    alpha_model = Alpha(log)
    alpha_model.generate_footprint(txtfile="{}_footprint.txt".format(filename))
    pn = PetriNet()
    pn.generate_with_alpha(alpha_model, dotfile="{}.dot".format(filename))


if __name__ == '__main__':
    main(sys.argv)
