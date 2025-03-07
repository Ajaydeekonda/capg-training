using System;
using System.Security.Cryptography;
using System.Text;
namespace CSharpPractice2
{
    class User
    {
        private string username;
        private string passwordHash;

        public User(string username, string password)
        {
            this.username = username;
            passwordHash = HashPassword(password);
        }

        private string HashPassword(string password)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
                return Convert.ToBase64String(bytes);
            }
        }

        public bool Authenticate(string password)
        {
            return passwordHash == HashPassword(password);
        }
    }

}
