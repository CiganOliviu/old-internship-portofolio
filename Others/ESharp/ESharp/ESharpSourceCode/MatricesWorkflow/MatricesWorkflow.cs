using ESharp.DataStructures.Matrix;

namespace ESharp.ESharpSourceCode.MatricesWorkflow
{
    public class MatricesWorkflow : IAbstractMatricesWorkflow
    {
        public int GetMaximumValueFromMatrix(IAbstractMatrix matrix)
        {
            var result = matrix.GetMatrix()[0, 0];
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 1; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (result < matrix.GetMatrix()[it, jit])
                        result = matrix.GetMatrix()[it, jit];

            return result;
        }

        public int GetMinimumValueFromMatrix(IAbstractMatrix matrix)
        {
            var result = matrix.GetMatrix()[0, 0];
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 1; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (result > matrix.GetMatrix()[it, jit])
                        result = matrix.GetMatrix()[it, jit];

            return result;
        }

        public int GetMatrixElementsSum(IAbstractMatrix matrix)
        {
            var result = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    result += matrix.GetMatrix()[it, jit];

            return result;
        }

        public int GetMatrixElementsProduct(IAbstractMatrix matrix)
        {
            var result = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    result *= matrix.GetMatrix()[it, jit];

            return result;
        }

        public int GetMatrixElementsDifference(IAbstractMatrix matrix)
        {
            var result = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    result -= matrix.GetMatrix()[it, jit];

            return result;
        }

        public int GetMatrixElementsDivision(IAbstractMatrix matrix)
        {
            var result = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++) 
                    result /= matrix.GetMatrix()[it, jit];

            return result;
        }

        public IAbstractMatrix BoostUpMatrix(IAbstractMatrix matrix, int booster)
        {
            var result = MatrixFactoryObject.GetMatrixObject();
            result.SetLineOfMatrix(matrix.GetLineOfMatrix());
            result.SetColumnOfMatrix(matrix.GetColumnOfMatrix());
            result.SetMatrix(matrix.GetMatrix());
            
            for (var it = 0; it < result.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < result.GetColumnOfMatrix(); jit++)
                    result.GetMatrix()[it, jit] *= booster;

            return result;
        }

        public IAbstractMatrix BoostDownMatrix(IAbstractMatrix matrix, int booster)
        {
            var result = MatrixFactoryObject.GetMatrixObject();
            result.SetLineOfMatrix(matrix.GetLineOfMatrix());
            result.SetColumnOfMatrix(matrix.GetColumnOfMatrix());
            result.SetMatrix(matrix.GetMatrix());
            
            for (var it = 0; it < result.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < result.GetColumnOfMatrix(); jit++)
                    result.GetMatrix()[it, jit] /= booster;

            return result;
        }

        public IAbstractMatrix GetMatricesSum(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo)
        {
            var result = MatrixFactoryObject.GetMatrixObject();
            result.SetLineOfMatrix(matrixOne.GetLineOfMatrix());
            result.SetColumnOfMatrix(matrixOne.GetColumnOfMatrix());
            result.SetMatrix(matrixOne.GetMatrix());
            
            for (var it = 0; it < matrixOne.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrixOne.GetColumnOfMatrix(); jit++)
                    result.GetMatrix()[it, jit] += matrixTwo.GetMatrix()[it, jit];

            return result;
        }

        public IAbstractMatrix GetMatricesDifference(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo)
        {
            var result = MatrixFactoryObject.GetMatrixObject();
            result.SetLineOfMatrix(matrixOne.GetLineOfMatrix());
            result.SetColumnOfMatrix(matrixOne.GetColumnOfMatrix());
            result.SetMatrix(matrixOne.GetMatrix());
            
            for (var it = 0; it < matrixOne.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrixOne.GetColumnOfMatrix(); jit++)
                    result.GetMatrix()[it, jit] -= matrixTwo.GetMatrix()[it, jit];

            return result;
        }

        public IAbstractMatrix GetMatricesProduct(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo)
        {
            var result = MatrixFactoryObject.GetMatrixObject();
            result.SetLineOfMatrix(matrixOne.GetLineOfMatrix());
            result.SetColumnOfMatrix(matrixOne.GetColumnOfMatrix());
            result.SetMatrix(matrixOne.GetMatrix());
            
            for (var it = 0; it < matrixOne.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrixOne.GetColumnOfMatrix(); jit++)
                    result.GetMatrix()[it, jit] *= matrixTwo.GetMatrix()[it, jit];

            return result;
        }

        private static int AddValueInArray(IAbstractMatrix matrix, int[] result, int index, int it, int jit)
        {
            result[index] = matrix.GetMatrix()[it, jit];
            index += 1;
            
            return index;
        }
        
        private static bool IsElementOnMainDiagonal(int it, int jit)
        {
            return it == jit;
        }
        
        public int[] GetMainDiagonalElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementOnMainDiagonal(it, jit))
                        index = AddValueInArray(matrix, result, index, it, jit);
                    

            return result;
        }
        
        private static bool IsElementAboveTheMainDiagonal(int it, int jit)
        {
            return it > jit;
        }
        
        public int[] GetElementsAboveMainDiagonalFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementAboveTheMainDiagonal(it, jit))
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }
        
        private static bool IsElementUnderTheMainDiagonal(int it, int jit)
        {
            return it < jit;
        }
        
        public int[] GetElementsUnderMainDiagonalFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementUnderTheMainDiagonal(it, jit))
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementOnTheSecondaryDiagonal(IAbstractMatrix matrix, int it, int jit)
        {
            return it + jit == matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetSecondaryDiagonalElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementOnTheSecondaryDiagonal(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementAboveTheSecondaryDiagonal(IAbstractMatrix matrix, int it, int jit)
        {
            return it + jit > matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetElementsAboveSecondaryDiagonalFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementAboveTheSecondaryDiagonal(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementUnderTheSecondaryDiagonal(IAbstractMatrix matrix, int it, int jit)
        {
            return it + jit < matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetElementsUnderSecondaryDiagonalFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix()];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementUnderTheSecondaryDiagonal(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementInTheNorth(IAbstractMatrix matrix, int it, int jit)
        {
            return it < jit && it + jit < matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetNorthElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix() - 2];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementInTheNorth(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementInTheSouth(IAbstractMatrix matrix, int it, int jit)
        {
            return it > jit && it + jit > matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetSouthElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix() - 2];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementInTheSouth(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }
        
        private static bool IsElementInTheEast(IAbstractMatrix matrix, int it, int jit)
        {
            return it < jit && it + jit > matrix.GetLineOfMatrix() - 1;
        }

        public int[] GetEastElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix() - 2];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementInTheEast(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }

        private static bool IsElementInTheWest(IAbstractMatrix matrix, int it, int jit)
        {
            return it > jit && it + jit < matrix.GetLineOfMatrix() - 1;
        }
        
        public int[] GetWestElementsFromMatrix(IAbstractMatrix matrix)
        {
            var result = new int[matrix.GetLineOfMatrix() - 2];
            var index = 0;
            
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    if (IsElementInTheWest(matrix, it, jit)) 
                        index = AddValueInArray(matrix, result, index, it, jit);

            return result;
        }
    }
}