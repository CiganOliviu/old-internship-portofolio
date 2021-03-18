using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.SpecialOneDimensionalArrayAlgorithms
{
    public interface IAbstractSpecialOneDimensionalArrayAlgorithms
    {
        void BubbleSort(IAbstractOneDimensionalArrayObject array);
        void MinimumValueSort(IAbstractOneDimensionalArrayObject array);
        void InsertionSort(IAbstractOneDimensionalArrayObject array);
        void SelectionSort(IAbstractOneDimensionalArrayObject array);
        void ShellSort(IAbstractOneDimensionalArrayObject array);

        bool LinearSearchValue(IAbstractOneDimensionalArrayObject array, int valueToSearch);
        bool BinarySearchValue(IAbstractOneDimensionalArrayObject array, int valueToSearch);
    }
}