#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 针对 2*10^5 的数据量，每个数字 30 位，节点数最大约为 2*10^5 * 31
const int MAX_NODES = 6200005; 

class BinaryTrie {
public:
    int trie[MAX_NODES][2];
    int size;
    int max_bits;

    BinaryTrie(int bits) {
        max_bits = bits;
        size = 0;
        // 初始化根节点
        trie[0][0] = trie[0][1] = 0;
    }

    void insert(int num) {
        int curr = 0;
        for (int i = max_bits; i >= 0; --i) {
            int bit = (num >> i) & 1;
            if (!trie[curr][bit]) {
                size++;
                trie[size][0] = trie[size][1] = 0;
                trie[curr][bit] = size;
            }
            curr = trie[curr][bit];
        }
    }

    // 这里按照你 Python 原版的逻辑：返回“能产生最大异或值的那个数字”
    int query_best_match(int num) {
        int curr = 0;
        int best_match = 0;
        for (int i = max_bits; i >= 0; --i) {
            int bit = (num >> i) & 1;
            int target = 1 - bit;
            if (trie[curr][target]) {
                // 如果能走相反的路（让异或结果该位为1）
                best_match |= (target << i);
                curr = trie[curr][target];
            } else {
                // 只能走相同的路
                best_match |= (bit << i);
                curr = trie[curr][bit];
            }
        }
        return best_match;
    }
};

// 全局变量以避免栈溢出
BinaryTrie bt(29); 

int main() {
    // 优化 I/O 速度
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }

    int current_prefix_xor = 0;
    int ans = 0;

    // 初始插入 0，代表空子数组的前缀异或和
    bt.insert(0);

    for (int i = 0; i < n; ++i) {
        current_prefix_xor ^= x[i];
        
        // 找到之前的前缀和中，能与当前前缀和异或出最大值的那个数
        int best_prev_xor = bt.query_best_match(current_prefix_xor);
        ans = max(ans, current_prefix_xor ^ best_prev_xor);
        
        // 将当前前缀和存入 Trie
        bt.insert(current_prefix_xor);
    }

    cout << ans << endl;

    return 0;
}