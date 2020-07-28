import unittest
from mower import Direction
from mower import Mower

class TestMowerMethods(unittest.TestCase):

    def test_str_to_direction_should_return_unknown(self):
        mower = Mower(0,0,0,0,0,'@',None)
        self.assertTrue(mower.direction == Direction.UNKNOWN)

    def test_str_to_direction_should_not_be_case_sensitive(self):
        mower1 = Mower(0,0,0,0,0,'N',None)
        mower2 = Mower(0,0,0,0,0,'n',None)

        self.assertTrue(mower1.direction == Direction.NORTH)
        self.assertTrue(mower2.direction == Direction.NORTH)

    def test_str_to_direction_should_parse_correctly_inputs(self):
        mower1 = Mower(0,0,0,0,0,'N',None)
        mower2 = Mower(0,0,0,0,0,'S',None)
        mower3 = Mower(0,0,0,0,0,'E',None)
        mower4 = Mower(0,0,0,0,0,'W',None)

        self.assertTrue(mower1.direction == Direction.NORTH)
        self.assertTrue(mower2.direction == Direction.SOUTH)
        self.assertTrue(mower3.direction == Direction.EAST)
        self.assertTrue(mower4.direction == Direction.WEST)


    def test_rotate_left_should_modify_direction_to_the_left(self):
        mower1 = Mower(0,0,0,0,0,'N',None)
        self.assertTrue(mower1.direction == Direction.NORTH)
        mower1.rotate_left()
        self.assertTrue(mower1.direction == Direction.WEST)
        mower1.rotate_left()
        self.assertTrue(mower1.direction == Direction.SOUTH)
        mower1.rotate_left()
        self.assertTrue(mower1.direction == Direction.EAST)
        mower1.rotate_left()
        self.assertTrue(mower1.direction == Direction.NORTH)

    def test_rotate_right_should_modify_direction_to_the_right(self):
        mower1 = Mower(0,0,0,0,0,'N',None)
        self.assertTrue(mower1.direction == Direction.NORTH)
        mower1.rotate_right()
        self.assertTrue(mower1.direction == Direction.EAST)
        mower1.rotate_right()
        self.assertTrue(mower1.direction == Direction.SOUTH)
        mower1.rotate_right()
        self.assertTrue(mower1.direction == Direction.WEST)
        mower1.rotate_right()
        self.assertTrue(mower1.direction == Direction.NORTH)

    def test_move_forward_shoud_not_move_if_on_south_lawn_border(self):
        mower1 = Mower(0,0,0,5,5,'S',None)
        pos_x_before = mower1.pos_x
        pos_y_before = mower1.pos_y
        mower1.move_forward()
        pos_x_after = mower1.pos_x
        pos_y_after = mower1.pos_y
        self.assertEqual(pos_x_before,pos_x_after,'position x before and after do not match')
        self.assertEqual(pos_y_before,pos_y_after,'position y before and after do not match')

    def test_move_forward_shoud_not_move_if_on_north_lawn_border(self):
        mower1 = Mower(0,0,5,5,5,'N',None)
        pos_x_before = mower1.pos_x
        pos_y_before = mower1.pos_y
        mower1.move_forward()
        pos_x_after = mower1.pos_x
        pos_y_after = mower1.pos_y
        self.assertEqual(pos_x_before,pos_x_after,'position x before and after do not match')
        self.assertEqual(pos_y_before,pos_y_after,'position y before and after do not match')

    def test_move_forward_shoud_not_move_if_on_east_lawn_border(self):
        mower1 = Mower(0,5,5,5,5,'E',None)
        pos_x_before = mower1.pos_x
        pos_y_before = mower1.pos_y
        mower1.move_forward()
        pos_x_after = mower1.pos_x
        pos_y_after = mower1.pos_y
        self.assertEqual(pos_x_before,pos_x_after,'position x before and after do not match')
        self.assertEqual(pos_y_before,pos_y_after,'position y before and after do not match')

    def test_move_forward_shoud_not_move_if_on_west_lawn_border(self):
        mower1 = Mower(0,0,5,5,5,'W',None)
        pos_x_before = mower1.pos_x
        pos_y_before = mower1.pos_y
        mower1.move_forward()
        pos_x_after = mower1.pos_x
        pos_y_after = mower1.pos_y
        self.assertEqual(pos_x_before,pos_x_after,'position x before and after do not match')
        self.assertEqual(pos_y_before,pos_y_after,'position y before and after do not match')

# shoud move forward

if __name__ == '__main__':
    unittest.main()

