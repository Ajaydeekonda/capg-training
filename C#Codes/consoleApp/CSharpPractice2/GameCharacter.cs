
namespace CSharpPractice2
{
    class GameCharacter
    {
        private int health;
        private int stamina;
        private int attackPower;

        public GameCharacter(int health, int stamina, int attackPower)
        {
            this.health = health > 0 ? health : 0;
            this.stamina = stamina > 0 ? stamina : 0;
            this.attackPower = attackPower > 0 ? attackPower : 0;
        }

        public void TakeDamage(int damage)
        {
            if (damage > 0)
            {
                health -= damage;
                if (health < 0)
                    health = 0;
            }
        }

        public void Attack(GameCharacter target)
        {
            if (stamina > 0)
            {
                target.TakeDamage(attackPower);
                stamina--;
            }
        }

        public int GetHealth()
        {
            return health;
        }
    }

}
