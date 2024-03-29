#!/usr/bin/env python3

# Credits: @itm4n (https://itm4n.github.io/dll-proxying/)

from __future__ import print_function
import argparse

def main():
    parser = argparse.ArgumentParser(description="DLL Export Viewer - Report Parser")
    parser.add_argument("report", help="the HTML report generated by DLL Export Viewer")
    args = parser.parse_args()
    report = args.report

    try:
        f = open(report)
        page = f.readlines()
        f.close()
    except:
        print("[-] ERROR: open('%s')" % report)
        return

    for line in page:
        if line.startswith("<tr>"):
            cols = line.replace("<tr>", "").split("<td bgcolor=#FFFFFF nowrap>")
            function_name = cols[1]
            ordinal = cols[4].split(' ')[0]
            dll_orig = "%s_orig" % cols[5][:cols[5].rfind('.')]
            print("#pragma comment(linker,\"/export:%s=%s.%s,@%s\")" % (function_name, dll_orig, function_name, ordinal))

if __name__ == '__main__':
    main()

