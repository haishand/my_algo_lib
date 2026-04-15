class BinaryTrie(val maxBits: Int, maxNodes: Int) {
    // 模拟 Python 的 trie = [[0, 0]]
    val trie = Array(maxNodes + 1) { IntArray(2) }
    val count = IntArray(maxNodes + 1)
    var size = 0

    // 插入入口
    fun insert(num: Int) {
        _insert(0, maxBits, num)
    }

    // 递归插入逻辑
    private fun _insert(node: Int, mbits: Int, num: Int) {
        // 路径经过即增加计数
        count[node]++

        if (mbits < 0) return

        val bit = (num ushr mbits) and 1
        
        if (trie[node][bit] == 0) {
            size++
            // 这里的 trie[size] 已经在初始化时准备好了
            trie[node][bit] = size
        }
        
        _insert(trie[node][bit], mbits - 1, num)
    }

    // 查询最大异或值入口
    fun queryMaxXor(num: Int): Int {
        return _queryMaxXor(0, maxBits, num)
    }

    // 递归查询最大异或值逻辑
    private fun _queryMaxXor(node: Int, mbits: Int, num: Int): Int {
        if (mbits < 0) return 0

        val bit = (num ushr mbits) and 1
        val target = 1 - bit

        return if (trie[node][target] != 0) {
            // 能够走相反位：该位异或结果为 1，加上低位的递归结果
            (1 shl mbits) or _queryMaxXor(trie[node][target], mbits - 1, num)
        } else {
            // 只能走相同位：该位异或结果为 0
            _queryMaxXor(trie[node][bit], mbits - 1, num)
        }
    }
}

fun main() {
    val bt = BinaryTrie(30, 100000)
    
    bt.insert(123)
    bt.insert(243)
    
    println("Max XOR with 20: ${bt.queryMaxXor(20)}")
    // 调试打印根节点的 count (应该是 2)
    println("Root node count: ${bt.count[0]}")
}