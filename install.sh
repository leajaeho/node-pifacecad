gcc -c -o ./lib/libpiface.o ./src/pifacecad.c
ar rcs ./lib/libpifacecad.a ./lib/libpiface.o
gcc -c -o ./lib/libmcp23s17.o ./src/mcp23s17.c
ar rcs ./lib/libmcp23s17.a ./lib/libmcp23s17.o