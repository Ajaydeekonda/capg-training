public class Student
{
    public int Id { get; set; }
    public required string Name { get; set; } // Ensures Name is always initialized.
    public int Age { get; set; }
}
