namespace CsharpTest
{
    class Complex
    {
        public int Real { get; set; }
        public int Imag { get; set; }

        public Complex(int real, int imag)
        {
            Real = real;
            Imag = imag;
        }

        public override string ToString()
        {
            return $"{Real}+i{Imag}";
        }
        public static Complex operator +(Complex a, Complex b)
        {
            return new Complex(a.Real+b.Real,a.Imag+b.Imag);
        }

        public static void Main(string[] args)
        {
            Complex comp = new Complex(1, 2);
            Complex comp2 = new Complex(2, 3);
            Complex res = comp + comp2;
            Console.WriteLine(comp);
            Console.WriteLine(comp2);
            Console.WriteLine(res);
        }
    }


}
