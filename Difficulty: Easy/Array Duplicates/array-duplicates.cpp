#include <unordered_set>

class Solution {
  public:
    vector<int> findDuplicates(vector<int>& arr) {
        
        unordered_set<int> seen;
        unordered_set<int> duplicate;
        vector<int> result;

        for(int i = 0; i < arr.size(); i++){
            if(seen.count(arr[i])) {
                duplicate.insert(arr[i]);
            } else {
                seen.insert(arr[i]);
            }
        }

        for(auto x : duplicate){
            result.push_back(x);
        }

        if(result.empty()) return {};

        return result;
    }
};
