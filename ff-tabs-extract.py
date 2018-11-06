#!.venv/bin/python3

# import sys
# sys.argv

import fire

## TODO get args - 
## ? ff-tabs [in-name] [out-name]   # assuming jsonlz4, the moz fmt

def fetch():
    """Copies current version of Firefox recovery backup file and returns path to snapshot"""
    from glob import glob
    from datetime import datetime
    from shutil import copyfile
    import os

    paths = glob('/Users/mcint/Library/Application Support/Firefox/Profiles/*/sessionstore-backups/recovery.jsonlz4')
    srcpath = paths[0]
    
    localpath = 'data/raw'
    timestamp = datetime.strftime(datetime.now(), '%F.%T')
    tgtfile = '.'.join([os.path.basename(srcpath), timestamp, 'snapshot'])
    tgtpath = os.path.join(localpath, tgtfile)

    copyfile(srcpath, tgtpath)

    # TODO copy to data/raw/  as recovery.jsonlz4.ymd.hms.snapshot
    # TODO return new path to data/raw/ file
    return tgtpath

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
    fire.Fire()
