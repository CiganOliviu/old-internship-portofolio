namespace ESharp.ESharpSourceCode.FundamentalAlgorithms
{
    public static class FundamentalAlgorithmsFactoryObject
    {
        public static IAbstractFundamentalAlgorithms GetFundamentalAlgorithmsObject()
        {
            return new FundamentalAlgorithms();
        }
    }
}