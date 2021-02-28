namespace ESharp.DataStructures.OneDimensionalArray
{
    public class OneDimensionalArrayObject : IAbstractOneDimensionalArrayObject
    {
        private int _length;
        private int[] _array = { };

        private void AssignLength()
        {
            this._length = _array.Length;
        }
        public int GetLengthOfOneDimensionalArray()
        {
            return this._length;
        }

        public int[] GetOneDimensionalArray()
        {
            return this._array;
        }

        public void SetOneDimensionalArray(int[] array)
        {
            this._array = array;
            
            AssignLength();
        }
    }
}