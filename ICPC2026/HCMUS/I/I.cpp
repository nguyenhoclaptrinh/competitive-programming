#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Tối ưu hóa I/O trong C++
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Số bước nhảy tối đa k thỏa mãn k(k+1)/2 <= n
    // k xấp xỉ sqrt(2 * n)
    int max_jump = sqrt(2.0 * n) + 5;
    
    // Khởi tạo mảng dp có kích thước đủ lớn để chứa cả những ô nảy ra ngoài bảng
    // Giá trị ban đầu là 0
    vector<long long> dp(n + max_jump, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> dp[i];
    }

    // Tìm k ban đầu cho p = n
    long long k = sqrt(2.0 * n) + 2;
    while (k * (k + 1) / 2 > n) {
        k--;
    }

    // Quy hoạch động từ n về 1
    for (int p = n; p >= 1; --p) {
        // Cập nhật k sao cho k(k+1)/2 <= p <= k(k+3)/2
        while (k * (k + 1) / 2 > p) {
            k--;
        }
        // Công thức truy hồi
        dp[p] += max(dp[p + k + 1], dp[p + k + 2]);
    }

    // Từ vị trí 0, heo Danh nhảy đến ô 1 hoặc ô 2
    long long ans = max(dp[1], dp[2]);
    
    cout << ans << "\n";

    return 0;
}
