#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// O(log n) runtime, O(n) memory
// My Solution
class TimeMap {
    unordered_map<string, vector<pair<int, string> > >
        key_map;
public:
    TimeMap() {

    }
    
    void set(string key, string value, int timestamp) {
        if (!key_map.contains(key)) {
            key_map[key] = vector<pair<int, string> >();
        }
        key_map[key].push_back(make_pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        if (!key_map.contains(key) || 
                (timestamp < key_map[key][0].first) ) {
            return "";
        }
        // Binary search goes here
        int l = 0, r = key_map[key].size()-1, mid = 0;
        // target = timestamp
        while (l <= r) {
            mid = (l+r)/2;
            if (key_map[key][mid].first == timestamp)
                return key_map[key][mid].second;
            else if (key_map[key][mid].first < timestamp)
                l = mid + 1;
            else 
                r = mid - 1;
        }
        // Looked at the solution beyond this point
        // Realized that when the above loop finishes without a return
        // Target timestamp not found, and `r` is always 1 less than
        // `mid`, which becomes the closest min val to target `timestamp`
        return key_map[key][r].second;
    }
};