import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_4_and_5_is_9(self):
        self.assertEqual(extend.add(4, 5), 9)

    def test_add_2_and_1_is_3(self):
        self.assertEqual(extend.add(2, 1), 3)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(6, 10, 2), 10)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(8, 4, 10), 10)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,4]), 4.5)

    def test_median_five(self):
        self.assertEqual(extend.median([2,3,8,4,4]), 4)

    def test_is_vovel_b(self):
        self.assertFalse(extend.is_vovel('b'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_alma(self):
        self.assertEqual(extend.translate('alma'), 'avalmava')

if __name__ == '__main__':
    unittest.main()
