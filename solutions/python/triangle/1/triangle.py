def equilateral(sides):
    if sides[0] == 0:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if sides[0] == 0:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    if sides[0] == sides[1] and sides[1] > sides[2]:
        return True
    if sides[1] == sides[2] and sides[1] > sides[0]:
        return True
    if sides[0] == sides[2] and sides[2] > sides[1]:
        return True
    return False


def scalene(sides):
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return False
    if sides[0] == sides[2]:
        return False
    if sides[0] + sides[1] < sides[2]:
        return False
    if sides[1] + sides[2] < sides[0]:
        return False
    if sides[0] + sides[2] < sides[1]:
        return False
    return True