import math
import plotext as plt
import heapq


def get_max_c_point(d):
    max_ac2, max_ac_x, max_ac_y = heapq.heappop(d)

    if max_ac_x >= 2 and (max_ac_x - 1) >= max_ac_y:
        key = (max_ac_x - 1) ** 2 + max_ac_y**2
        if key not in d:
            heapq.heappush(d, (-key, max_ac_x - 1, max_ac_y))
    if max_ac_y >= 2:
        key = max_ac_x**2 + (max_ac_y - 1) ** 2
        if key not in d:
            heapq.heappush(d, (-key, max_ac_x, max_ac_y - 1))

    return -max_ac2, (max_ac_x, max_ac_y)


def get_max_b_point(ab2, bc2, ac2, c_point, n):
    # 理解为圆心（0，0）（cx, cy), 半径分别为 ab，和 bc 画圆 的 交点
    # 如果没有实数解，为False，如果有，取 [0-n] 内任意的整数解
    # 整理出一元二次方程，
    (cx, cy) = c_point
    t = ab2 + ac2 - bc2

    sqrt2 = t * t * (cx * cx - ac2) + 4 * ac2 * cy * cy * ab2

    sqrt_tmp = math.isqrt(sqrt2)

    if sqrt_tmp**2 != sqrt2:
        return False

    root = t * cx + sqrt_tmp
    if root % (2 * ac2) != 0:
        root = t * cx - sqrt_tmp

        if root < 0:
            return False

        if root % (2 * ac2) != 0:
            return False

    bx = root // (2 * ac2)
    if bx > n:
        return False

    by2 = ab2 - bx * bx
    by = math.isqrt(by2)
    if by**2 != by2:
        return False

    if (cx - bx) ** 2 + (cy - by) ** 2 != bc2:
        return False

    return (bx, by)


def max_similar_triangle(ab2, bc2, ac2, n):
    d = []
    heapq.heappush(d, (-n * n * 2, n, n))

    while d:
        max_ac2, (cx, cy) = get_max_c_point(d)
        if (max_ac2 * ab2) % ac2 != 0 or (max_ac2 * bc2) % ac2 != 0:
            continue

        max_ab2 = max_ac2 * ab2 // ac2
        max_bc2 = max_ac2 * bc2 // ac2

        b_point = get_max_b_point(max_ab2, max_bc2, max_ac2, (cx, cy), n)
        if b_point:
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

                (b_point, c_point) = max_similar_triangle(ab2, bc2, ac2, n)

                if b_point is False or c_point is False:
                    print("没有找到符合条件的三角形", end=" ")
                else:
                    draw_triangle(b_point, c_point, n)
                    print(f"b{b_point}, c{c_point}", end=" ")

                print("或按 Ctrl+C 退出\n")
            except ValueError:
                print("输入格式错误\n")
    except KeyboardInterrupt:
        pass


def test():
    (b_point, c_point) = max_similar_triangle(9, 16, 25, 7)
    draw_triangle(b_point, c_point, 7)


def benchmark():
    for nx in range(4, 20):
        for ny in range(4, 20):
            for bx in range(1, nx):
                for by in range(0, ny):
                    ab2 = bx**2 + by**2
                    bc2 = (nx - bx) ** 2 + (ny - by) ** 2
                    ac2 = nx**2 + ny**2
                    print(f"ab2: {ab2}, bc2: {bc2}, ac2: {ac2}, n: {nx + ny}")
                    (b_point, c_point) = max_similar_triangle(ab2, bc2, ac2, nx + ny)
                    print(b_point, c_point, nx + ny)


if __name__ == "__main__":
    main()
    # benchmark()
    # test()
