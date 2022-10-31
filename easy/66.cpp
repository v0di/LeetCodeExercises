#include <vector>
#include <cstdlib>
#include <iostream>

class Solution {
	public:
		std::vector<int> plusOne(std::vector<int>& digits) {
			++digits.back();
			for (int i = digits.size() - 1; i > 0; --i) {
				if (digits[i] > 9) {
					digits[i] = 0;
					++digits[i - 1];
				}
				else {break;}
			}
			if (digits.front() > 9) {
				digits[0] = 0;
				digits.insert(digits.begin(), 1);
			}
			return digits;
		}
};

int main() {

	std::vector<int> digits = {7};
	Solution solution = Solution();
	solution.plusOne(digits);

	for (const int i : digits) {std::cout << i;}
	std::cout << '\n';

	system("pause");

	return 0;
}