namespace ESharp.ESharpSourceCode.NumbersAlgorithms
{
    public class NumbersAlgorithmsFactoryObject
    {
        public static IAbstractNumbersAlgorithms GetNumbersAlgorithmsObject()
        {
            return new NumbersAlgorithms();
        }
    }
}