#include <stdio.h>

int one() {
	// ���� ���� ����ϱ�
	/*int num1 = 2;
	float num2 = 3.14;

	printf("% d % f \n", num1, num2);*/

	// ����� ���� ����ϱ�
	/*int money = 1300;
	int age = 16;
	printf("���� %d�� ������ �ְ� ���̴� %d���Դϴ�.", money, age);*/

	// % ����ϱ�- %%
	// printf("100%% real");

	// scanf
		/* scanf ���ο� �ٸ� ������ �����ؼ� �� ������ ���� ���� ���� �����ϰ�, ������ ���� �̿��� ������ ����Ѵ�.*/
	/*int num = 3;
	int result = add(num);
	printf("num= %d, result %d", num, result);*/

	// ���� ���� �Է��ϱ�
	/*int price1, price2;
	printf("������ �� �� �Է��ϼ���.");
	scanf("%d %d", &price1, &price2);
	printf("%d���� %d���� ���� %d���Դϴ�.", price1, price2, price1 + price2);*/

	// �� ���� �� ���
	/*int a, b;
	printf("�� ���� �Է����ּ���.\n");
	scanf("%d %d", &a, &b);
	printf("%d+ %d= %d", a, b, a + b);*/

	// �� �м��� �� ���
	/*int a_down, a_up;
	int b_down, b_up;
	int total_up, total_down = 0;

	printf("���� �м� �� ���� �Է��Ͻʽÿ�.\n");
	scanf("%d/ %d+ %d/ %d", &a_up, &a_down, &b_up, &b_down);
	
	total_up = (a_up * b_down) + (b_up * a_down);
	total_down = (a_down * b_up) + (b_down * a_up);
	
	printf("�� �м��� ���� ���� %d/%d�Դϴ�.", total_up, total_down);*/

	// printf("%d, %d", 30 / 6, 30 % 7);

	//int num = 2;
	///*if (num % 2 == 0) printf("%d�� 2�� ����Դϴ�.\n", num);
	//else if (num % 3 == 0) printf("%d�� 3�� ����Դϴ�.\n", num);*/

	//for (num; num <= 100; num+= 2) {
	//	int sum = 0;
	//	sum+= num;
	//	printf("%d\n", sum);
	//}

	/*int star = 8;

	for (int i = 0; i < star; i++) {
		for (int j = 0; j <= i; j++) printf("*");
		printf("\n");
	}*/

	printf(add(3, 7));
	
	return 0;
}

int add(int num1, int  num2) {
	int sum = num1 + num2;

	return sum;
}