class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): [number, number] | undefined {
        // nums.sort()
        const map =  new Map<number, number>()

        for (let i = 0; i < nums.length; i++ ){
            const val = nums[i]
            const comp = target - val

            const compIdx = map.get(comp)
            if (compIdx !== undefined) {
                return [compIdx, i]
            }
            map.set(val, i)
        }
        return undefined
    }
}
