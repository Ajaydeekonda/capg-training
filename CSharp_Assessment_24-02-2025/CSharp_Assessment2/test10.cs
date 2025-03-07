using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public sealed class SecuritySystem
{
    public void AuthenticateUser()
    {
        Console.WriteLine("Authenticating user");
    }

}

public class DerivedClass : SecuritySystem
{
    public void AuthenticateUser()
    {
        Console.WriteLine("Authenticating user from derived class");
    }
}

public class test10
{
    public static void Main()
    {
        DerivedClass derivedClass = new DerivedClass();
        derivedClass.AuthenticateUser();
        SecuritySystem SealedClass = new SecuritySystem();
        SealedClass.AuthenticateUser();
    }
}