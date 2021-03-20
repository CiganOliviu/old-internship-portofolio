using ESharp.DataStructures.Matrix;
using ESharp.ESharpSourceCode.MatricesWorkflow;
using NUnit.Framework;

namespace TestESharp
{
    public class MatricesWorkflowTests
    {
        private IAbstractMatricesWorkflow _matricesWorkflow;
        private IAbstractMatrix _matrix;
        [SetUp]
        public void Setup()
        {
            _matricesWorkflow = MatricesWorkflowFactoryObject.GetMatricesWorkflowObject();
            _matrix = MatrixFactoryObject.GetMatrixObject();
        }

        [Test]
        public void Test_GetMaximumValueFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            Assert.IsTrue(_matricesWorkflow.GetMaximumValueFromMatrix(_matrix) == 9);
        }
        
        [Test]
        public void Test_GetMinimumValueFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            Assert.IsTrue(_matricesWorkflow.GetMinimumValueFromMatrix(_matrix) == 1);
        }
        
        [Test]
        public void Test_GetMatrixElementsSum_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            Assert.IsTrue(_matricesWorkflow.GetMatrixElementsSum(_matrix) == 45);
        }
        
        [Test]
        public void Test_GetMatrixElementsProduct_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {0, 8, 9}});
            
            Assert.IsTrue(_matricesWorkflow.GetMatrixElementsProduct(_matrix) == 0);
        }
        
        [Test]
        public void Test_GetMatrixElementsDifference_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{-1, -2, -3}, {-4, -5, -6}, {-7, -8, -9}});
            
            Assert.IsTrue(_matricesWorkflow.GetMatrixElementsDifference(_matrix) == 45);
        }
        
        [Test]
        public void Test_GetMatrixElementsDivision_()
        {
            _matrix.SetLineOfMatrix(2);
            _matrix.SetColumnOfMatrix(2);
            _matrix.SetMatrix(new [,]{{4, 3}, {2, 1}});
            
            Assert.IsTrue(_matricesWorkflow.GetMatrixElementsDivision(_matrix) == 0);
        }
        
        [Test]
        public void Test_BoostUpMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {0, 8, 9}});

            var expected = new [,] {{2, 4, 6}, {8, 10, 12}, {0, 16, 18}};
            
            Assert.AreEqual(_matricesWorkflow.BoostUpMatrix(_matrix, 2).GetMatrix(), expected);
        }
        
        [Test]
        public void Test_BoostDownMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {27, 8, 9}});

            var expected = new [,] {{0, 0, 1}, {1, 1, 2}, {9, 2, 3}};
            
            Assert.AreEqual(_matricesWorkflow.BoostDownMatrix(_matrix, 3).GetMatrix(), expected);
        }
        
        [Test]
        public void Test_GetMatricesSum_()
        {
            var firstMatrix = MatrixFactoryObject.GetMatrixObject();
            firstMatrix.SetLineOfMatrix(3);
            firstMatrix.SetColumnOfMatrix(3);
            firstMatrix.SetMatrix(new [, ]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            var secondMatrix = MatrixFactoryObject.GetMatrixObject();
            secondMatrix.SetLineOfMatrix(3);
            secondMatrix.SetColumnOfMatrix(3);
            secondMatrix.SetMatrix(new [, ]{{7, 8, 9}, {4, 5, 6}, {1, 2, 3}});

            var expected = new[,] {{8, 10, 12}, {8, 10, 12}, {8, 10, 12}};

            Assert.AreEqual(_matricesWorkflow.GetMatricesSum(firstMatrix,secondMatrix).GetMatrix(),
                expected);
        }
        
        [Test]
        public void Test_GetMatricesDifference_()
        {
            var firstMatrix = MatrixFactoryObject.GetMatrixObject();
            firstMatrix.SetLineOfMatrix(3);
            firstMatrix.SetColumnOfMatrix(3);
            firstMatrix.SetMatrix(new [, ]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            var secondMatrix = MatrixFactoryObject.GetMatrixObject();
            secondMatrix.SetLineOfMatrix(3);
            secondMatrix.SetColumnOfMatrix(3);
            secondMatrix.SetMatrix(new [, ]{{7, 8, 9}, {4, 5, 6}, {1, 2, 3}});

            var expected = new[,] {{-6, -6, -6}, {0, 0, 0}, {6, 6, 6}};

            Assert.AreEqual(_matricesWorkflow.GetMatricesDifference(firstMatrix,secondMatrix).GetMatrix(),
                expected);
        }
        
        [Test]
        public void Test_GetMatricesProduct_()
        {
            var firstMatrix = MatrixFactoryObject.GetMatrixObject();
            firstMatrix.SetLineOfMatrix(3);
            firstMatrix.SetColumnOfMatrix(3);
            firstMatrix.SetMatrix(new [, ]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});
            
            var secondMatrix = MatrixFactoryObject.GetMatrixObject();
            secondMatrix.SetLineOfMatrix(3);
            secondMatrix.SetColumnOfMatrix(3);
            secondMatrix.SetMatrix(new [, ]{{7, 8, 9}, {4, 5, 6}, {1, 2, 3}});

            var expected = new[,] {{7, 16, 27}, {16, 25, 36}, {7, 16, 27}};

            Assert.AreEqual(_matricesWorkflow.GetMatricesProduct(firstMatrix,secondMatrix).GetMatrix(),
                expected);
        }
        
        [Test]
        public void Test_GetMainDiagonalElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {1, 5, 9};
            
            Assert.AreEqual(_matricesWorkflow.GetMainDiagonalElementsFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetElementsAboveMainDiagonalFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {4, 7, 8};
            
            Assert.AreEqual(_matricesWorkflow.GetElementsAboveMainDiagonalFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetElementsUnderMainDiagonalFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {2, 3, 6};
            
            Assert.AreEqual(_matricesWorkflow.GetElementsUnderMainDiagonalFromMatrix(_matrix), expected);
        }

        [Test]
        public void Test_GetSecondaryDiagonalElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {3, 5, 7};
            
            Assert.AreEqual(_matricesWorkflow.GetSecondaryDiagonalElementsFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetElementsAboveSecondaryDiagonalFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {6, 8, 9};
            
            Assert.AreEqual(_matricesWorkflow.GetElementsAboveSecondaryDiagonalFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetElementsUnderSecondaryDiagonalFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {1, 2, 4};
            
            Assert.AreEqual(_matricesWorkflow.GetElementsUnderSecondaryDiagonalFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetNorthElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {2};
            
            Assert.AreEqual(_matricesWorkflow.GetNorthElementsFromMatrix(_matrix), expected);
        }
        
        [Test]
        public void Test_GetSouthElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {8};
            
            Assert.AreEqual(_matricesWorkflow.GetSouthElementsFromMatrix(_matrix), expected);

        }

        [Test]
        public void Test_GetEastElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {6};
            
            Assert.AreEqual(_matricesWorkflow.GetEastElementsFromMatrix(_matrix), expected);

        }
        
        [Test]
        public void Test_GetWestElementsFromMatrix_()
        {
            _matrix.SetLineOfMatrix(3);
            _matrix.SetColumnOfMatrix(3);
            _matrix.SetMatrix(new [,]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}});

            var expected = new [] {4};
            
            Assert.AreEqual(_matricesWorkflow.GetWestElementsFromMatrix(_matrix), expected);

        }
    }
}