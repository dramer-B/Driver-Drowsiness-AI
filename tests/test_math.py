import unittest
import sys
import os
import numpy as np

# Add the parent folder to path so we can import 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils

class TestDrowsinessMath(unittest.TestCase):

    def test_ear_calculation(self):
        """Test if EAR formula works on a perfect square eye"""
        # Create a fake eye (Square shape)
        # Points: (0,0), (1,1), (2,1), (3,0), (2,-1), (1,-1)
        fake_eye = [
            (0, 0),  # P1 (Left corner)
            (1, 1),  # P2 (Top Left)
            (2, 1),  # P3 (Top Right)
            (3, 0),  # P4 (Right Corner)
            (2, -1), # P5 (Bottom Right)
            (1, -1)  # P6 (Bottom Left)
        ]

        # The vertical distance is 2 (from 1 to -1)
        # The horizontal distance is 3 (from 0 to 3)
        # Formula: (2 + 2) / (2 * 3) = 4 / 6 = 0.666...

        result = utils.eye_aspect_ratio(fake_eye)

        # Assert that the result is close to 0.666
        self.assertAlmostEqual(result, 0.6666666666666666, places=5)
        print(f"\n[TEST PASSED] Calculated EAR: {result:.4f} (Expected ~0.6667)")

if __name__ == '__main__':
    unittest.main()
