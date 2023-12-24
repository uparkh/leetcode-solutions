#include <string>
#include <unordered_map>
using namespace std;

// My Original Solution - O(n) time for required operations
// Unordered maps are really slow, but at least the solution worked.
class NeetCodeTrie {
private:
    struct TrieNode {
        char val;
        unordered_map<char, TrieNode*> children;
        TrieNode(char n_val = '\0') : val(n_val) {}
        ~TrieNode() {
            for (auto char_node_pair : children) {
                delete char_node_pair.second;
            }
        }
    };

    TrieNode root;
public:
    NeetCodeTrie() {
    }
    
    void insert(string word) {
        TrieNode* node = &root;
        for (char c : word) {
            if (node->children.contains(c)) 
                node = node->children[c];
            else
                node = node->children[c] = new TrieNode(c);
        }
        node->children['\0'] = new TrieNode(); // indicate a word ended at this last node
    }
    
    bool search(string word) {
        TrieNode* node = &root;
        for (char c : word) {
            if (! node->children.contains(c))
                return false;
            node = node->children[c];
        }
        return node->children.contains('\0');
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = &root;
        for (char c : prefix) {
            if (! node->children.contains(c))
                return false;
            node = node->children[c];
        }
        return true;
    }
};


// NeetCode Solution
// Key points:
// 1. Constraints are that only English lowercase used, can easily use an array here
// 2. Don't store a null character for EOW, just use a bool
// This solution uses only C++ primitives, no additional structures beyond the string.
// Even though hash maps are O(1) time important operations, they will always be much slower
// to use than primitive arrays. So next time I use a hash map I should ask myself if I 
// really **need** to use the map or if an array with index-value mapping is more than enough.

class NeetCodeTrieNode {
public:
    NeetCodeTrieNode* children[26];
    bool isWord;
    
    NeetCodeTrieNode() {
        for (int i = 0; i < 26; i++) {
            children[i] = NULL;
        }
        isWord = false;
    }
};

class NeetCodeTrie {
public:
    NeetCodeTrie() {
        root = new NeetCodeTrieNode();
    }
    
    void insert(string word) {
        NeetCodeTrieNode* node = root;
        int curr = 0;
        
        for (int i = 0; i < word.size(); i++) {
            curr = word[i] - 'a';
            if (node->children[curr] == NULL) {
                node->children[curr] = new NeetCodeTrieNode();
            }
            node = node->children[curr];
        }
        
        node->isWord = true;
    }
    
    bool search(string word) {
        NeetCodeTrieNode* node = root;
        int curr = 0;
        
        for (int i = 0; i < word.size(); i++) {
            curr = word[i] - 'a';
            if (node->children[curr] == NULL) {
                return false;
            }
            node = node->children[curr];
        }
        
        return node->isWord;
    }
    
    bool startsWith(string prefix) {
        NeetCodeTrieNode* node = root;
        int curr = 0;
        
        for (int i = 0; i < prefix.size(); i++) {
            curr = prefix[i] - 'a';
            if (node->children[curr] == NULL) {
                return false;
            }
            node = node->children[curr];
        }
        
        return true;
    }
private:
    NeetCodeTrieNode* root;
};
