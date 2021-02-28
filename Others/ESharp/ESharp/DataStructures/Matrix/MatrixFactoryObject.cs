namespace ESharp.DataStructures.Matrix
{
    public static class MatrixFactoryObject
    {
        public static IAbstractMatrix GetMatrixObject()
        {
            return new MatrixObject();
        }
    }
}