import unittest
import operaciones
import math


class TestOperacionesComplejos(unittest.TestCase):

    def test_suma_1(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)

        resultado = operaciones.suma(c1, c2)

        self.assertAlmostEqual(resultado[0], 2.2)
        self.assertAlmostEqual(resultado[1], -2.7)

    def test_suma_2(self):
        c1 = (1, 2)
        c2 = (3, 4)

        resultado = operaciones.suma(c1, c2)

        self.assertEqual(resultado, (4, 6))



    def test_producto_1(self):
        c1 = (3, 2)
        c2 = (-1, 4)

        resultado = operaciones.producto(c1, c2)

        self.assertEqual(resultado, (-11, 10))

    def test_producto_2(self):
        c1 = (1, 1)
        c2 = (1, -1)

        resultado = operaciones.producto(c1, c2)

        self.assertEqual(resultado, (2, 0))



    def test_resta_1(self):
        c1 = (5, 7)
        c2 = (3, -2)

        resultado = operaciones.resta(c1, c2)

        self.assertEqual(resultado, (2, 9))

    def test_resta_2(self):
        c1 = (8, 6)
        c2 = (2, 1)

        resultado = operaciones.resta(c1, c2)

        self.assertEqual(resultado, (6, 5))



    def test_division_1(self):
        c1 = (12, 1)
        c2 = (1, 4)

        resultado = operaciones.division(c1, c2)

        self.assertAlmostEqual(resultado[0], 16 / 17)
        self.assertAlmostEqual(resultado[1], -47 / 17)

    def test_division_2(self):
        c1 = (4, 2)
        c2 = (1, 1)

        resultado = operaciones.division(c1, c2)

        self.assertAlmostEqual(resultado[0], 3)
        self.assertAlmostEqual(resultado[1], -1)


    def test_modulo_1(self):
        self.assertEqual(operaciones.modulo((3, 4)), 5)

    def test_modulo_2(self):
        self.assertEqual(operaciones.modulo((5, 12)), 13)


    def test_conjugado_1(self):
        self.assertEqual(operaciones.conjugado((2, -3)), (2, 3))

    def test_conjugado_2(self):
        self.assertEqual(operaciones.conjugado((4, 5)), (4, -5))


    def test_polar_a_cartesiano_1(self):
        resultado = operaciones.polar_a_cartesiano((2, math.pi / 3))

        self.assertAlmostEqual(resultado[0], 1)
        self.assertAlmostEqual(resultado[1], math.sqrt(3))

    def test_polar_a_cartesiano_2(self):
        resultado = operaciones.polar_a_cartesiano((5, 0))

        self.assertAlmostEqual(resultado[0], 5)
        self.assertAlmostEqual(resultado[1], 0)



    def test_cartesiano_a_polar_1(self):
        resultado = operaciones.cartesiano_a_polar((3, 4))

        self.assertAlmostEqual(resultado[0], 5)
        self.assertAlmostEqual(resultado[1], math.atan2(4, 3))

    def test_cartesiano_a_polar_2(self):
        resultado = operaciones.cartesiano_a_polar((5, -2))

        self.assertAlmostEqual(resultado[0], math.sqrt(29))
        self.assertAlmostEqual(resultado[1], math.atan2(-2, 5))


    def test_fase_1(self):
        self.assertAlmostEqual(
            operaciones.fase((1, 1)),
            math.pi / 4
        )

    def test_fase_2(self):
        self.assertAlmostEqual(
            operaciones.fase((0, 1)),
            math.pi / 2
        )


if __name__ == "__main__":
    unittest.main()
