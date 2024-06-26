#include <stdio.h>

int one() {
	// 여러 변수 출력하기
	/*int num1 = 2;
	float num2 = 3.14;

	printf("% d % f \n", num1, num2);*/

	// 문장과 같이 출력하기
	/*int money = 1300;
	int age = 16;
	printf("돈을 %d원 가지고 있고 나이는 %d살입니다.", money, age);*/

	// % 출력하기- %%
	// printf("100%% real");

	// scanf
		/* scanf 내부에 다른 변수를 선언해서 그 변수에 원래 변수 값을 대입하고, 대입한 값을 이용해 변수를 출력한다.*/
	/*int num = 3;
	int result = add(num);
	printf("num= %d, result %d", num, result);*/

	// 여러 변수 입력하기
	/*int price1, price2;
	printf("가격을 두 개 입력하세요.");
	scanf("%d %d", &price1, &price2);
	printf("%d원과 %d원의 합은 %d원입니다.", price1, price2, price1 + price2);*/

	// 두 수의 합 출력
	/*int a, b;
	printf("두 수를 입력해주세요.\n");
	scanf("%d %d", &a, &b);
	printf("%d+ %d= %d", a, b, a + b);*/

	// 두 분수의 합 출력
	/*int a_down, a_up;
	int b_down, b_up;
	int total_up, total_down = 0;

	printf("더할 분수 두 개를 입력하십시오.\n");
	scanf("%d/ %d+ %d/ %d", &a_up, &a_down, &b_up, &b_down);
	
	total_up = (a_up * b_down) + (b_up * a_down);
	total_down = (a_down * b_up) + (b_down * a_up);
	
	printf("두 분수를 더한 값은 %d/%d입니다.", total_up, total_down);*/

	// printf("%d, %d", 30 / 6, 30 % 7);

	//int num = 2;
	///*if (num % 2 == 0) printf("%d는 2의 배수입니다.\n", num);
	//else if (num % 3 == 0) printf("%d는 3의 배수입니다.\n", num);*/

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