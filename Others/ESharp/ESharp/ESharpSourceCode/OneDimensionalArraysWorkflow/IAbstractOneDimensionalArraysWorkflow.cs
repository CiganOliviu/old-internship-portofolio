using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.OneDimensionalArraysWorkflow
{
    public interface IAbstractOneDimensionalArraysWorkflow
    {
        int GetMinimumValueFromArray(IAbstractOneDimensionalArrayObject array);
        int GetMaximumValueFromArray(IAbstractOneDimensionalArrayObject array);
        int GetArrayElementsSum(IAbstractOneDimensionalArrayObject array);
        int GetArrayElementsProduct(IAbstractOneDimensionalArrayObject array);
        int GetArrayElementsDifference(IAbstractOneDimensionalArrayObject array);
        float GetArrayElementsDivision(IAbstractOneDimensionalArrayObject array);
        float GetArrayElementsMean(IAbstractOneDimensionalArrayObject array);
        bool IsArraySymmetric(IAbstractOneDimensionalArrayObject array);
        IAbstractOneDimensionalArrayObject AddValueInArray(IAbstractOneDimensionalArrayObject array, int value);
        bool IsValueInArray(IAbstractOneDimensionalArrayObject array, int value);
        int[] ConvertNumberToArray(int number);
        int ConvertArrayToNumber(int[] array);
        IAbstractOneDimensionalArrayObject BoostUpArray(IAbstractOneDimensionalArrayObject array, int booster);
        IAbstractOneDimensionalArrayObject BoostDownArray(IAbstractOneDimensionalArrayObject array, int booster);
        IAbstractOneDimensionalArrayObject GetArraysSum(IAbstractOneDimensionalArrayObject arrayOne,
                                                        IAbstractOneDimensionalArrayObject arrayTwo);
        IAbstractOneDimensionalArrayObject GetArraysProduct(IAbstractOneDimensionalArrayObject arrayOne,
                                                            IAbstractOneDimensionalArrayObject arrayTwo);
        IAbstractOneDimensionalArrayObject GetArraysDifference(IAbstractOneDimensionalArrayObject arrayOne, 
                                                                IAbstractOneDimensionalArrayObject arrayTwo);
        IAbstractOneDimensionalArrayObject GetArraysDivision(IAbstractOneDimensionalArrayObject arrayOne,
                                                            IAbstractOneDimensionalArrayObject arrayTwo);
        bool AreArraysEqual(IAbstractOneDimensionalArrayObject arrayOne, IAbstractOneDimensionalArrayObject arrayTwo);
        void SortArray(IAbstractOneDimensionalArrayObject array);
    }
}