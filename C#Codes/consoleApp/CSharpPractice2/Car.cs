namespace CSharpPractice2
{
    class Car
    {
        private int speed;
        private const int MAX_SPEED = 200;

        public void Accelerate(int value)
        {
            speed += value;
            if (speed > MAX_SPEED)
                speed = MAX_SPEED;
        }

        public void Brake(int value)
        {
            speed -= value;
            if (speed < 0)
                speed = 0;
        }

        public int GetSpeed()
        {
            return speed;
        }
    }
}
