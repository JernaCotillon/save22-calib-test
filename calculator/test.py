import calculator2
import unittest


class TestCalculator(unittest.TestCase):

    def test_Add(self):
        self.assertEqual(calculator2.add(1,1),2)
        with self.assertRaises(TypeError):
            calculator2.add('1',1)

    def test_Subtract(self):
        self.assertEqual(calculator2.sub(1,1),0)


    def test_Multiply(self):
        self.assertEqual(calculator2.mul(1,1),1)


    def test_Divide(self):
        self.assertEqual(calculator2.div(1,1),1)

        with self.assertRaises(ZeroDivisionError):
            calculator2.div(10,0)

    def test_operator(self):
        self.assertEqual(calculator2.operator('+', 13,11),24)
        self.assertEqual(calculator2.operator('-', 15,-10),25)
        self.assertEqual(calculator2.operator('/', 16,2),8)
        self.assertEqual(calculator2.operator('*', 7,-3),-21)
        self.assertEqual(calculator2.operator(1, 'AB',3), None)
        
        
    def test_output(self):
        self.assertEqual(calculator2.output('+', 13,11,24), "13 + 11 = 24")
        

    # def test_op(self):
    #      self.assertEqual(calculator.inputop(self.mock_input),1)

    # def test_inputOne(self):
    #      self.assertEqual(calculator.int1(self.mock_input),1)

    # def test_inputTwo(self):
    #      self.assertEqual(calculator.int2(self.mock_input),1)
        
    def mock_input(self,prompt):
        return 1

    def mock_ope(self,prompt):
        return '+'
        
    # def test_success(self):
    #     num1 = calculator.int1(self.mock_input)
    #     ope = calculator.inputop(self.mock_ope)        
    #     num2 = calculator.int2(self.mock_input)
    #     ans = calculator.operator(ope, num1, num2)
    #     final = calculator.output(ope, num1, num2, ans)

    #     self.assertEqual(final, "1 + 1 = 2")

    def mock_input_N1(self,prompt):
        return 1

    def mock_input_Zero(self,prompt):
        return 0

    def mock_inputString(self,prompt):
        return 'A'

    # def test_DividedByZero (self):
    #     n1 = calculator2.int1(self.mock_input_N1)
    #     n2 = calculator2.int1(self.mock_input_Zero)
        
    #     try:
    #             self.assertEqual((n1/n2), None )
    #     except ZeroDivisionError:
    #             pass
    #     else:
    #             self.fail('Not a ZeroDivisionError')
        
    def test_DivideByZero(self):
        try:
            
            z = 1/0
        except ZeroDivisionError:
            print "Zero Division Error"
    
    def test_StringInputs (self):
         try:
               self.assertEqual(calculator2.int1(self.mock_inputString),1)
               self.assertEqual(calculator2.inputop(self.mock_ope),'+')
               self.assertEqual(calculator2.int2(self.mock_inputString), 1) 
                
         except ValueError:
                print "Invalid Input"
         else:
                self.fail('Did not see StringInputs')


    def test_IntAndString(self):
        
         try:
               self.assertEqual(calculator2.int1(self.mock_inputString),1)
               self.assertEqual(calculator2.inputop(self.mock_ope),'+')
               self.assertEqual(calculator2.int2(self.mock_input_N1), 1) 
                
         except ValueError:
                print "Invalid Input"
         else:
                self.fail('Did not see StringInputs')

if __name__ == '__main__':
    unittest.main()