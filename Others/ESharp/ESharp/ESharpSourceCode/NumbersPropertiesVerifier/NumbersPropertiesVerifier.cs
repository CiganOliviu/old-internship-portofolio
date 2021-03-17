using System;

namespace ESharp.ESharpSourceCode.NumbersPropertiesVerifier
{
    public class NumbersPropertiesVerifier: IAbstractNumbersPropertiesVerifier
    {
        public bool IsPrime(int number)
        {
            if (number == 2) return true;

            for (var divisor = 2; divisor <= number / 2; divisor++)
                if (number % divisor == 0)
                    return false;

            return true;
        }

        public bool IsOdd(int number)
        {
            return number % 2 == 1;
        }

        public bool IsEven(int number)
        {
            return number % 2 == 0;
        }

        private int ReverseNumber(int number)
        {
            var result = 0;

            while (number != 0)
            {
                var digit = number % 10;
                result = ( result * 10 ) + digit; 
                number /= 10;
            }

            return result;
        }
        
        public bool IsPalindrome(int number)
        {
            return ReverseNumber(number) == number;
        }

        public bool IsPerfectSquare(int number)
        {
            return Math.Sqrt(number) % 1 == 0;
        }

        private int GetFibonacciNumber(int number)
        {
            if (number == 1 || number == 2)
                return 1;

            return GetFibonacciNumber(number - 1) + GetFibonacciNumber(number - 2);
        }
        public bool IsFibonacci(int number)
        {
            for (var it = 1; it < number; it++)
                if (GetFibonacciNumber(it) == number)
                    return true;

            return false;
        }

        private int GetFactorialNumber(int number)
        {
            if (number == 0 || number == 1)
                return 1;

            return number * GetFactorialNumber(number - 1);
        }
        
        public bool IsFactorial(int number)
        {
            for (var it = 1; it < number; it++)
                if (GetFactorialNumber(it) == number)
                    return true;

            return false;
        }
    }
}