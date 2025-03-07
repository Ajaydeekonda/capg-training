//using System;
//namespace CSharpPractice
//{
//    class Student
//    {
//        int[] scores = new int[5];

//        public void input()
//        {
//            Console.WriteLine("Enter 5 Integers:");
//            for (int i = 0; i < scores.Length; i++)
//            {
//                this.scores[i] = int.Parse(Console.ReadLine());
//            }
//        }

//        public int calculateTotalScore()
//        {
//            int sum = 0;
//            for (int i = 0; i < scores.Length; i++)
//            {
//                sum += scores[i];
//            }
//            return sum;
//        }

//    }
//}

using System;

class Program
{
    static void Main()
    {
        //Console.WriteLine("Enter 5 integers separated by spaces:");
        //int[] numbers = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        //Console.WriteLine("You entered:");
        //Console.WriteLine(string.Join(", ", numbers));
        //int[] arr = new int[5];
        //Array.Fill(arr, 0);
        //Console.Write(string.Join(',',arr));
        int[,,] arr = new int[1, 3, 5]
        {
            {
                {42, 87, 15, 63, 29},
                {94, 51, 76, 38, 12},
                {67, 23, 80, 49, 95}
            }
        };

        //for(int i=0;i< arr.GetLength(0); i++)
        //{
        //    for(int j = 0; j < arr.GetLength(1); j++)
        //    {
        //        for(int k=0; k< arr.GetLength(2); k++)
        //        {
        //            Console.WriteLine(arr[i,j,k]);
        //        }
        //    }
        //}

        //Console.WriteLine(arr.GetLength(2));

        //Console.WriteLine(arr.GetUpperBound(1));
        Console.WriteLine(arr.Rank);


        //Console.WriteLine(Array.IndexOf(arr, 49));
        //Console.WriteLine(Array.LastIndexOf(arr,42));
        //Console.WriteLine(Array.Find(arr, x => x%2 == 0));
        //Console.WriteLine(Array.Exists(arr, x => x< 50));




    }
}
