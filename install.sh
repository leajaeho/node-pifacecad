make -C ./libmcp23s17/Makefile
make install
mkdir lib
gcc -c -o ./lib/libpiface.o ./src/pifacecad.c
ar rcs ./lib/libpifacecad.a ./lib/libpiface.o
