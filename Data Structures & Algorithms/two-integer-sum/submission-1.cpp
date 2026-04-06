class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            if (indices.find(nums[i]) == indices.end()) {
                indices[target - nums[i]] = i;
                cout << target -nums[i] << "index " << i << endl;
            }
            else {
                
                return {indices[nums[i]], i};
            }
        }
    }
};
