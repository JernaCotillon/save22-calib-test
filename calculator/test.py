import calculator2
import unittest


class TestCalculator(unittest.TestCase):

    def test_Add(self):
        self.assertEqual(calculator2.add(1,1),2)
        with self.assertRaises(TypeError):
            calculator2.add('1',1)

    def test_Sub(self):
        self.assertEqual(calculator2.sub(1,1),0)


    def test_Mul(self):
        self.assertEqual(calculator2.mul(1,1),1)


    def test_Div(self):
        self.assertEqual(calculator2.div(1,1),1)

        with self.assertRaises(ZeroDivisionError):
            calculator2.div(10,0)

    def test_StringInputs(self):
        pass
        #with self.assertRaises(ValueError):
        #    calculator2.add("A","A")

    def test_IntAndString(self):
        pass
        #"""1+A"""
        #self.fail("This is an expected failure")

    def test_DivideByZero(self):
        try:
            z = 1/0
        except ZeroDivisionError as e:
            print e # output: "Zero Division Error"

    def test_operator(self):
        self.assertEqual(calculator2.operator('+', 13,11),24)
        self.assertEqual(calculator2.operator('-', 15,-10),25)
        self.assertEqual(calculator2.operator('/', 16,2),8)
        self.assertEqual(calculator2.operator('*', 7,-3),-21)
        #self.assertEqual(calculator2.operator(1, 'AB',3), None)
        
        
    def test_output(self):
        self.assertEqual(calculator2.output('+', 13,11,24), "13 + 11 = 24")
        

    # def test_op(self):
    #      self.assertEqual(calculator2.inputop(self.mock_input),1)

    # def test_inputOne(self):
    #      self.assertEqual(calculator2.input1(self.mock_input),1)

    # def test_inputTwo(self):
    #      self.assertEqual(calculator2.input2(self.mock_input),1)
        

    def mock_input(self,prompt):
        return 1

    
    def mock_ope(self,prompt):
        return '+'
        
    # def test_success(self):
    #     num1 = calculator2.input1(self.mock_input)
    #     ope = calculator2.inputop(self.mock_ope)        
    #     num2 = calculator2.input2(self.mock_input)
    #     ans = calculator2.operator(ope, num1, num2)
    #     finalOutput = calculator2.output(ope, num1, num2, ans)

    #     self.assertEqual(finalOutput, "1 + 1 = 2")

if __name__ == '__main__':
    unittest.main()