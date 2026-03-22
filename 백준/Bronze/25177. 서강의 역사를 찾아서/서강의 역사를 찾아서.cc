#include <bits/stdc++.h>
using namespace std;
#include <algorithm>

#define fastio ios::sync_with_stdio(false); cin.tie(nullptr);

int main() {
    fastio;

    int N, M;
    cin >> N >> M;

    vector<int> arr(max(N,M));
    vector<int> res(max(N,M));

    for (int i = 0; i < N; i++) 
        cin >> arr[i];

    for (int i = 0; i < M; i++) {
        int x, y;    
        cin >> x;
        y = x - arr[i];
        if (y > 0) {
            res[i] = x - arr[i];
        } else res[i] = 0;
    }

    int max_val = *std::max_element(std::begin(res), std::end(res));

    cout << max_val;
    
    return 0;
}