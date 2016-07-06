mkdir lib
cd ./libmcp23s17/ && make
sudo make install
cd ..
gcc -c -o ./lib/libpifacecad.o ./src/pifacecad.c
ar rcs ./lib/libpifacecad.a ./lib/libpifacecad.o