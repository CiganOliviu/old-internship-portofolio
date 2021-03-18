namespace ESharp.ESharpSourceCode.SpecialOneDimensionalArrayAlgorithms
{
    public class SpecialOneDimensionalArrayAlgorithmsFactoryObject
    {
        public static IAbstractSpecialOneDimensionalArrayAlgorithms GetSpecialOneDimensionalArrayAlgorithms()
        {
            return new SpecialOneDimensionalArrayAlgorithms();
        }
    }
}