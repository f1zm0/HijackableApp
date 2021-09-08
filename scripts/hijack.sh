#!/bin/bash

echo "Moving original helpers.dll to helpers_orig.dll ..."
mv ../x64/Release/helpers.dll ../x64/Release/helpers_orig.dll

echo "Copying evil.dll into directory with executable ..."
cp evil.dll ../x64/Release/helpers.dll

echo "Done!"
