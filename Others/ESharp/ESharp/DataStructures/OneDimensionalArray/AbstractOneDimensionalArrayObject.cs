namespace ESharp.DataStructures.OneDimensionalArray
{
    public interface IAbstractOneDimensionalArrayObject
    {
        void SetLengthOfOneDimensionalArray(int length);
        int GetLengthOfOneDimensionalArray();
        int[] GetOneDimensionalArray();
        void SetOneDimensionalArray(int[] array);
    }
}