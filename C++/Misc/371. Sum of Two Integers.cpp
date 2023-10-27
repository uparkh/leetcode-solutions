using namespace std;

// My Solution
/**
 * Was pretty much just going for a Full Adder
 * from Computer Architecture class.
 * 
 * Gave up because it doesn't feel clever enough.
*/
// class Solution {
// public:
//     int getSum(int a, int b) {
//         int res = 0, S = 0, C_out = 0;
//         int max_int = sizeof(int) * 8;
//         while (max_int-- > 0)
//         {
//             int dA = a & 1;
//             int dB = b & 1;

//             S = (~dA & dB) | (dA & ~dB) | (~dA & ~dB);



//             C_out = (~dA & ~dB);
//         }
//     }
// };


// kishynivas10's Java->cpp solution:
// https://leetcode.com/problems/sum-of-two-integers/solutions/132479/simple-explanation-on-how-to-arrive-at-the-solution/
/**
 * And I was right! This solution is incredibly clever.
 * - AND (&) calculates carry bit (1 if 1+1)
 * - XOR (^) performs binary addition (0+1 = 1+0 = 1)
 * - Remaining carries need to be shifted left by 1.
 * Need to perform carry calculation first, then binary
 * addition with XOR, then shift new carries left 1.
 * 
 * Keep repeating until next carry bits are zeroed out
 * (b != 0)
*/
class Solution {
public:
    int getSum(int a, int b) {
        int c;
        while (b != 0)
        {
            c = a & b;
            a = a ^ b;
            b = c << 1;
        }
        return a;
    }
};