using Microsoft.EntityFrameworkCore;
using PracticeProject.Models.Entities;

namespace PracticeProject.Data
{
    public class ApplicationDbContext : DbContext
    {
      
        public ApplicationDbContext(DbContextOptions options) : base(options)
        {
        }
        public DbSet<Employee> Employees { get; set; }
    }
}
