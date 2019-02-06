
mkdir -p lib
cd ./libmcp23s17/ && make && make install
cd ..
gcc -c -o ./lib/libpifacecad.o ./src/pifacecad.c \
  && ar rcs ./lib/libpifacecad.a ./lib/libpifacecad.o

node-gyp configure
node-gyp build

