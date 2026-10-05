# ICPC Learn - Học từ số 0

Folder này chứa tài liệu học mới, viết lại từ đầu cho người mới.
Không sửa cheatsheet cũ.

## Lộ trình

| Thứ tự | Folder | Nội dung | Thời gian |
|---|---|---|---|
| 1 | `01-fenwick/` | Mảng cộng dồn động, nghịch thế, K-th one | 1-2 buổi |
| 2 | `02-rmq-lca/` | Sparse Table, LCA binary lifting | 2 buổi |
| 3 | `03-dinic-flow/` | Max flow Dinic, matching, min-cut | 2-3 buổi |
| 4 | `04-supplement/` | DSU, topo, đường ngắn, tổ hợp mod, hull, Aho | ôn dần |

## Cách học mỗi bài

1. Đọc `README.md` trong folder bài đó (lý thuyết + ví dụ tay).
2. Đọc `template.cpp` (code chuẩn để in mang vào phòng thi).
3. Tự gõ lại template, không copy-paste.
4. Làm bài tập cuối file, ít nhất 2/4 bài.

## Quy ước chung

* Code C++17, 1-based cho Fenwick, 0-based hay 1-based nói rõ cho từng bài.
* Mọi `sum` dùng `long long`.
* Compile test: `g++ -std=c++17 -O2 -Wall template.cpp -o /tmp/opencode/t && /tmp/opencode/t`
