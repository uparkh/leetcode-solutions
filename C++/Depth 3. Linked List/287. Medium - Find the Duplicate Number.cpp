#include <vector>
using namespace std;

// My Original Solution - O(?) runtime, O(1) space (Required)
// This solution works, but tends towards exponential time (?)
// as the size of the problem increases.
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        while (!(slow != fast && nums[slow] == nums[fast])) {
            slow = (slow + 1) % nums.size();
            fast = (fast + 2 + (fast == slow)) % nums.size();
        }
        return nums[slow];
    }
};

// NeetCode Solution - O(n) runtime, O(1) space (R)
// Since 1 <= nums[i] <= n, and array.size() in [1, n+1],
// each element of array can be an index to another
// element of the array.

// KEY INTUITION: Treating each value in the index as another
// index turns this array into a linked list/digraph with
// a cycle. Once this cycle is discovered, the meeting
// point will be the duplicate.
class NeetCodeSolution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[nums[0]];
        
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};