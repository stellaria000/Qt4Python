#include <stdio.h>

void isPrime(int num) {
	int check = 0;

	for (int i = 2; i <= num; i++) {
		if (num % i!= 0) {

			check += 1;
			
		}
	}
	printf("%d ���� �Ҽ��� ã�ҽ��ϴ�.");
}