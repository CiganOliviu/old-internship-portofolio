namespace ESharp.DataStructures.Tree
{
    public interface IAbstractTree
    {
        int GetValueOfNode();
        IAbstractTree GetLeafLeaf();
        IAbstractTree GetRightLeaf();
    }
}