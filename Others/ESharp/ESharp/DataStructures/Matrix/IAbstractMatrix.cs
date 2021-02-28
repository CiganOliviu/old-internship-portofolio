namespace ESharp.DataStructures.Matrix
{
    public interface IAbstractMatrix
    {
        int GetLineOfMatrix();
        void SetLineOfMatrix(int line);

        int GetColumnOfMatrix();
        void SetColumnOfMatrix(int column);

        int[, ] GetMatrix();
        void SetMatrix(int[, ] matrix);
    }
}