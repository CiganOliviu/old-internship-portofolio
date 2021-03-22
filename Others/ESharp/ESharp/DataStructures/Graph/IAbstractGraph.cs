namespace ESharp.DataStructures.Graph
{
    public interface IAbstractGraph
    {
        void SetVertices(int vertices);
        void SetEdges(int edges);
        int GetVertices();
        int GetEdges();
    }
}