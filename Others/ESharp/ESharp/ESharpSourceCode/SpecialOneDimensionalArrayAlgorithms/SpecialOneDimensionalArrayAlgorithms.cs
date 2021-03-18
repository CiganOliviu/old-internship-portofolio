using System;
using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.SpecialOneDimensionalArrayAlgorithms
{
    public class SpecialOneDimensionalArrayAlgorithms : IAbstractSpecialOneDimensionalArrayAlgorithms
    {
        private static void SwapElements(ref int firstParameter, ref int secondParameter)
        {
            firstParameter += secondParameter;
            secondParameter = firstParameter - secondParameter;
            firstParameter -= secondParameter;
        }
        
        public void BubbleSort(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray() - 1; it++)
                for (var jit = 0; jit < array.GetLengthOfOneDimensionalArray() - it - 1; jit++)
                    if (array.GetOneDimensionalArray()[jit] > array.GetOneDimensionalArray()[jit + 1])
                        SwapElements(ref array.GetOneDimensionalArray()[jit],
                            ref array.GetOneDimensionalArray()[jit + 1]);
        }

        public void MinimumValueSort(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray() - 1; it++)
                for (var jit = it + 1; jit < array.GetLengthOfOneDimensionalArray(); jit++)
                    if (array.GetOneDimensionalArray()[it] > array.GetOneDimensionalArray()[jit])
                        SwapElements(ref array.GetOneDimensionalArray()[it], ref array.GetOneDimensionalArray()[jit]);
        }

        private static bool VerifyInsertionCondition(IAbstractOneDimensionalArrayObject array, int jit, int temp)
        {
            return jit >= 0 && array.GetOneDimensionalArray()[jit] > temp;
        }
        
        public void InsertionSort(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
            {
                var temp = array.GetOneDimensionalArray()[it];
                var jit = it - 1;

                while (VerifyInsertionCondition(array, jit, temp))
                {
                    array.GetOneDimensionalArray()[jit + 1] = array.GetOneDimensionalArray()[jit];
                    jit--;
                }

                array.GetOneDimensionalArray()[jit + 1] = temp;
            }
        }

        public void SelectionSort(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                for (var jit = it + 1; jit < array.GetLengthOfOneDimensionalArray(); jit++)
                    if (array.GetOneDimensionalArray()[it] > array.GetOneDimensionalArray()[jit])
                        SwapElements(ref array.GetOneDimensionalArray()[it], ref array.GetOneDimensionalArray()[jit]);
        }

        private static int PerformSwapIfPossible(IAbstractOneDimensionalArrayObject array, int jit, int step)
        {
            if (array.GetOneDimensionalArray()[jit] > array.GetOneDimensionalArray()[jit + step])
            {
                SwapElements(ref array.GetOneDimensionalArray()[jit],
                    ref array.GetOneDimensionalArray()[jit + step]);

                jit -= step;
            }
            else jit--;

            return jit;
        }
        
        public void ShellSort(IAbstractOneDimensionalArrayObject array)
        {
            var step = array.GetLengthOfOneDimensionalArray() / 2;

            while (step > 0)
            {
                for (var it = step; it < array.GetLengthOfOneDimensionalArray(); it++)
                {
                    var jit = it - step;

                    while (jit >= 0)
                        jit = PerformSwapIfPossible(array, jit, step);
                }
                
                step /= 2;
            }
        }

        public bool LinearSearchValue(IAbstractOneDimensionalArrayObject array, int valueToSearch)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                if (array.GetOneDimensionalArray()[it] == valueToSearch)
                    return true;

            return false;
        }

        private static void ProcessCaseWhenValueIsUnderMiddlePoint(IAbstractOneDimensionalArrayObject array, int valueToSearch,
            int middlePoint, ref int rightIndex)
        {
            if (valueToSearch < array.GetOneDimensionalArray()[middlePoint])
                rightIndex = middlePoint - 1;
        }
        
        private static void ProcessCaseWhenValueIsAboveMiddlePoint(IAbstractOneDimensionalArrayObject array, int valueToSearch,
            int middlePoint, ref int leftIndex)
        {
            if (valueToSearch > array.GetOneDimensionalArray()[middlePoint])
                leftIndex = middlePoint + 1;
        }
        
        public bool BinarySearchValue(IAbstractOneDimensionalArrayObject array, int valueToSearch)
        {
            var leftIndex = 0;
            var rightIndex = array.GetLengthOfOneDimensionalArray() - 1;

            while (leftIndex < rightIndex)
            {
                var middlePoint = (leftIndex + rightIndex) / 2;

                if (valueToSearch == array.GetOneDimensionalArray()[middlePoint]) 
                    return true;
                
                ProcessCaseWhenValueIsUnderMiddlePoint(array, valueToSearch, middlePoint, ref rightIndex);
                
                ProcessCaseWhenValueIsAboveMiddlePoint(array, valueToSearch, middlePoint, ref leftIndex);
            }

            return false;
        }
    }
}