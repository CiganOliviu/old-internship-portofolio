namespace ESharp.DataStructures.Graph
{
    public class Graph : IAbstractGraph
    {
        private int _vertices;
        private int _edges;

        public void SetVertices(int vertices)
        {
            this._vertices = vertices;
        }

        public void SetEdges(int edges)
        {
            this._edges = edges;
        }

        public int GetVertices()
        {
            return _vertices;
        }

        public int GetEdges()
        {
            return _edges;
        }
    }
}