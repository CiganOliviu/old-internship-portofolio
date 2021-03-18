namespace ESharp.ESharpSourceCode.MatricesWorkflow
{
    public class MatricesWorkflowFactoryObject
    {
        public static IAbstractMatricesWorkflow GetMatricesWorkflowObject()
        {
            return new MatricesWorkflow();
        }
    }
}