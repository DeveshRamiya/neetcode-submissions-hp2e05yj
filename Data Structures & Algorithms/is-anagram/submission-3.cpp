class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::vector<int> nums(26,0);
        for (int i = 0; i < s.length(); i++) {
            nums[s[i] - 'a'] += 1;
            nums[t[i] - 'a'] -= 1;
        }
        for (int i : nums) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
};
