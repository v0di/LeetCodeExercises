#include <iostream>
#include <vector>
#include <string>

class Solution {
    public:
        std::string longestCommonPrefix(std::vector<std::string>& strs) {
            std::string str = "";
            char temp;
            int index = 0;
            int maxLength = strs[0].size();
            while (true) {
                temp = strs[0][index];
                for (auto iter = strs.begin() + 1; iter < strs.end(); iter++) {
                    if ((*iter)[index] != temp) { return str; }
                    if (index == 0) {
                        int s = (*iter).size();
                        maxLength = s < maxLength ? s : maxLength;
                    }
                }
                if (temp) { str += temp; }
                ++index;
                if (index > maxLength) { return str; }
            }
        }
};

int main() {

    std::vector<std::string> str = {"flower","flow","flight"};
    Solution solution = Solution();
    std::string solutionString = solution.longestCommonPrefix(str);
    std::cout << solutionString << std::endl;
    system("pause");

    return 0;
}