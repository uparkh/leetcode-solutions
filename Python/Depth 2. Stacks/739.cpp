#include <vector>
#include <stack>
#include <iostream>

using namespace std;

class Solution {
public:
    static vector<int> dailyTemperatures(const vector<int>& temperatures)
    {
        vector<int> result(temperatures.size(), 0);
        stack<int> S;
        for (int i = 0; i < temperatures.size(); ++i)
        {
            // result.push_back(0);
            while (!S.empty() && temperatures[i] > temperatures[S.top()])
            {
                result[S.top()] = i - S.top();
                S.pop();
            }
            S.push(i);
        }
        return result;
    }
};

int main()
{
    auto rv = Solution::dailyTemperatures({73,74,75,71,69,72,76,73});
    cout << '[';
    for (auto days : rv)
    {
        cout << ' ' << days << ' ';
    }
    cout << ']';
    return 0;
}
