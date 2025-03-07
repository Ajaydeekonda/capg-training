

namespace CsharpTest
{
    sealed class SecuritySystem
    {
        public void AuthenticateUser() => Console.WriteLine("User authenticated.");
    }

    class SecurityMain
    {
        static void Main()
        {
            SecuritySystem security = new SecuritySystem();
            security.AuthenticateUser();
        }
    }
}
