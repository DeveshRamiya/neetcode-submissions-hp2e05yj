class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> s;
        for (int x : nums) {
            if (s.count(x)) {
                return true;
            } else {
                s.insert(x);
            }
        }
        return false;
    }
};