using System;

abstract class Book
{
    public string Title { get; set; }
    public string Author { get; set; }
    public string ISBN { get; set; }
    public bool IsAvailable { get; private set; } = true;

    public void BorrowBook()
    {
        if (IsAvailable)
        {
            IsAvailable = false;
            Console.WriteLine($"{Title} has been borrowed.");
        }
        else
        {
            Console.WriteLine($"{Title} is already checked out.");
        }
    }

    public void ReturnBook()
    {
        IsAvailable = true;
        Console.WriteLine($"{Title} has been returned.");
    }
}
