#!/bin/bash

echo "Moving original helpers.dll to helpers_orig.dll ..."
mv ../x64/Release/helpers.dll ../x64/Release/helpers_orig.dll

echo "Replacing helpers.dll with evill.dll ..."
mv ../x64/Release/evil.dll ../x64/Release/helpers.dll

echo "Done!"
