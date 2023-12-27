#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

// My Original Solution -- Recursive Backtracking w/Trie
// O(m*n*c) runtime, O(m*n*c*w) memory
// m = rows, n = columns, c = avg. dict. word length, w = amt of words in dict

// This isn't the best solution, but I am REALLY happy that it worked.
// I applied everything I've learned up to this point with DFS and Tries and I'm just so happy
// I did it in C++ too! Very proud of this.
// The last 1 hr 12 minutes went by very quickly
class Trie {
private:
    struct TrieNode {
        TrieNode* children[26]; // lowercase English alphabet
        bool isWord; // End-of-word

        TrieNode(): isWord{false} {
            for (TrieNode* &child : children) {
                child = nullptr;
            }
        }

        ~TrieNode() {
            for (TrieNode* &child : children) {
                delete child;
            }
        }
    };

    TrieNode* root;
public:
    Trie() : root{new TrieNode()} {
    }

    void insert(const string & word) {
        TrieNode* node = root;
        int idx = 0;
        for (char c : word) {
            idx = c - 'a';
            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->isWord = true;
    }

    friend class Solution;
};
class Solution {
private:
    void dfs(Trie::TrieNode* root, int i, int j, vector<vector<char>>& board, 
                vector<vector<bool>> & visited, unordered_set<string> &result, string & word) {
        if ( (i < 0 || i >= board.size()) || (j < 0 || j >= board[0].size()) ) { //bounds
            return;
        }
        if (visited[i][j]) { // don't rerun visited nodes!
            return;
        }

        char elem = board[i][j];
        int idx = elem - 'a';
        if (root->children[idx] == nullptr) {
            return;
        }
        root = root->children[idx];
        visited[i][j] = true;
        word.push_back(elem); 
        if (root->isWord) {
            result.insert(word);
        }

        dfs(root, i-1, j, board, visited, result, word); // left
        dfs(root, i+1, j, board, visited, result, word); // right
        dfs(root, i, j-1, board, visited, result, word); // down
        dfs(root, i, j+1, board, visited, result, word); // up

        visited[i][j] = false;
        word.pop_back();

    }
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie trie;
        for (const string & word : words) {
            trie.insert(word);
        }

        unordered_set<string> result;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        string currWord;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(trie.root, i, j, board, visited, result, currWord); 
            }
        }

        return vector<string>(result.begin(), result.end());
        
    }
};


// NeetCode Solution
// The general idea is the exact same as mine, with recursive backtracking.
// Main differences are:
// 1. Instead of a `visited` 2D container, just mark board[i][j] with some sentinel value
//    (in their case, '#') as visited. Saves memory/lookup cost of the visited vector.

// 2. No need to pass a ref to the word-building string, just pass by value.

// 3. When a word is added to result, mark node->isWord = false, "consuming" the word
//    so I don't need an unordered_set. When isWord becomes false, now no duplicate word
//    can be added. Saves memory of result vector and the O(n) conversion of set->vector.

/*
    Given a board of characters & a list of words, return all words on the board

    Implement trie, for search: iterate thru children until isWord, add to result

    Time: O(m x (4 x 3^(l - 1))) -> m = # of cells, l = max length of words
    Space: O(n) -> n = total number of letters in dictionary (no overlap in Trie)
*/

// class TrieNode {
// public:
//     TrieNode* children[26];
//     bool isWord;
    
//     TrieNode() {
//         for (int i = 0; i < 26; i++) {
//             children[i] = NULL;
//         }
//         isWord = false;
//     }
// };

// class Solution {
// public:
//     vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
//         for (int i = 0; i < words.size(); i++) {
//             insert(words[i]);
//         }
        
//         int m = board.size();
//         int n = board[0].size();
        
//         TrieNode* node = root;
//         vector<string> result;
        
//         for (int i = 0; i < m; i++) {
//             for (int j = 0; j < n; j++) {
//                 search(board, i, j, m, n, node, "", result);
//             }
//         }
        
//         return result;
//     }
// private:
//     TrieNode* root = new TrieNode();
    
//     void insert(string word) {
//         TrieNode* node = root;
//         int curr = 0;
        
//         for (int i = 0; i < word.size(); i++) {
//             curr = word[i] - 'a';
//             if (node->children[curr] == NULL) {
//                 node->children[curr] = new TrieNode();
//             }
//             node = node->children[curr];
//         }
        
//         node->isWord = true;
//     }
    
//     void search(vector<vector<char>>& board, int i, int j, int m, int n, TrieNode* node, string word, vector<string>& result) {
//         if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] == '#') {
//             return;
//         }
        
//         char c = board[i][j];
        
//         node = node->children[c - 'a'];
//         if (node == NULL) {
//             return;
//         }
        
//         word += board[i][j];
//         if (node->isWord) {
//             result.push_back(word);
//             node->isWord = false;
//         }
        
//         board[i][j] = '#';
        
//         search(board, i - 1, j, m, n, node, word, result);
//         search(board, i + 1, j, m, n, node, word, result);
//         search(board, i, j - 1, m, n, node, word, result);
//         search(board, i, j + 1, m, n, node, word, result);
        
//         board[i][j] = c;
//     }
// };


