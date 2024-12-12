/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const str=x.toString()
    const y = str.split('').reverse().join('')
    if(str===y)
        return true
    else
        return false    
};