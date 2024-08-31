#include <string>
using namespace std;

// My Original Solution
// I tried my hardest to be clever and work within a 2D matrix, but
// I guess it's not the most optimal solution. Maybe should have just stuck with
// the trie. Even still I'm not sure what's going wrong.
class WordDictionary {
private:
    // bool = isWord ?
    bool* wordMatrix [26][26]; // 1 <= word.length <= 25, word[26] = EOW
    bool* used[26]; // tracking used slots for '.' processing
public:
    WordDictionary() {
        for (int r = 0; r < 26; r++) {
            for (int c = 0; c < 26; c++) {
                wordMatrix[r][c] = nullptr;
            }
            used[r] = nullptr;
        }
    }

    ~WordDictionary() {
        for (int r = 0; r < 26; r++) {
            for (int c = 0; c < 26; c++) {
                delete wordMatrix[r][c];
            }
            delete used[r];
        }
    }
    
    void addWord(string word) {
        int idx, N = word.length();
        for (int i = 0; i < N; i++) {
            idx = static_cast<int>(word[i] - 'a');
            if (wordMatrix[i][idx] == nullptr) {
                wordMatrix[i][idx] = new bool(false);
                used[i] = new bool(false); // Node created = word pos used
            }
        }
        *wordMatrix[N-1][idx] = true; // the word ends here
        *used[N-1] = true; // SOME word ends here
    }
    
    bool search(string word) {
        bool result = false;
        for (int i = 0; i < word.length(); i++) {
            if (word[i] == '.') {
                if (used[i] == nullptr) // no word reached yet
                    return false;
                result = *used[i];
                continue;
            }
            int idx = static_cast<int>(word[i] - 'a');
            if (wordMatrix[i][idx] == nullptr)
                return false;
            result = *wordMatrix[i][idx]; // did a word end at this node
        }
        return result;
    }
};


// NeetCode Solution
// Much, much, much more simpler than what I thought it was going to be.

// This seems like it performs much worse than my 2D array solution above, with all this
// backtracking/recursion when dealing with '.' wildcards.
// But, alas, after further testing and investigation this truly is the best solution.

// Otherwise, it's just a normal trie addWord/search, like in the previous problem. 
// I'm still not sure why my solution fails.
class TrieNode {
public:
    TrieNode* children[26];
    bool isWord;
    
    TrieNode() {
        for (int i = 0; i < 26; i++) {
            children[i] = NULL;
        }
        isWord = false;
    }
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        int curr = 0;
        
        for (int i = 0; i < word.size(); i++) {
            curr = word[i] - 'a';
            if (node->children[curr] == NULL) {
                node->children[curr] = new TrieNode();
            }
            node = node->children[curr];
        }
        
        node->isWord = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        return searchInNode(word, 0, node);
    }
private:
    TrieNode* root;
    
    bool searchInNode(string& word, int i, TrieNode* node) {
        if (node == NULL) {
            return false;
        }
        if (i == word.size()) {
            return node->isWord;
        }
        if (word[i] != '.') {
            return searchInNode(word, i + 1, node->children[word[i] - 'a']);
        }
        // Literally just searches through every letter when encountering a '.'
        // This can't be the best solution here.

        // Actually I just looked at the Solutions tab and after 3 trials it's
        // consistently in the top 10% of solutions. Apparently backtracking truly is
        // the best way to tackle wildcards. No fancy 'used' tracking arrays,
        // just check every possible letter to substitute for the '.'
        for (int j = 0; j < 26; j++) {
            if (searchInNode(word, i + 1, node->children[j])) {
                return true;
            }
        }
        return false;
    }
};
