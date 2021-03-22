namespace ESharp.DataStructures.Graph
{
    public class GraphFactoryObject
    {
        public static IAbstractGraph GetGraphObject()
        {
            return new Graph();
        }
    }
}