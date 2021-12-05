from collections import Counter

# https://github.com/encukou/bresenham/blob/master/bresenham.py
def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def main():
    with open("day5_input.txt") as f:
        
        lines = []
        for line in f.readlines():
            start, end = line.split('->')
            start_x = int(start.strip().split(',')[0])
            start_y = int(start.strip().split(',')[1])
            end_x = int(end.strip().split(',')[0])
            end_y = int(end.strip().split(',')[1])
            lines.append(((start_x, start_y), (end_x, end_y)))

        points = []
        for line in lines:
            start, end = line
            for point in bresenham(*start, *end):
                points.append(point)

        count = 0
        for number in Counter(points).values():
            count += number >= 2

        print(count)


main()