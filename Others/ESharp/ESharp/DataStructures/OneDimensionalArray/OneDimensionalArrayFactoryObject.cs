namespace ESharp.DataStructures.OneDimensionalArray
{
    public static class OneDimensionalArrayFactoryObject
    {
        public static IAbstractOneDimensionalArrayObject GetOneDimensionalArrayObject()
        {
            return new OneDimensionalArrayObject();
        }
    }
}