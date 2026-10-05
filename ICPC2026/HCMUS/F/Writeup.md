# ICPC 2026 HCMUS - Problem F: Wagon Sorting

## Phân tích bài toán
Bài toán yêu cầu chúng ta tìm giá trị $M$ lớn nhất sao cho có thể đưa các toa tàu mang số từ $1$ đến $M$ vào đường ray đích theo đúng thứ tự tăng dần $1, 2, \dots, M$. Chúng ta có 1 đường ray chính (nguồn), 1 đường ray đích, và 1 đường ray phụ.
Dựa vào luật di chuyển, đường ray phụ hoạt động chính xác như một cấu trúc dữ liệu **Hàng đợi (Queue)** (Vào trước ra trước - FIFO).

Một hoán vị có thể được sắp xếp bằng 1 hàng đợi khi và chỉ khi nó **không chứa mẫu 321**. Điều này tương đương với việc dãy có **độ dài dãy con giảm dài nhất (LDS) $\le 2$**, hay nói cách khác, dãy có thể được chia thành tối đa 2 dãy con tăng ngặt.

Tuy nhiên, bài toán chỉ yêu cầu sắp xếp các số từ $1$ đến $M$, các số $> M$ chỉ được phép nằm lại ở đường ray chính hoặc đi vào hàng đợi.
Nếu một phần tử $> M$ bị đẩy vào hàng đợi, nó sẽ không bao giờ được lấy ra (vì không được phép cho vào đích). Do hàng đợi là FIFO, phần tử $> M$ này sẽ **chặn** toàn bộ các phần tử đi vào hàng đợi sau nó.
Điều này dẫn đến hệ quả: **Bất kỳ phần tử $\le M$ nào nằm sau phần tử $> M$ đầu tiên đều KHÔNG ĐƯỢC phép đi vào hàng đợi**. Chúng bắt buộc phải đi thẳng từ đường ray chính vào đích. Vì chúng đi thẳng vào đích theo thứ tự xuất hiện, dãy các phần tử này phải tạo thành một dãy con **tăng ngặt**.

## Điều kiện để $M$ thỏa mãn
Giả sử kiểm tra tính hợp lệ của $M$:
1. Gọi dãy $S_{\le M}$ là dãy con của $S$ chỉ chứa các phần tử $\le M$. Dãy này phải có $\text{LDS} \le 2$.
2. Gọi $F_M$ là vị trí xuất hiện **đầu tiên** của một phần tử $> M$ trong $S$. Tập hợp các phần tử $\le M$ nằm **sau** vị trí $F_M$ phải tạo thành một dãy tăng ngặt.

Bằng chứng minh toán học, có thể thấy nếu $M$ thỏa mãn 2 điều kiện trên thì $M-1$ cũng sẽ thỏa mãn. Nhờ tính **đơn điệu (monotonic)** này, ta có thể dùng **Tìm kiếm nhị phân (Binary Search)** để tìm $M$ lớn nhất.

## Thuật toán
1. Khởi tạo khoảng tìm kiếm nhị phân $L = 1, R = N$.
2. Hàm `check(M)` chạy trong $O(N)$:
   - Trích xuất dãy $S_{\le M}$ và tìm vị trí $F_M$.
   - Kiểm tra $\text{LDS} \le 2$ của $S_{\le M}$ bằng thuật toán tham lam $O(N)$ (Duy trì 2 giá trị đuôi của 2 dãy tăng, luôn cố gắng nối vào đuôi lớn hơn để tối ưu).
   - Kiểm tra các phần tử $\le M$ nằm sau $F_M$ có tăng ngặt hay không.
3. Nếu `check(M)` trả về `true`, ta cập nhật kết quả và tìm $M$ lớn hơn ($L = M + 1$). Ngược lại, tìm $M$ nhỏ hơn ($R = M - 1$).

Độ phức tạp thời gian: $O(N \log N)$.
Độ phức tạp không gian: $O(N)$.

## Cài đặt (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> S;

bool check(int M) {
    vector<int> S_M;
    int F_M = -1;
    for (int i = 0; i < N; ++i) {
        if (S[i] <= M) {
            S_M.push_back(S[i]);
        }
        if (S[i] > M && F_M == -1) {
            F_M = i;
        }
    }
    
    // Kiểm tra LDS <= 2 của dãy S_M bằng cách chia thành 2 dãy con tăng
    int t1 = -1, t2 = -1;
    for (int x : S_M) {
        if (x > t2) {
            t2 = x;
        } else if (x > t1) {
            t1 = x;
        } else {
            return false; // Phát hiện mẫu 321
        }
    }
    
    // Kiểm tra các phần tử <= M nằm sau F_M phải là dãy tăng ngặt
    if (F_M != -1) {
        int last = -1;
        for (int i = F_M + 1; i < N; ++i) {
            if (S[i] <= M) {
                if (S[i] <= last) return false;
                last = S[i];
            }
        }
    }
    
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    if (!(cin >> N)) return 0;
    S.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }
    
    int low = 1, high = N, ans = 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    cout << ans << "\n";
    return 0;
}
```
