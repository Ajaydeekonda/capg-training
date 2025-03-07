namespace CsharpTest
{
    class Book
    {
        public string title;
        public string author;
        public string ISBN;
        Book()
        {
            Console.WriteLine("Default constructor\n");
        }

        Book(string title, string author)
        {
            this.title = title;
            this.author = author;
            Console.WriteLine($"title {this.title}, author {author} are initialised successfully\n");
        }

        Book(string title,string author, string ISBN)
        {
            this.title = title;
            this.author = author;
            this.ISBN = ISBN;
            Console.WriteLine($"title {this.title}, author {author}, ISBN {ISBN} are initialised successfully\n");
        }

        public static void Main(string[] args)
        {
            Book lib = new Book();
            Book lib2 = new Book("The Midnight Library", "Matt Haig");
            Book lib3 = new Book("The Midnight Library", "Matt Haig", "978-0525559474"); 

        }


    }
}
