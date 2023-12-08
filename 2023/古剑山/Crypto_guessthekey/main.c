#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
	if (argc != 3) {
		printf("USAGE: %s INPUT OUTPUT\n", argv[0]);
		return 0;
	}
	FILE* input  = fopen(argv[1], "rb");
	FILE* output = fopen(argv[2], "wb");
	if (!input || !output) {
		printf("Error\n");
		return 0;
	}
	char key[] = "guessthekey";
	char d, q, t = 0;
	int ijk = 0;
	while ((q = fgetc(input)) != EOF) {
		d = (q + (key[ijk % strlen( key )] ^ t) + ijk*ijk) & 0xff;
		t = q;
        ijk++;
		fputc(d, output);
	}
	return 0;
}
