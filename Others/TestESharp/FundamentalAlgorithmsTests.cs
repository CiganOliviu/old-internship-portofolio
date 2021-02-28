using ESharp.ESharpSourceCode.FundamentalAlgorithms;
using NUnit.Framework;

namespace TestESharp
{
    public class FundamentalAlgorithmsTests
    {
        private IAbstractFundamentalAlgorithms _fundamentalAlgorithms;
        
        [SetUp]
        public void Setup()
        {
            _fundamentalAlgorithms = FundamentalAlgorithmsFactoryObject.GetFundamentalAlgorithmsObject();
        }

        [Test]
        public void Test_GetGaussSum_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetGaussSum(6) == 21);
            Assert.IsTrue(_fundamentalAlgorithms.GetGaussSum(5) == 15);
            Assert.IsTrue(_fundamentalAlgorithms.GetGaussSum(1) == 1);
        }
        
        [Test]
        public void Test_GetFactorialNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumber(5) == 120);
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumber(7) == 5040);
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumber(0) == 1);
        }
        
        [Test]
        public void Test_GetFactorialNumberRecursive_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumberRecursive(5) == 120);
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumberRecursive(7) == 5040);
            Assert.IsTrue(_fundamentalAlgorithms.GetFactorialNumberRecursive(0) == 1);
        }
        
        [Test]
        public void Test_GetFibonacciNumberRecursive_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumberRecursive(10) == 55);
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumberRecursive(14) == 377);
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumberRecursive(1) == 1);
        }
        
        [Test]
        public void Test_GetFibonacciNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumber(10) == 55);
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumber(14) == 377);
            Assert.IsTrue(_fundamentalAlgorithms.GetFibonacciNumber(1) == 1);
        }
        
        [Test]
        public void Test_GetMannaPnueliNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetMannaPnueliNumber(8) == 11);
            Assert.IsTrue(_fundamentalAlgorithms.GetMannaPnueliNumber(15) == 14);
        }
        
        [Test]
        public void Test_GetAckermanNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetAckermanNumber(1, 2) == 4);
        }
        
        [Test]
        public void Test_GetEulerNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetEulerNumber(3, 1) == 4);
        }
        
        [Test]
        public void Test_GetCatalanNumber_()
        {
            Assert.IsTrue(_fundamentalAlgorithms.GetCatalanNumber(3) == 5);
        }
        
    }
}