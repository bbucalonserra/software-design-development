import unittest


############################# Teste 1.1  RED #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    return None

class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


############################# Teste 1.2 GREEN #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if True:
        return True
    else:
        return False

class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


############################# Teste 1.3 REFACTOR #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    return True

class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


############################# Teste 2.1 RED #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    return True

class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

    def test_point_outside_box(self):
        result = point_is_in_box(15, 15, 0, 0, 10, 10)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


############################# Teste 2.2 GREEN #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX > boxTopCornerX + boxWidth:
        return False
    else:
        pass  # DEAD CODE

    if pointY > boxTopCornerY + boxHeight:
        return False
    else:
        pass  # DEAD CODE

    if True:
        return True
    else:
        return False  # DEAD CODE


class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

    def test_point_outside_box(self):
        result = point_is_in_box(15, 15, 0, 0, 10, 10)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()


############################# Teste 2.3 REFACTOR #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX > boxTopCornerX + boxWidth:
        return False

    if pointY > boxTopCornerY + boxHeight:
        return False
    
    return True


class TestCollision(unittest.TestCase):

    def test_point_inside_box(self):
        result = point_is_in_box(5, 5, 0, 0, 10, 10)
        self.assertTrue(result)

    def test_point_outside_box(self):
        result = point_is_in_box(15, 15, 0, 0, 10, 10)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()



############################# Teste 3.1 RED #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX > boxTopCornerX + boxWidth:
        return False

    if pointY > boxTopCornerY + boxHeight:
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

############################# Teste 3.2 GREEN #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX < boxTopCornerX:
        return False
    else:
        pass  # dead code

    if pointY < boxTopCornerY:
        return False
    else:
        pass  # dead code

    if pointX > boxTopCornerX + boxWidth:
        return False
    else:
        pass  # dead code

    if pointY > boxTopCornerY + boxHeight:
        return False
    else:
        pass  # dead code

    if True:
        return True
    else:
        return False  # dead code


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


############################# Teste 3.3 REFACTOR #############################
def point_is_in_box(pointX, pointY, boxTopCornerX, boxTopCornerY, boxWidth, boxHeight):
    if pointX < boxTopCornerX:
        return False
    
    if pointY < boxTopCornerY:
        return False
    
    if pointX > boxTopCornerX + boxWidth:
        return False
    
    if pointY > boxTopCornerY + boxHeight:
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