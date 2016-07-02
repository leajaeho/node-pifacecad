pwd
ls
mkdir lib
ls
cd ./libmcp23s17/ && make
make install
pwd
cd ..
pwd
gcc -c -o ./lib/libpifacecad.o ./src/pifacecad.c
ar rcs ./lib/libpifacecad.a ./lib/libpifacecad.o