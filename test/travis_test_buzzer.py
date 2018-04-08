#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

class BuzzerTest(unittest.TestCase):

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/buzzer',nodes, "node does not exist")

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_buzzer')
    rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)

# Copyright 2016 Ryuichi Ueda
# Released under the BSD License.
# To make line numbers be identical with the book, this statement is written here. Don't move it to the header.
