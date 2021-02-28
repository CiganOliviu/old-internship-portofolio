using System.Linq;
using ESharp.DataStructures.Matrix;
using ESharp.DataStructures.OneDimensionalArray;
using NUnit.Framework;

namespace TestESharp
{
    public class Tests
    {
        private IAbstractOneDimensionalArrayObject _oneDimensionalArray;
        private IAbstractMatrix _matrix;
        
        [SetUp]
        public void Setup()
        {
            _oneDimensionalArray = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            _matrix = MatrixFactoryObject.GetMatrixObject();
        }

        [Test]
        public void Test_GetLengthOfOneDimensionalArray_()
        {    
            _oneDimensionalArray.SetOneDimensionalArray(new int[] {1, 2, 3, 4, 5});
            Assert.IsTrue(_oneDimensionalArray.GetLengthOfOneDimensionalArray() == 5);
        }
        
        [Test]
        public void Test_GetOneDimensionalArray_()
        {
            _oneDimensionalArray.SetOneDimensionalArray(new int[] {1, 2, 3, 4, 5});
            Assert.IsTrue(_oneDimensionalArray.GetOneDimensionalArray().SequenceEqual(new int[] {1, 2, 3, 4, 5}));
        }

        [Test]
        public void Test_GetLineOfMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            Assert.IsTrue(_matrix.GetLineOfMatrix() == 3);
        }

        [Test]
        public void Test_GetColumnOfMatrix_()
        {
            _matrix.SetColumnOfMatrix(3);
            Assert.IsTrue(_matrix.GetColumnOfMatrix() == 3);
        }

        [Test]
        public void Test_GetMatrix_()
        {
            _matrix.SetMatrix(new int[, ] { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} });
            Assert.IsTrue(_matrix.GetMatrix().Cast<int>().SequenceEqual(new int[, ] { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} }.Cast<int>()));
        }
    }
}