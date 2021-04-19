#!/usr/bin/python3

import numpy as np
import sys
import h5py
import re


def phase2id(phase):
    # careful, playing tricks with the 8 bit overflow in order to wrap the phase into 0..2pi and discritize into 0..15
    p = np.uint8(float(phase) / 2. / np.pi * 256)
    return np.uint8(int(p) * 16 // 256)


def extract_XY(fname):
    f = h5py.File(fname, 'r')
    X = []
    Y = []
    imkeys = [i for i in list(f.keys()) if re.match('^img\d+', i)]
    for imkey in imkeys:
        carrier = f[imkey].attrs['carrier']
        h = f[imkey]['hist'][()]
        phases = [phase2id(carrier + f[imkey].attrs['ephases'][i]) for i in range(f[imkey].attrs['npulses'])]
        X.append(h)
        Y.append(phases)
    f.close()
    return X, Y


def main():
    imnums = [0]
    if len(sys.argv) < 2:
        print('syntax:\t%s <h5files>' % sys.argv[0])
        return
    fnames = [n for n in sys.argv[1:]]

    for fname in fnames:
        X, Y = extract_XY(fname)
        print(fname)

        _ = [print(a.shape) for a in X]
        _ = [print(y) for y in Y]

    return


if __name__ == '__main__':
    main()
