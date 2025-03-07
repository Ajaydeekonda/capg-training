namespace LeetcodeTesting
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Solution.AddBinary("11", "1"));
        }
    }

    public class Solution
    {
        public static string AddBinary(string a, string b)
        {
            int num1 = int.Parse(a);
            int num2 = int.Parse(b);
            int carry = 0;
            string bin = "";
            while (num1 > 0 && num2 > 0)
            {
                int sum = 0;
                int x = num1 % 10;
                int y = num2 % 10;
                num1 = num1 / 10;
                num2 = num2 / 10;
                sum = x + y + carry;
                if (sum == 2)
                {
                    carry = 1;
                    bin = '0' + bin;
                }
                else if (sum == 3)
                {
                    carry = 1;
                    bin = '1' + bin;
                }
                else
                {
                    carry = 0;
                    bin = (char)sum + bin;
                }
            }
            return bin;

        }
    }
}
