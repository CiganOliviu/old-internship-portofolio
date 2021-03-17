namespace ESharp.ESharpSourceCode.NumbersPropertiesVerifier
{
    public class NumbersPropertiesVerifierFactoryObject
    {
        public static IAbstractNumbersPropertiesVerifier GetNumbersPropertiesVerifier()
        {
            return new NumbersPropertiesVerifier();
        }

    }
}