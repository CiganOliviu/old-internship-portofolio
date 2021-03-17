using System;
using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.OneDimensionalArraysWorkflow
{
    public class OneDimensionalArraysWorkflow : IAbstractOneDimensionalArraysWorkflow
    {
        public int GetMinimumValueFromArray(IAbstractOneDimensionalArrayObject array)
        {
            var min = array.GetOneDimensionalArray()[0];
            
            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
                if (min > array.GetOneDimensionalArray()[it])
                    min = array.GetOneDimensionalArray()[it];

            return min;
        }

        public int GetMaximumValueFromArray(IAbstractOneDimensionalArrayObject array)
        {
            var max = array.GetOneDimensionalArray()[0];
            
            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
                if (max < array.GetOneDimensionalArray()[it])
                    max = array.GetOneDimensionalArray()[it];

            return max;
        }

        public int GetArrayElementsSum(IAbstractOneDimensionalArrayObject array)
        {
            var sum = 0;
            
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                sum += array.GetOneDimensionalArray()[it];

            return sum;
        }

        public int GetArrayElementsProduct(IAbstractOneDimensionalArrayObject array)
        {
            var product = 1;

            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                product *= array.GetOneDimensionalArray()[it];

            return product;
        }

        public int GetArrayElementsDifference(IAbstractOneDimensionalArrayObject array)
        {
            var difference = array.GetOneDimensionalArray()[0];

            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
                difference -= array.GetOneDimensionalArray()[it];

            return difference;
        }

        public float GetArrayElementsDivision(IAbstractOneDimensionalArrayObject array)
        {
            var division = array.GetOneDimensionalArray()[0];

            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
                division /= array.GetOneDimensionalArray()[it];

            return division;
        }

        public float GetArrayElementsMean(IAbstractOneDimensionalArrayObject array)
        {
            var mean = array.GetOneDimensionalArray()[0];

            for (var it = 1; it < array.GetLengthOfOneDimensionalArray(); it++)
                mean += array.GetOneDimensionalArray()[it];

            mean /= array.GetLengthOfOneDimensionalArray();

            return mean;
        }

        public bool IsArraySymmetric(IAbstractOneDimensionalArrayObject array)
        {
            var it = 0;
            var jit = array.GetLengthOfOneDimensionalArray() - 1;

            while (it < jit)
            {

                if (array.GetOneDimensionalArray()[it] != array.GetOneDimensionalArray()[jit])
                    return false;
                
                it += 1;
                jit -= 1;
            }

            return true;
        }
        
        private static void SetupNewArray(IAbstractOneDimensionalArrayObject array, int[] newArray)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                newArray[it] = array.GetOneDimensionalArray()[it];
        }

        public IAbstractOneDimensionalArrayObject AddValueInArray(IAbstractOneDimensionalArrayObject array, int value)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();

            var newArray = new int[array.GetLengthOfOneDimensionalArray() + 1];

            SetupNewArray(array, newArray);

            newArray[array.GetLengthOfOneDimensionalArray()] = value;
            
            result.SetOneDimensionalArray(newArray);

            return result;
        }

        public bool IsValueInArray(IAbstractOneDimensionalArrayObject array, int value)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                if (value == array.GetOneDimensionalArray()[it])
                    return true;

            return false;
        }

        private static int ReverseNumber(int number)
        {
            var result = 0;
            
            while (number != 0)
            {
                var digit = number % 10;
                result = result * 10 + digit;
                
                number /= 10;
            }

            return result;
        }

        private static int GetNumberSize(int number)
        {
            var result = 0;
            
            while (number != 0)
            {
                result += 1;
                number /= 10;
            }

            return result;
        }
        public int[] ConvertNumberToArray(int number)
        {
            var numberAsArray = new int[GetNumberSize(number)];
            var it = 0;

            number = ReverseNumber(number);
            
            while (number != 0)
            {
                numberAsArray[it] = number % 10;
                it += 1;
                number /= 10;
            }

            return numberAsArray;
        }

        public int ConvertArrayToNumber(int[] array)
        {
            var result = 0;
            
            foreach (var element in array)
                result = result * 10 + element;

            return result;
        }

        public IAbstractOneDimensionalArrayObject BoostUpArray(IAbstractOneDimensionalArrayObject array, int booster)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();

            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                array.GetOneDimensionalArray()[it] *= booster;
            
            result.SetOneDimensionalArray(array.GetOneDimensionalArray());

            return result;
        }

        public IAbstractOneDimensionalArrayObject BoostDownArray(IAbstractOneDimensionalArrayObject array, int booster)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                array.GetOneDimensionalArray()[it] /= booster;
            
            result.SetOneDimensionalArray(array.GetOneDimensionalArray());

            return result;
        }

        public IAbstractOneDimensionalArrayObject GetArraysSum(IAbstractOneDimensionalArrayObject arrayOne,
            IAbstractOneDimensionalArrayObject arrayTwo)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            result.SetOneDimensionalArray(arrayOne.GetOneDimensionalArray());

            for (var it = 0; it < arrayOne.GetLengthOfOneDimensionalArray(); it++)
                result.GetOneDimensionalArray()[it] =
                    arrayOne.GetOneDimensionalArray()[it] + arrayTwo.GetOneDimensionalArray()[it];

            return result;
        }

        public IAbstractOneDimensionalArrayObject GetArraysProduct(IAbstractOneDimensionalArrayObject arrayOne,
            IAbstractOneDimensionalArrayObject arrayTwo)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            result.SetOneDimensionalArray(arrayOne.GetOneDimensionalArray());

            for (var it = 0; it < arrayOne.GetLengthOfOneDimensionalArray(); it++)
                result.GetOneDimensionalArray()[it] =
                    arrayOne.GetOneDimensionalArray()[it] * arrayTwo.GetOneDimensionalArray()[it];

            return result;
        }

        public IAbstractOneDimensionalArrayObject GetArraysDifference(IAbstractOneDimensionalArrayObject arrayOne,
            IAbstractOneDimensionalArrayObject arrayTwo)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            result.SetOneDimensionalArray(arrayOne.GetOneDimensionalArray());

            for (var it = 0; it < arrayOne.GetLengthOfOneDimensionalArray(); it++)
                result.GetOneDimensionalArray()[it] =
                    arrayOne.GetOneDimensionalArray()[it] - arrayTwo.GetOneDimensionalArray()[it];

            return result;
        }

        public IAbstractOneDimensionalArrayObject GetArraysDivision(IAbstractOneDimensionalArrayObject arrayOne,
            IAbstractOneDimensionalArrayObject arrayTwo)
        {
            var result = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            result.SetOneDimensionalArray(arrayOne.GetOneDimensionalArray());

            for (var it = 0; it < arrayOne.GetLengthOfOneDimensionalArray(); it++)
                result.GetOneDimensionalArray()[it] =
                    arrayOne.GetOneDimensionalArray()[it] / arrayTwo.GetOneDimensionalArray()[it];

            return result;
        }

        private static bool AssertNumbers(int firstNumber, int secondNumber)
        {
            return firstNumber == secondNumber;
        }
        
        public bool AreArraysEqual(IAbstractOneDimensionalArrayObject arrayOne, IAbstractOneDimensionalArrayObject arrayTwo)
        {
            if (!AssertNumbers(arrayOne.GetLengthOfOneDimensionalArray(), arrayTwo.GetLengthOfOneDimensionalArray()))
                return false;
            
            for (var it = 0; it < arrayOne.GetLengthOfOneDimensionalArray(); it++)
                if (arrayOne.GetOneDimensionalArray()[it] != arrayTwo.GetOneDimensionalArray()[it])
                    return false;
            
            return true;
        }

        private static void SwapElements(ref int firstParameter, ref int secondParameter)
        {
            firstParameter += secondParameter;
            secondParameter = firstParameter - secondParameter;
            firstParameter -= secondParameter;
        }
        
        public void SortArray(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray() - 1; it++)
                for (var jit = it + 1; jit < array.GetLengthOfOneDimensionalArray(); jit++)
                    if (array.GetOneDimensionalArray()[it] > array.GetOneDimensionalArray()[jit])
                        SwapElements(ref array.GetOneDimensionalArray()[it], ref array.GetOneDimensionalArray()[jit]);
        }
    }
}