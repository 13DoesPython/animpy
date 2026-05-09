from .coords import Coords

class Shapes:
    @staticmethod
    def rectangle(width, height, char="#"):
        return "\n".join([char * width for _ in range(height)])

    @staticmethod
    def circle(radius, char="#"):
        result = []
        for y in range(-radius, radius + 1):
            row = ""
            for x in range(-radius, radius + 1):
                if x**2 + y**2 <= radius**2:
                    row += char
                else:
                    row += " "
            result.append(row)
        return "\n".join(result)

    @staticmethod
    def polygon(points, char="#"):
        if not points:
            return ""

        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        grid = [[" " for _ in range(width)] for _ in range(height)]

        for point in points:
            x = point.x - min_x
            y = point.y - min_y
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = char

        return "\n".join("".join(row) for row in grid)

    @staticmethod
    def line(x1, y1, x2, y2, char="#"):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return char

        x_increment = dx / steps
        y_increment = dy / steps

        x, y = x1, y1
        for _ in range(steps + 1):
            points.append(Coords(round(x), round(y)))
            x += x_increment
            y += y_increment

        return Shapes.polygon(points, char)

    @staticmethod
    def triangle(x1, y1, x2, y2, x3, y3, char="#"):
        points = [Coords(x1, y1), Coords(x2, y2), Coords(x3, y3)]
        return Shapes.polygon(points, char)

    @staticmethod
    def ellipse(center_x, center_y, radius_x, radius_y, char="#"):
        result = []
        for y in range(-radius_y, radius_y + 1):
            row = ""
            for x in range(-radius_x, radius_x + 1):
                if (x**2 / radius_x**2) + (y**2 / radius_y**2) <= 1:
                    row += char
                else:
                    row += " "
            result.append(row)
        return "\n".join(result)

    @staticmethod
    def heart(size, char="#"):
        result = []
        for y in range(-size, size + 1):
            row = ""
            for x in range(-size, size + 1):
                if (x**2 + y**2 - size**2)**3 - x**2 * y**3 <= 0:
                    row += char
                else:
                    row += " "
            result.append(row)
        return "\n".join(result)