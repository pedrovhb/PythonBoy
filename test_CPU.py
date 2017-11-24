from unittest import TestCase

from cpu import *

class TestCPU(TestCase):

    #def

    def test_ld_r_n(self):

        cpu = CPU(memory=bytearray(0xFFFF*[0x00]))
        self.assertRaises(ValueError, cpu.ld_r_n, -1, 0)
        self.assertRaises(ValueError, cpu.ld_r_n, 256, 0)
        self.assertRaises(TypeError, cpu.ld_r_n, 3.4, 0)
        self.assertRaises(TypeError, cpu.ld_r_n, '3.4', 0)
        self.assertRaises(ValueError, cpu.ld_r_n, 0x06, -1)
        self.assertRaises(ValueError, cpu.ld_r_n, 0x06, 256)
        self.assertRaises(TypeError, cpu.ld_r_n, 0x06, 3.4)
        self.assertRaises(TypeError, cpu.ld_r_n, 0x06, '3.4')

        cpu.ld_r_n(0x06, 0x12)
        self.assertEqual(0x12, cpu.registers[b])
        #self.fail()

    def test_set_flag(self):  # Modify given flag
        c = CPU(memory=bytearray(0xFFFF*[0x00]))

        c.set_flag(f_c, 1)
        assert c.registers[f] % f_c == 0



    '''def test_ld_r1_r2(self):
        self.fail()

    def test_ld_ahl_r(self):
        self.fail()

    def test_ld_r_ahl(self):
        self.fail()

    def test_ld_ahl_n(self):
        self.fail()

    def test_ld_r_a(self):
        self.fail()

    def test_ld_arr_a(self):
        self.fail()

    def test_ld_ann_a(self):
        self.fail()

    def test_ld_a_ac(self):
        self.fail()

    def test_ld_ac_a(self):
        self.fail()

    def test_ld_a_an(self):
        self.fail()

    def test_ld_an_a(self):
        self.fail()'''
