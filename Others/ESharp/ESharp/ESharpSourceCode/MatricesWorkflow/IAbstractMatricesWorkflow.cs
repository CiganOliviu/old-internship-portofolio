using ESharp.DataStructures.Matrix;

namespace ESharp.ESharpSourceCode.MatricesWorkflow
{
    public interface IAbstractMatricesWorkflow
    {
        int GetMaximumValueFromMatrix(IAbstractMatrix matrix);
        int GetMinimumValueFromMatrix(IAbstractMatrix matrix);
        int GetMatrixElementsSum(IAbstractMatrix matrix);
        int GetMatrixElementsProduct(IAbstractMatrix matrix);
        int GetMatrixElementsDifference(IAbstractMatrix matrix);
        int GetMatrixElementsDivision(IAbstractMatrix matrix);
        IAbstractMatrix BoostUpMatrix(IAbstractMatrix matrix);
        IAbstractMatrix BoostDownMatrix(IAbstractMatrix matrix);
        IAbstractMatrix GetMatricesSum(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo);
        IAbstractMatrix GetMatricesDifference(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo);
        IAbstractMatrix GetMatricesProduct(IAbstractMatrix matrixOne, IAbstractMatrix matrixTwo);
        int[] GetMainDiagonalElementsFromMatrix(IAbstractMatrix matrix);
        int[] GetElementsAboveMainDiagonalFromMatrix(IAbstractMatrix matrix);
        int[] GetElementsUnderMainDiagonalFromMatrix(IAbstractMatrix matrix);
        int[] GetSecondaryDiagonalElementsFromMatrix(IAbstractMatrix matrix);
        int[] GetElementsAboveSecondaryDiagonalFromMatrix(IAbstractMatrix matrix);
        int[] GetElementsUnderSecondaryDiagonalFromMatrix(IAbstractMatrix matrix);
        int[] GetNorthElementsFromMatrix(IAbstractMatrix matrix);
        int[] GetSouthElementsFromMatrix(IAbstractMatrix matrix);
        int[] GetEastElementsFromMatrix(IAbstractMatrix matrix);
        int[] GetWestElementsFromMatrix(IAbstractMatrix matrix);
    }
}