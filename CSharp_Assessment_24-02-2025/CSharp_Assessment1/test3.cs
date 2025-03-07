using System;
public class Library
{
    public string Title { get; set; }
    public string Author { get; set; }
    public string Isbn { get; set; }
    public Library()
    {
        Title = "Title";
        Author = "Author";
        Isbn = "Isbn";
    }
    public Library(string title, string author)
    {
        Title = title;
        Author = author;
    }

    public Library(string title, string author, string isbn)
    {
        Title = title;
        Author = author;
        Isbn = isbn;
    }

}

public class test3
{
    public static void Main()
    {
        Library l = new Library("Title", "Author", "Isbn");
        Library l1 = new Library("Title", "Author");
        Library l2 = new Library();
    }
}