#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 全域變量，方便在函數間訪問，避免過多的參數傳遞
vector<int> adj[100005]; // 鄰接表
int c[100005];           // 存儲節點的 c 值
bool vis[100005];        // 訪問標記
vector<int> ans;         // 存儲結果

void dfs(int x)
{
    if (vis[x])
        return;
    vis[x] = true;

    // logic: all &= c[y] 表示檢查所有子節點的 c 值是否都為 1
    // 如果沒有子節點，all 保持為 1
    int all = 1;
    for (int y : adj[x])
    {
        if (c[y] == 0)
        {
            all = 0; // 只要有一個子節點不尊重(c=0)，all 就變成 0
        }
        dfs(y);
    }

    // 如果自己不尊重(c=1)且所有子節點也不尊重(all=1)，則可以刪除
    if (all == 1 && c[x] == 1)
    {
        ans.push_back(x);
    }
}

int main()
{
    // 優化 C++ 的輸入輸出速度，這兩行對 CP 非常重要
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    if (!(cin >> n))
        return 0;

    int root = -1;
    for (int i = 1; i <= n; i++)
    {
        int p, val;
        cin >> p >> val;
        c[i] = val;
        if (p == -1)
        {
            root = i;
        }
        else
        {
            adj[p].push_back(i); // p 是父節點，i 是子節點
        }
    }

    if (root != -1)
    {
        dfs(root);
    }

    // 題目要求排序輸出
    sort(ans.begin(), ans.end());

    if (ans.empty())
    {
        cout << -1 << endl;
    }
    else
    {
        for (int i = 0; i < ans.size(); i++)
        {
            cout << ans[i] << (i == ans.size() - 1 ? "" : " ");
        }
        cout << endl;
    }

    return 0;
}
