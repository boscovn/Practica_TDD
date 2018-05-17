# -*- coding: utf-8 -*-

from .context import practica

import unittest


class TestBattery(unittest.TestCase):
    """Basic test cases."""

    def test_punctuation(self):
        assert practica.wordStats("*$%:") == []
    def test_caps(self):
        assert practica.wordStats("hola HOLA Hola") == ['hola 3']
    def test_repetition(self):
    	the_list = practica.wordStats(" htge j y5ht4 6u7k iuj6yh5t4g rg y6uk7 76 5y4t3t 4y56 iu54 t4y56 7i u54")
    	assert len(the_list)==len(set(the_list))

if __name__ == '__main__':
    unittest.main()