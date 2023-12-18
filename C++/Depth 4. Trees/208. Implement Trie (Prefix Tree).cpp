#include <string>
using namespace std;

class Trie {
    char val;
    vector<Trie*> nextChars;

    int find_nextChar(char c) {
        for (int i = 0; i < nextChars.size(); ++i) {
            if (nextChars[i]->val == c)
                return i;
        }
        return -1;
    }

    void insert_helper(Trie* &node, string &word,
        int start, int end) {
        if (start > end) {
            return;
        }
        if (node->val == word.at(start)) {
            insert_helper(nextChars[find_nextChar(node->val)], 
                word, start+1, end);
            return;
        }
        
    }
public:
    Trie() : val{'\0'}, nextChars{}
    {}

    void insert(string word) {
        insert_helper(this, word, 0, word.size()-1);
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */