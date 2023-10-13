import curses
import math
import time

def render_donut(stdscr, A, B):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)

    while True:
        z = [0] * (A*B)
        b = [' '] * (A*B)

        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                c = int(math.sin(i) * 1000 + math.cos(j) * 1000)
                d = int(math.cos(i) * 1000 - math.sin(j) * 1000)
                e = int((math.sin(i) + math.cos(j)) * 1000)
                f = int(math.sin(j) * 1000)
                g = int(math.cos(i) * 1000)
                h = int(B + B * c / (f + 6))
                l = int(A + A * d / (f + 6))
                m = int(A + A * e / (f + 6))
                n = int(B + B * g / (f + 6))
                t = int(0.98 * ((A * A) / (m * h + 1) + (B * B) / (n * l + 1)))
                u = int((0.98 * (h * l - m * n) / ((m * h - n * l) + 2) + A / 2))
                v = int((0.98 * (h * n + l * m) / ((m * h - n * l) + 2) + B / 2))
                w = int(8 * ((g * e - f * d) / (f * h - d * e) + A / 2))
                x = int(8 * ((g * d + f * e) / (f * h - d * e) + B / 2))
                if 0 <= v < A and 0 <= u < B and 0 <= x < A and 0 <= w < B:
                    i = int((w * A) + x)
                    j = int((u * B) + v)
                    q = int((x * A) + w)
                    r = int((v * B) + u)
                    z[int(i)] += t
                    b[int(i)] = '.,-~:;=!*#$@'[int((t * 69 / 100))]

        output = [' '] * (A*B)
        for k in range(0, A*B):
            j = int((k / A) % B)
            i = int(k % A)
            c = int(z[k])
            if j < B and i < A and c > 0:
                output[int((j * A) + i)] = b[int((j * A) + i)]
        output_str = ''.join(output)

        win.addstr(0, 0, output_str)
        win.refresh()

        time.sleep(0.05)
        win.clear()

def main(stdscr):
    A = 80
    B = 24
    curses.wrapper(render_donut, A, B)

if __name__ == '__main__':
    main()
