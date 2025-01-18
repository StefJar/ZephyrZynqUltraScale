#!/bin/bash

echo "activate zephyr enviroment and build dir"

mkdir -p build
cd build
#rm -rf * && cmake -DCMAKE_BUILD_TYPE=Debug ..
rm -rf * && cmake ..
make -j
echo "done!"
