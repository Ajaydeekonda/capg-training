namespace CsharpTest
{
    sealed class SecuritySystem
    {
        public int temp = 10;
        public void display()
        {
            Console.WriteLine("Security System");
        }
    }

    //This is will cause a compilation error
    //class child : SecuritySystem { }

    class SecurityMain
    {
        public static void Main(string[] args)
        {
            SecuritySystem sys = new SecuritySystem();
            Console.WriteLine(sys.temp);
            sys.display();
        }
    }

}
