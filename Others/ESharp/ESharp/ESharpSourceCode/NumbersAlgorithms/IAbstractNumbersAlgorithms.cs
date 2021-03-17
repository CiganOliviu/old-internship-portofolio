namespace ESharp.ESharpSourceCode.NumbersAlgorithms
{
    public interface IAbstractNumbersAlgorithms
    {
        int GetTheLargestCommonDivisor(int inferiorLimit, int superiorLimit);
        int GetTheLargestCommonDivisorRecursive(int inferiorLimit, int superiorLimit);
        int GetTheLeastCommonMultiple(int inferiorLimit, int superiorLimit);
        int GetValueIfPrime(int factor);
        int ReverseNumber(int number);
        int GetPalindromeNumber(int factor);
        float GetMeanOfTwoNumbers<T>(T firstNumber, T secondNumber);
        void InterchangeVariablesValues<T>(ref T firstVariable, ref T secondVariable);
        int GetDigitsSumOfNumber(int number);
        int GetDigitsProductOfNumber(int number);
    }
}