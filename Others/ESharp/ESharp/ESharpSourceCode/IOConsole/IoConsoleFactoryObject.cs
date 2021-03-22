namespace ESharp.ESharpSourceCode.IOConsole
{
    public class IoConsoleFactoryObject
    {
        public static IAbstractIoConsole GetIoConsoleObject()
        {
            return new IoConsole();
        }
    }
}