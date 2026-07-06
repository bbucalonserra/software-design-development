import unittest

def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX > boxTopCornerX + boxWidth:
        return False
    
    if pointY > boxTopCornerY + boxHeight:
        return False

    if pointX < boxTopCornerX:
        return False

    if pointY < boxTopCornerY:
        return False

    return True


class TestCollision(unittest.TestCase):
    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

    def test_point_outside_box(self):
        result = point_is_in_box(15, 15, 0, 0, 10, 10)
        self.assertFalse(result)

    def test_point_left_of_box(self):
        result = point_is_in_box(-1, 5, 0, 0, 10, 10)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()