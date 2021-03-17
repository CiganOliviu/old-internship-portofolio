namespace ESharp.ESharpSourceCode.MatricesWorkflow
{
    public class MatricesWorkflowAbstractFactory
    {
        public static IAbstractMatricesWorkflow GetMatricesWorkflowObject()
        {
            return new MatricesWorkflow();
        }
    }
}