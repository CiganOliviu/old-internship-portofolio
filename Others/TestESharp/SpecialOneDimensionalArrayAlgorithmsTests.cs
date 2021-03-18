using ESharp.DataStructures.OneDimensionalArray;
using ESharp.ESharpSourceCode.SpecialOneDimensionalArrayAlgorithms;
using NUnit.Framework;

namespace TestESharp
{
    public class SpecialOneDimensionalArrayAlgorithmsTests
    {
        private IAbstractSpecialOneDimensionalArrayAlgorithms _specialOneDimensionalArrayAlgorithms;
        private IAbstractOneDimensionalArrayObject _array;

        [SetUp]
        public void Setup()
        {
            _specialOneDimensionalArrayAlgorithms = SpecialOneDimensionalArrayAlgorithmsFactoryObject
                .GetSpecialOneDimensionalArrayAlgorithms();

            _array = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
        }

        [Test]
        public void Test_BubbleSort_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            _specialOneDimensionalArrayAlgorithms.BubbleSort(_array);
            
            var expected = new int[] {-5, -3, 1, 2, 4, 6, 7};
            
            Assert.AreEqual(_array.GetOneDimensionalArray(), expected);
        }
        
        [Test]
        public void Test_MinimumValueSort_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            _specialOneDimensionalArrayAlgorithms.MinimumValueSort(_array);
            
            var expected = new int[] {-5, -3, 1, 2, 4, 6, 7};
            
            Assert.AreEqual(_array.GetOneDimensionalArray(), expected);
        }
        
        [Test]
        public void Test_InsertionSort_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            _specialOneDimensionalArrayAlgorithms.InsertionSort(_array);
            
            var expected = new int[] {-5, -3, 1, 2, 4, 6, 7};
            
            Assert.AreEqual(_array.GetOneDimensionalArray(), expected);
        }
        
        [Test]
        public void Test_SelectionSort_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            _specialOneDimensionalArrayAlgorithms.SelectionSort(_array);
            
            var expected = new int[] {-5, -3, 1, 2, 4, 6, 7};
            
            Assert.AreEqual(_array.GetOneDimensionalArray(), expected);
        }
        
        [Test]
        public void Test_ShellSort_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            _specialOneDimensionalArrayAlgorithms.ShellSort(_array);
            
            var expected = new int[] {-5, -3, 1, 2, 4, 6, 7};
            
            Assert.AreEqual(_array.GetOneDimensionalArray(), expected);
        }
        
        [Test]
        public void Test_LinearSearchValue_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            
            Assert.IsTrue(_specialOneDimensionalArrayAlgorithms.LinearSearchValue(_array, 2));
            
        }
        
        [Test]
        public void Test_BinarySearchValue_()
        {
            _array.SetOneDimensionalArray(new [] {7, 6, -5, 4, -3, 2, 1});
            
            _specialOneDimensionalArrayAlgorithms.BubbleSort(_array);
            
            Assert.IsTrue(_specialOneDimensionalArrayAlgorithms.BinarySearchValue(_array, 2));
        }
    }
}