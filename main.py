import math
import plotext as plt


def put_next_max_ac(d, x, y):
    if x >= 2 and (x - 1) >= y:
        key = (x - 1) ** 2 + y**2
        if key not in d:
            d[key] = (x - 1, y)
    if y >= 2:
        key = x**2 + (y - 1) ** 2
        if key not in d:
            d[key] = (x, y - 1)


def pop_max_ac(d: dict):
    tmp = sorted(d.items(), reverse=True)
    max_ac2, (max_ac_x, max_ac_y) = next(iter(tmp))
    del d[max_ac2]
    put_next_max_ac(d, max_ac_x, max_ac_y)

    return max_ac2, (max_ac_x, max_ac_y)


def judge_square_sum(c, n):
    a = 0
    b = int(math.isqrt(c))  # 获取 c 的平方根的整数部分
    b = min(b, n)  # 确保 b 不超过 n

    while a <= b:
        total = a * a + b * b
        if total == c:
            return True
        elif total < c:
            a += 1
        else:
            b -= 1

    return False


def judge_valid_triangle(ab2, bc2, ac2, c_point, n):
    (cx, cy) = c_point
    tmp2 = ab2 + ac2 - bc2
    for i in range(0, n + 1):
        tmp = tmp2 - 2 * i * cx
        if tmp % (2 * cy) != 0:
            continue

        j = int(tmp / (2 * cy))
        if j > n or j < 0:
            continue

        if (i * i + j * j) != ab2 and (i - cx) * (i - cx) + (j - cy) * (j - cy) != bc2:
            continue

        return (i, j)

    return False


def max_similar_triangle(ab2, bc2, ac2, n):
    d = {}
    d[n * n * 2] = (n, n)

    while d:
        max_ac2, (cx, cy) = pop_max_ac(d)
        if (max_ac2 * ab2) % ac2 != 0 or (max_ac2 * bc2) % ac2 != 0:
            continue

        max_ab2 = max_ac2 * ab2 // ac2
        max_bc2 = max_ac2 * bc2 // ac2

        if (
            judge_square_sum(max_ab2, n) is False
            or judge_square_sum(max_bc2, n) is False
        ):
            continue

        b_point = judge_valid_triangle(max_ab2, max_bc2, max_ac2, (cx, cy), n)
        if b_point is False:
            continue

        return b_point, (cx, cy)

    return False, False


def draw_triangle(b_point, c_point, n):
    plt.clf()
    plt.plot_size(width=80, height=30)
    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.xticks(range(0, n + 1))
    plt.yticks(range(0, n + 1))

    plt.xlabel("X")
    plt.ylabel("Y")

    (bx, by) = b_point
    (cx, cy) = c_point

    draw_x = [0, bx, cx]
    draw_y = [0, by, cy]

    draw_x = draw_x + [draw_x[0]]
    draw_y = draw_y + [draw_y[0]]

    plt.plot(draw_x, draw_y)
    plt.show()


def main():
    try:
        while True:
            try:
                ab2, bc2, ac2, n = map(
                    int,
                    input(
                        "请输入三角形三边的平方数和正方形的格数（空格隔开）："
                    ).split(),
                )

                (b_poinx, c_point) = max_similar_triangle(ab2, bc2, ac2, n)

                if b_poinx is False or c_point is False:
                    print("没有找到符合条件的三角形", end=" ")
                else:
                    draw_triangle(b_poinx, c_point, n)
                    print(f"b{b_poinx}, c{c_point}", end=" ")

                print("或按 Ctrl+C 退出\n")
            except ValueError:
                print("输入格式错误\n")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
