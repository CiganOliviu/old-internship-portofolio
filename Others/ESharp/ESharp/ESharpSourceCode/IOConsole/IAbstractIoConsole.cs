using ESharp.DataStructures.Matrix;
using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.IOConsole
{
    public interface IAbstractIoConsole
    {
        IAbstractOneDimensionalArrayObject ReadOneDimensionalArray(int size);
        void OutputOneDimensionalArray(IAbstractOneDimensionalArrayObject array);

        IAbstractMatrix ReadMatrix(int lines, int columns);
        void OutputMatrix(IAbstractMatrix matrix);
    }
}