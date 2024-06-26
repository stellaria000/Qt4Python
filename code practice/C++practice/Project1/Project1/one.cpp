#include <iostream>
#include <cstdlib>

using std::cout;
using std::endl;
using std::cin;

int change_val(int* p) {
	*p = 3;
	return 0;

}
int main() {
	int lucky_number = 9;

	// if-else문 
	/*std::cout << "내 비밀 숫자를 맞춰 보세요" << std::endl;

	int user_input;

	while (1) {
		std::cout << "입력: ";
		std::cin >> user_input;

		if (lucky_number == user_input) {
			std::cout << "맞추셨습니다" << std::endl;

			break;
		}
		else std::cout << "다시 해보세요" << std::endl;
	}*/

	// SWITCH
	/*int user_input;
	cout << "저의 정보를 표시해 줍니다." << endl;
	cout << "1. name: " << endl
		<< "2. age: " << endl
		<< "3. sex: " << endl;

	cin >> user_input;

	switch (user_input) {
	case 1:
		cout << "ysy" << endl;
		break;

	case 2:
		cout << "20s" << endl;
		break;

	case 3:
		cout << "woman" << endl;
		break;

	default:
		cout << "nothing" << endl;
	}*/

	int a = 3;
	int x;
	int& y = x;
	int& z = y;

	x = 1;
	std::cout << "x: " << x << "y: " << y << "z: " << z << std::endl;

	x = 2;
	std::cout << "x: " << x << "y: " << y << "z: " << z << std::endl;

	x = 3;
	std::cout << "x: " << x << "y: " << y << "z: " << z << std::endl;
	return 0;
}

