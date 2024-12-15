/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const sortedarr = nums.sort((a,b) => a-b)
    const duplic = [...new Set(sortedarr)]
    for(let i=0;i<duplic.length;i++){
        nums[i]=duplic[i]
    }
    return duplic.length

};