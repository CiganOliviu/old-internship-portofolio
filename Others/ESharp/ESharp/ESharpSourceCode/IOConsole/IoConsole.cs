using System;
using ESharp.DataStructures.Matrix;
using ESharp.DataStructures.OneDimensionalArray;

namespace ESharp.ESharpSourceCode.IOConsole
{
    public class IoConsole : IAbstractIoConsole
    {
        public IAbstractOneDimensionalArrayObject ReadOneDimensionalArray(int size)
        {
            var array = OneDimensionalArrayFactoryObject.GetOneDimensionalArrayObject();
            array.SetLengthOfOneDimensionalArray(size);

            for (var it = 0; it < size; it++)
                array.GetOneDimensionalArray()[it] = Convert.ToInt32(Console.ReadLine());

            return array;
        }

        public void OutputOneDimensionalArray(IAbstractOneDimensionalArrayObject array)
        {
            for (var it = 0; it < array.GetLengthOfOneDimensionalArray(); it++)
                Console.Write(array.GetOneDimensionalArray()[it] + " ");
        }

        public IAbstractMatrix ReadMatrix(int lines, int columns)
        {
            var matrix = MatrixFactoryObject.GetMatrixObject();
            matrix.SetLineOfMatrix(lines);
            matrix.SetColumnOfMatrix(columns);

            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    matrix.GetMatrix()[it, jit] = Convert.ToInt32(Console.ReadLine());

            return matrix;
        }

        public void OutputMatrix(IAbstractMatrix matrix)
        {
            for (var it = 0; it < matrix.GetLineOfMatrix(); it++)
                for (var jit = 0; jit < matrix.GetColumnOfMatrix(); jit++)
                    Console.Write(matrix.GetMatrix()[it, jit] + " ");
        }
    }
}