using System;

namespace AccessModifiersExample
{
    class Parent
    {
        public string PublicVar = "Public";
        private string PrivateVar = "Private";
        protected string ProtectedVar = "Protected";
        internal string InternalVar = "Internal";
        protected internal string ProtectedInternalVar = "Protected Internal";
        private protected string PrivateProtectedVar = "Private Protected";

        public void Display()
        {
            Console.WriteLine($"{PublicVar}, {PrivateVar}, {ProtectedVar}, {InternalVar}, {ProtectedInternalVar}, {PrivateProtectedVar}");
        }
    }

    class Child : Parent
    {
        public void Show()
        {
            Console.WriteLine($"{PublicVar}, {ProtectedVar}, {InternalVar}, {ProtectedInternalVar}, {PrivateProtectedVar}");
        }
    }

    class Program
    {
        static void Main()
        {
            Parent parent = new Parent();
            Console.WriteLine($"{parent.PublicVar}, {parent.InternalVar}, {parent.ProtectedInternalVar}");

            Child child = new Child();
            child.Show();
        }
    }
}
