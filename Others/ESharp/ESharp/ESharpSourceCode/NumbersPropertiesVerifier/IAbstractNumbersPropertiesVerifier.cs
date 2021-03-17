namespace ESharp.ESharpSourceCode.NumbersPropertiesVerifier
{
    public interface IAbstractNumbersPropertiesVerifier
    {
        bool IsPrime(int number);
        bool IsOdd(int number);
        bool IsEven(int number);
        bool IsPalindrome(int number);
        bool IsPerfectSquare(int number);
        bool IsFibonacci(int number);
        bool IsFactorial(int number);
    }
}