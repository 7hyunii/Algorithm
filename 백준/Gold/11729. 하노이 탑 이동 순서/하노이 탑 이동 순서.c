#include <stdio.h>

void hanoi(int num, int x, int z, int y)
{
	if (num==1) {
		printf("%d %d\n", x, z);
	}
	else {
		hanoi(num-1, x, y, z);
		printf("%d %d\n", x, z);
		hanoi(num-1, y, z, x);
	}
}

int main()
{
	int n;
	scanf("%d", &n);

	int count = (1 << n) - 1;
	printf("%d\n", count);
	hanoi(n, 1, 3, 2);
}