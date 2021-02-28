namespace ESharp.DataStructures.Matrix
{
    public class MatrixObject : IAbstractMatrix
    {
        private int _line;
        private int _column;
        private int[, ] _matrix;
        
        public int GetLineOfMatrix()
        {
            return this._line;
        }

        public void SetLineOfMatrix(int line)
        {
            this._line = line;
        }
        
        public int GetColumnOfMatrix()
        {
            return this._column;
        }

        public void SetColumnOfMatrix(int column)
        {
            this._column = column;
        }

        public int[, ] GetMatrix()
        {
            return this._matrix;
        }

        public void SetMatrix(int[, ] matrix)
        {
            this._matrix = matrix;
        }
    }
}