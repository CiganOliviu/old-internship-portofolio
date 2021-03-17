using System;
using ESharp.ESharpSourceCode.NumbersAlgorithms;
using NUnit.Framework;

namespace TestESharp
{
    public class NumbersAlgorithmsTests
    {

        private IAbstractNumbersAlgorithms _numbersAlgorithms;
        
        [SetUp]
        public void Setup()
        {
            _numbersAlgorithms = NumbersAlgorithmsFactoryObject.GetNumbersAlgorithmsObject();
        }

        [Test]
        public void Test_GetTheLargestCommonDivisor_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisor(8, 12) == 4);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisor(1, 2) == 1);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisor(36, 69) == 3);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisor(100, 50) == 50);
        }
        
        [Test]
        public void Test_GetTheLargestCommonDivisorRecursive_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisorRecursive(8, 12) == 4);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisorRecursive(1, 2) == 1);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisorRecursive(36, 69) == 3);
            Assert.IsTrue(_numbersAlgorithms.GetTheLargestCommonDivisorRecursive(100, 50) == 50);
        }
     
        [Test]
        public void Test_GetTheLeastCommonMultiple_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetTheLeastCommonMultiple(8, 12) == 24);
            Assert.IsTrue(_numbersAlgorithms.GetTheLeastCommonMultiple(1, 2) == 2);
            Assert.IsTrue(_numbersAlgorithms.GetTheLeastCommonMultiple(200, 324) == 16200);
            Assert.IsTrue(_numbersAlgorithms.GetTheLeastCommonMultiple(100, 50) == 100);
        }
        
        [Test]
        public void Test_GetValueIfPrime_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetValueIfPrime(12) == 0);
            Assert.IsTrue(_numbersAlgorithms.GetValueIfPrime(25) == 0);
            Assert.IsTrue(_numbersAlgorithms.GetValueIfPrime(13) == 13);
            Assert.IsTrue(_numbersAlgorithms.GetValueIfPrime(23) == 23);
        }
        
        [Test]
        public void Test_ReverseNumber_()
        {
            Assert.IsTrue(_numbersAlgorithms.ReverseNumber(12) == 21);
            Assert.IsTrue(_numbersAlgorithms.ReverseNumber(25) == 52);
            Assert.IsTrue(_numbersAlgorithms.ReverseNumber(1369895) == 5989631);
            Assert.IsTrue(_numbersAlgorithms.ReverseNumber(333) == 333);
        }
        
        [Test]
        public void Test_GetPalindromeNumber_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetPalindromeNumber(121) == 121);
            Assert.IsTrue(_numbersAlgorithms.GetPalindromeNumber(25) == 0);
            Assert.IsTrue(_numbersAlgorithms.GetPalindromeNumber(1369895) == 0);
            Assert.IsTrue(_numbersAlgorithms.GetPalindromeNumber(333) == 333);
        }
        
        [Test]
        public void Test_GetMeanOfTwoNumbers_()
        {
            Assert.IsTrue(Math.Abs(_numbersAlgorithms.GetMeanOfTwoNumbers(121, 122) - 121.5) < 3);
            Assert.IsTrue(Math.Abs(_numbersAlgorithms.GetMeanOfTwoNumbers(123, 432) - 277.5) < 3);
            Assert.IsTrue(Math.Abs(_numbersAlgorithms.GetMeanOfTwoNumbers(213123, 1369895) - 791509) < 3);
            Assert.IsTrue(Math.Abs(_numbersAlgorithms.GetMeanOfTwoNumbers(333, 2) - 167.5) < 3);
        }
        
        [Test]
        public void Test_InterchangeVariablesValues_()
        {
            var firstVariable = 12;
            var secondVariable = 13;
            
            _numbersAlgorithms.InterchangeVariablesValues(ref firstVariable, ref secondVariable);
            Assert.IsTrue(firstVariable == 13 && secondVariable == 12);
            
            _numbersAlgorithms.InterchangeVariablesValues(ref firstVariable, ref secondVariable);
            Assert.IsTrue(firstVariable == 12 && secondVariable == 13);

            var firstDoubleVariable = 123.32;
            var secondDoubleVariable = 345.32;
            
            _numbersAlgorithms.InterchangeVariablesValues(ref firstDoubleVariable, ref secondDoubleVariable);
            Assert.IsTrue(Math.Abs(firstDoubleVariable - 345.32) < 2 && Math.Abs(secondDoubleVariable - 123.32) < 2);
            
            _numbersAlgorithms.InterchangeVariablesValues(ref firstDoubleVariable, ref secondDoubleVariable);
            Assert.IsTrue(Math.Abs(firstDoubleVariable - 123.32) < 2 && Math.Abs(secondDoubleVariable - 345.32) < 2);
        }
        
        [Test]
        public void Test_GetDigitsSumOfNumber_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetDigitsSumOfNumber(121) == 4);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsSumOfNumber(25) == 7);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsSumOfNumber(1369895) == 41);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsSumOfNumber(333) == 9);
        }
        
        [Test]
        public void Test_GetDigitsProductOfNumber_()
        {
            Assert.IsTrue(_numbersAlgorithms.GetDigitsProductOfNumber(121) == 2);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsProductOfNumber(25) == 10);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsProductOfNumber(1369895) == 58320);
            Assert.IsTrue(_numbersAlgorithms.GetDigitsProductOfNumber(333) == 27);
        }
    }
}