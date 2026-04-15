#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;

        string s;
        cin >> s;

        int x = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (s[i] == s[n - 1])
            {
                x++;
            }
            else
            {
                break;
            }
        }

        auto check = [&]()
        {
            for (int i = 0; i < k; i++)
            {
                if (s[i] != s[0])
                    return false;
            }
            for (int i = 0; i + k < n; i++)
            {
                if (s[i] == s[i + k])
                    return false;
            }
            return true;
        };

        auto operation = [&](int p)
        {
            reverse(s.begin(), s.begin() + p);
            s = s.substr(p, (int)s.size() - p) + s.substr(0, p);
            if (check())
            {
                cout << p << "\n";
            }
            else
            {
                cout << -1 << "\n";
            }
        };

        if (x == k)
        {
            int p = n;
            for (int i = n - 1 - k; i >= 0; i--)
            {
                if (s[i] == s[i + k])
                {
                    p = i + 1;
                    break;
                }
            }
            operation(p);
        }
        else if (x > k)
        {
            cout << -1 << "\n";
        }
        else
        {
            bool was = false;
            for (int i = 0; i < n; i++)
            {
                if (s[i] != s.back())
                    continue;
                int j = i;
                while (j + 1 < n && s[i] == s[j + 1])
                {
                    j++;
                }
                if (j - i + 1 + x == k)
                {
                    operation(j + 1);
                    was = true;
                    break;
                }
                else if (j - i + 1 - k + x == k)
                {
                    operation(i + k - x);
                    was = true;
                    break;
                }
                i = j;
            }
            if (!was)
            {
                operation(n);
            }
        }
    }
}