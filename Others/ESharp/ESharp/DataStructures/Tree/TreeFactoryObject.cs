namespace ESharp.DataStructures.Tree
{
    public class TreeFactoryObject
    {
        public static IAbstractTree GetTreeObject()
        {
            return new Tree();
        }
    }
}