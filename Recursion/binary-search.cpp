// class Solution {
// public:
//         int recursion(vector<int>& nums , int target , int low , int high ){
//         int mid = low + (high-low)/2;
//         if(low>high){
//             return -1;
//         }
//         if(nums[mid]==target){
//             return mid;
//         }
//         else if(nums[mid]>target){
//            return recursion( nums , target ,low ,mid-1);
//         }
//         else{
//         return recursion(nums , target ,mid+1 ,high);
//         }
//     }
//     int search(vector<int>& nums, int target) {
//         int x = nums.size()-1;
//         return recursion( nums,target ,0 ,x );
//     }
// };