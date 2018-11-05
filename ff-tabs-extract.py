#!.venv/bin/python3

# import sys
# sys.argv

import fire

## TODO get args - 
## ? ff-tabs [in-name] [out-name]   # assuming jsonlz4, the moz fmt

# def fetch():
# cp 
#   ~/Library/Application\ Support/Firefox/profiles/x98wumfy.default/sessionstore-backups/recovery.jsonlz4
#   data/raw/$(date +"recovery.jsonlz4.%F.%T")

def extract(infile, outfile):

    f = open(infile, 'rb')
    _mozilla_magic_prefix = f.read(8)
    jsonlz4 = f.read()

    import lz4.block
    json = lz4.block.decompress(jsonlz4)

    fw = open(outfile, 'wb')
    fw.write(json)
    
    return 'Succeeded'

if __name__ == '__main__':
    fire.Fire(extract)
