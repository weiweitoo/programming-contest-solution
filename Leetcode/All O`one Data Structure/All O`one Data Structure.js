// Runtime: 128 ms, faster than 75.00% of JavaScript online submissions for All O`one Data Structure.
// Memory Usage: 45.5 MB, less than 65.71% of JavaScript online submissions for All O`one Data Structure.

/**
 * Initialize your data structure here.
 */
var AllOne = function() {
    data = {}
};

/**
 * Inserts a new key <Key> with value 1. Or increments an existing key by 1. 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.inc = function(key) {
    if(data[key] === undefined){
        data[key] = 1
    }
    else{
        data[key] += 1
    }
};

/**
 * Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. 
 * @param {string} key
 * @return {void}
 */
AllOne.prototype.dec = function(key) {
    if(data[key] === undefined){
        return 
    }
    else if(data[key] === 1){
        delete data[key]
    }
    else{
        data[key] -= 1
    }
};

/**
 * Returns one of the keys with maximal value.
 * @return {string}
 */
AllOne.prototype.getMaxKey = function() {
    let length = Object.keys(data).length
    if(length == 0){
        return ""
    } 
    if(length == 1){
        return Object.keys(data)[0]
    }
    
    let max = Object.values(data)[0]
    let maxKey = Object.keys(data)[0]
    for (let [key, val] of Object.entries(data)){
        if (val > max){
            max = val
            maxKey = key
        }
    }
    return maxKey
};

/**
 * Returns one of the keys with Minimal value.
 * @return {string}
 */
AllOne.prototype.getMinKey = function() {
    let length = Object.keys(data).length
    if(length <= 0){
        return ""
    } 
    if(length == 1){
        return Object.keys(data)[0]
    }
    
    let max = Object.values(data)[0]
    let maxKey = Object.keys(data)[0]
    for (let [key, val] of Object.entries(data)){
        if (val < max){
            max = val
            maxKey = key
        }
    }
    return maxKey
};

/** 
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */