class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double window_sum=0,max_sum=0;

        for(int i=0;i<k;i++){
            max_sum+=nums[i];
        }
        window_sum=max_sum;

        for (int j=k;j<nums.size();j++){
            window_sum+=nums[j]-nums[j-k];
            max_sum=max(window_sum,max_sum);
        }

        return(max_sum/k);
    }
};