using Microsoft.EntityFrameworkCore;
using System;

class Program
{
    static void Main()
    {
        using (var db = new AppDbContext())
        {
            db.Database.EnsureCreated(); // Create database if it doesn’t exist

            var user = new User { Name = "John Doe" };
            db.Users.Add(user);
            db.SaveChanges();

            Console.WriteLine("User inserted successfully!");
        }
    }
}

public class AppDbContext : DbContext
{
    public DbSet<User> Users { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
    {
        options.UseSqlServer("Server=localhost;Database=SimpleDb;Trusted_Connection=True;TrustServerCertificate=True;");
    }
}

public class User
{
    public int Id { get; set; }
    public string Name { get; set; }
}
