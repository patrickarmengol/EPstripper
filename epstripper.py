import pefile
import argparse
import os

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='a script to strip the entrypoints of PE files')
    parser.add_argument('input', help='input file or directory')
    parser.add_argument('-r', help='specify replacement value - else will use default 0xcc00ffee', metavar='EP_VAL', action='store', type=lambda x: int(x,16), default=0xcc00ffee,)
    args = parser.parse_args()

    targets = []
    if os.path.isdir(args.input):
        for root,dirs,files in os.walk(args.input):
            for path in files:
                targets.append(os.path.join(root,path))
    elif os.path.isfile(args.input):
        targets.append(args.input)

    for target in targets:
        try:
            pe = pefile.PE(target)
        except pefile.PEFormatError:
            #print('file not in valid PE format:',target)
            continue

        # the EP attribute is of type int
        pe.OPTIONAL_HEADER.AddressOfEntryPoint = args.r

        # output
        pe.write('{0}_stripped{1}'.format(*os.path.splitext(target)))
