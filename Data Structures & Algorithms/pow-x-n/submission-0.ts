class Solution {
    /**
     * @param {number} x
     * @param {number} n
     * @return {number}
     */
    myPow(x: number, n: number): number {
        if (n < 0) {
            return 1 / this.myPow(x, -n);
        }

        if (n === 0) {
            return 1;
        }

        const half = this.myPow(x, Math.floor(n / 2));

        if (n % 2 === 0) {
            return half * half;
        }
        return x * half * half;
    }
}
