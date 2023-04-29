#include <stdio.h>
int main() {
	int N;
	int value = 0;
	int test = 1;
		
	scanf("%d", &N);
	
	while ((N - test) > 0) {
		value += 1;
		test += 6 * value;
	}
	printf("%d", value + 1);
}