#!/usr/bin/env python3

# Credits: @tothi (https://github.com/tothi/dll-hijack-by-proxying/blob/master/gen_def.py)

import pefile
import sys
import os.path

dll = pefile.PE(sys.argv[1])
dll_basename = os.path.splitext(sys.argv[1])[0]

print("EXPORTS")
for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
    if export.name:
        print('{}={}.{} @{}'.format(export.name.decode(), dll_basename, export.name.decode(), export.ordinal))
