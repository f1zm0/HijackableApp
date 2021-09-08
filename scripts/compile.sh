#!/bin/bash

 x86_64-w64-mingw32-gcc -shared -o helpers.dll evil.c helpers.def -s
