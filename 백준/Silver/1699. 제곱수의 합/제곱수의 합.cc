#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> dp(n + 1); 
    for (int i = 0; i <= n; i++) {
        dp[i] = i;  
    }
    
    for (int i = 1; i <= n; i++) {
        int j = 1;
        while (j * j <= i) {
            dp[i] = min(dp[i], dp[i - j * j] + 1);
            j++;
        }
    }
    
    cout << dp[n] << endl;
    return 0;
}