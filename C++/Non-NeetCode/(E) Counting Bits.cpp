#include <vector>
#include <iostream>
#include <bitset>

using namespace std;

/**
 * O(n) runtime
 * O(n) memory because of vector reallocs
*/
class Solution {
public:
    static vector<int> countBits(int n) {
        vector<int> rv(1, 0); // init first elem to 0
        for (int i = 1; i <= n; i++)
        {   
            int next_power = static_cast<int>(rv.capacity());
            if (i == next_power) // single bit set
                rv.push_back(1);
            else    // potentially just one-liner?
                rv.push_back(1 + rv[~(next_power >> 1) & i]);
        }
        return rv;
    }
};

/**
 * O(n) runtime
 * O(1) memory due to no vector realloc
 * 
 * Quite elegant, uses 1D DP, and fact that srl(even)
 * does not change count of 1s, while for odds, it
 * decreases count of 1s by 1. Account for it with
 * the even/odd adjust (i & 1).
*/
// class Solution {
// public:
//     vector<int> countBits(int n) {
//         vector<int> t(n+1);
//         t[0] = 0;
//         for(int i = 1; i<=n; ++i)
//             t[i] = t[i >> 1] + (i & 1);

//         return t;
//     }
// };

int main()
{
    int n = 32;
    auto counts = Solution::countBits(n);
    for (unsigned int i = 0; i <= n; i++)
    {
        auto bs = bitset<8>(i);
        cout << i << " | Count: " << counts[i] << 
            " | " << bs.to_string() << '\n'; 
    }
    return 0;
}