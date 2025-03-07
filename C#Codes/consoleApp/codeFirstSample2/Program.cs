using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.EntityFrameworkCore.SqlServer;

namespace codeFirstSample2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using(var db = new AppDbContext())
            {

            }
        }

        class AppDbContext : DbContext
        {
            DbSet<Employee> Employees { get; set; }

            protected override void OnConfiguring(DbContextOptionsBuilder options)
            {
                options.UseSqlServer("Server=localhost;Database=SampleDb2;Trusted_Connection=True;TrustServerCertificate=True;");
            }
        }

        class Employee
        {
            public int Id { get; set; }
            public string Name { get; set; }
            public int Salary  { get; set; }
        }
    }
}
