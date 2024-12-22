/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const n= nums.length;
   for(i=0;i<n;i++){
     if(nums[i]==target){
         return i;
     }else if(target<nums[i])
     return i;
   }
   return i++;   
 };