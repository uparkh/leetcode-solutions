#include <iostream>
#include <vector>
using namespace std;

// My Original Solution
// Build adjacancy graph, DFS to filter disconnected graphs (auto-false)
// then BFS to find cycles (auto-false). Else, true.

// Time: O(max(n, m)) -- n = numCourses, m = prerequisites.size()
// Space: O(n * m)
class Solution {
private:
    bool has_no_cycles(vector<vector<int>>& _adjacency, vector<bool>& _visited,
            int vtx_no) {
        _visited[vtx_no] = true;
        for (int& neighbor : _adjacency[vtx_no]) {
            if (_visited[neighbor] == true) { // cycle
                return false;
            }
            if (has_no_cycles(_adjacency, _visited, neighbor) == false) {
                return false;
            }
        }
        return true;
    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if (prerequisites.empty()) {
            return true;
        }
        vector<vector<int>> adjacency(numCourses);
        for (vector<int>& prereq_edge : prerequisites) {
            int to_vtx = prereq_edge[0], from_vtx = prereq_edge[1];
            adjacency[to_vtx].push_back(from_vtx);
        }
        vector<bool> visited(numCourses);
        int first_w_edges = 0;
        while (adjacency[first_w_edges].size() == 0 
                && first_w_edges < numCourses) {
            ++first_w_edges;
        }
        if (has_no_cycles(adjacency, visited, first_w_edges) == false) {
            return false;
        }
        for (bool vtx_visited : visited) {
            if (!vtx_visited) {
                return false;
            }
        }
        return true;
    }
};

int main (int argc, char *argv[]) {
    // vector<vector<int>> prereqs = {{1, 0}};
    // int numCourses = 1;
    vector<vector<int>> prereqs = {};
    int numCourses = 1;
    cout << "Result: " << Solution().canFinish(numCourses, prereqs) << "\n";
    return 0;
}
