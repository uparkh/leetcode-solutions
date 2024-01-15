#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// My Original Solution
// Gave up after 45 minutes in. I had the right idea of using BFS, but just didn't
// implement it right, not sure why it wasn't returning what I wanted to, but I gave up as soon
// as I started using parallel queue structures. Anytime parallel structures are used, it usually
// means there's significant inefficiencies in my design.
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }
        unordered_set<int> visited;
        queue<Node*> Q, cQ;
        Node* cHead, * cNode;
        cHead = cNode = new Node(node->val);
        visited.insert(node->val);
        Q.push(node);
        cQ.push(cNode);

        while (!Q.empty()) {
            node = Q.front();
            cNode = cQ.front();
            Q.pop();
            cQ.pop();
            visited.insert(node->val);
            for (Node* neighbor : node->neighbors) {
                if (visited.contains(neighbor->val)) {
                    continue;
                }
                Node* cNeighbor = new Node(neighbor->val);
                cNode->neighbors.push_back(cNeighbor);
                cNeighbor->neighbors.push_back(cNode);

                Q.push(neighbor);
                cQ.push(cNeighbor);
            }
        }

        // dfs(visited, node, cNode);
        return cHead;
    }

// private:
//     void dfs(unordered_set<int>& visited, Node* node, Node* cNode) {
//         // if (visited.contains(node->val)) {
//         //     return;
//         // }
//         visited.insert(node->val);
//         for (Node* neighbor : node->neighbors) {
//             if (visited.contains(neighbor->val)) {
//                 continue;
//             }
//             Node* cNeighbor = new Node(neighbor->val);
//             cNode->neighbors.push_back(cNeighbor);
//             cNeighbor->neighbors.push_back(cNode);
//             dfs(visited, neighbor, cNeighbor);
//         }
//     }
};

// NeetCode Solution
// O(n) spacetime
// Simply just maps the node ptrs to the copy ptrs. Makes it much easier to keep track of
// the cloned graph.
class NeetCodeSolution {
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) {
            return NULL;
        }
        
        Node* copy = new Node(node->val);
        m[node] = copy;
        
        queue<Node*> q;
        q.push(node);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            for (Node* neighbor : curr->neighbors) {
                if (!m.contains(neighbor)) {
                    m[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                m[curr]->neighbors.push_back(m[neighbor]);
            }
        }
        return copy;
    }
private:
    unordered_map<Node*, Node*> m;
};
