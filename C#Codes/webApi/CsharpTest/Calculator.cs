namespace CsharpTest
{
    class Calculator
    {
        public int Add(int x,int y)
        {
            return x + y;
        }

        public int Add(int x,int y,int z)
        {
            return x + y + z;
        }

        public double Add(double x,double y)
        {
            return x + y;
        }

        public static void Main(string[] args)
        {
            Calculator calculator = new Calculator();
            Console.WriteLine(calculator.Add(2, 3));
            Console.WriteLine(calculator.Add(3, 4, 5));
            Console.WriteLine(calculator.Add(2.0674, 3.38529));
        }
    }
}
