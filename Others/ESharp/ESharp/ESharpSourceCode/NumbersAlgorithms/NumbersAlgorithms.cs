namespace ESharp.ESharpSourceCode.NumbersAlgorithms
{
    public class NumbersAlgorithms : IAbstractNumbersAlgorithms
    {
        public int GetTheLargestCommonDivisor(int inferiorLimit, int superiorLimit)
        {
            if (superiorLimit == 0)
                return inferiorLimit;

            var rest = inferiorLimit % superiorLimit;

            while (rest != 0)
            {
                inferiorLimit = superiorLimit;
                superiorLimit = rest;
                rest = inferiorLimit % superiorLimit;
            }

            return superiorLimit;
        }

        public int GetTheLargestCommonDivisorRecursive(int inferiorLimit, int superiorLimit)
        {
            if (superiorLimit == 0) return inferiorLimit;
            if (inferiorLimit == 0) return superiorLimit;
            if (inferiorLimit == superiorLimit) return superiorLimit;

            if (inferiorLimit > superiorLimit)
                return GetTheLargestCommonDivisorRecursive(inferiorLimit - superiorLimit, superiorLimit);

            return GetTheLargestCommonDivisorRecursive(inferiorLimit, superiorLimit - inferiorLimit);
        }

        public int GetTheLeastCommonMultiple(int inferiorLimit, int superiorLimit)
        {
            return (inferiorLimit * superiorLimit) / GetTheLargestCommonDivisor(inferiorLimit, superiorLimit);
        }

        public int GetValueIfPrime(int factor)
        {
            if (factor == 2)
                return factor;

            for (var divisor = 2; divisor <= factor / 2; divisor++)
                if (factor % divisor == 0)
                    return 0;

            return factor;
        }

        public int ReverseNumber(int number)
        {
            var result = 0;

            while (number != 0)
            {
                result = (result * 10) + number % 10;
                number /= 10;
            }

            return result;
        }

        public int GetPalindromeNumber(int factor)
        {
            return ReverseNumber(factor) == factor ? factor : 0;
        }

        public float GetMeanOfTwoNumbers<T>(T firstNumber, T secondNumber)
        {
            dynamic firstAsNumber = firstNumber;
            dynamic secondAsNumber = secondNumber;

            return (firstAsNumber + secondAsNumber) / 2;
        }

        public void InterchangeVariablesValues<T>(ref T firstVariable, ref T secondVariable)
        {
            dynamic firstAsVariable = firstVariable;
            dynamic secondAsVariable = secondVariable;

            firstAsVariable += secondAsVariable;
            secondAsVariable = firstAsVariable - secondAsVariable;
            firstAsVariable -= secondAsVariable;

            firstVariable = firstAsVariable;
            secondVariable = secondAsVariable;
        }

        public int GetDigitsSumOfNumber(int number)
        {
            var result = 0;
            
            while (number != 0)
            {
                var digit = number % 10;
                result += digit;
                number /= 10;
            }

            return result;
        }

        public int GetDigitsProductOfNumber(int number)
        {
            var result = 1;
            
            while (number != 0)
            {
                var digit = number % 10;
                result *= digit;
                number /= 10;
            }

            return result;
        }
    }
}