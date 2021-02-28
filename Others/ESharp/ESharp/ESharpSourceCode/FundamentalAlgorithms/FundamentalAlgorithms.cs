namespace ESharp.ESharpSourceCode.FundamentalAlgorithms
{
    public class FundamentalAlgorithms : IAbstractFundamentalAlgorithms
    {
        private int GetProductOfConsecutiveElements(int factor)
        {
            int result = 1;

            for (int it = 1; it <= factor; it++)
                result *= it;

            return result;
        }

        private void StepUpInFibonacciSequence(ref int firstElement, ref int secondElement)
        {
            var result = firstElement + secondElement;
            firstElement = secondElement;
            secondElement = result;
        }

        private bool IsEulerConditionChecked(int inferiorLimit, int superiorLimit)
        {
            return (superiorLimit == 0 || superiorLimit == inferiorLimit - 1);
        }
        public int GetGaussSum(int factor)
        {
            return (factor * (factor + 1)) / 2;
        }

        public int GetFactorialNumber(int factor)
        {
            if (factor == 0 || factor == 1) return 1;

            int result = this.GetProductOfConsecutiveElements(factor);
            
            return result;
        }

        public int GetFactorialNumberRecursive(int factor)
        {
            if (factor == 0 || factor == 1) return 1;

            return factor * GetFactorialNumberRecursive(factor - 1);
        }

        public int GetFibonacciNumberRecursive(int factor)
        {
            if (factor == 0) return 0;
            if (factor == 1) return 1;

            return GetFibonacciNumberRecursive(factor - 1) + GetFibonacciNumberRecursive(factor - 2);
        }

        public int GetFibonacciNumber(int factor)
        {
            if (factor == 0) return 1;

            int firstElement = 0, secondElement = 1;

            for (int it = 2; it <= factor; it++)
                this.StepUpInFibonacciSequence(ref firstElement, ref secondElement);

            return secondElement;
        }

        public int GetMannaPnueliNumber(int factor)
        {
            if (factor >= 12) return factor - 1;

            return GetMannaPnueliNumber(GetMannaPnueliNumber(factor + 2));
        }

        public int GetAckermanNumber(int inferiorLimit, int superiorLimit)
        {
            if (inferiorLimit == 0) return superiorLimit + 1;
            if (superiorLimit == 0) return GetAckermanNumber(inferiorLimit - 1, 1);

            return GetAckermanNumber(inferiorLimit - 1, GetAckermanNumber(inferiorLimit, superiorLimit - 1));
        }

        public int GetEulerNumber(int inferiorLimit, int superiorLimit)
        {
            if (this.IsEulerConditionChecked(inferiorLimit, superiorLimit)) return 1;
            
            return (
                (inferiorLimit - superiorLimit) *
                GetEulerNumber(inferiorLimit - 1, superiorLimit - 1) + (superiorLimit + 1) *
                GetEulerNumber(inferiorLimit - 1, superiorLimit)
            );
        }

        public int GetCatalanNumber(int factor)
        {
            int result = 0; 
            
            if (factor <= 1) return 1; 
            
            for (int it = 0; it < factor; it++) 
                result += GetCatalanNumber(it) * GetCatalanNumber(factor - it - 1); 
            
            return result; 
        }
    }
}