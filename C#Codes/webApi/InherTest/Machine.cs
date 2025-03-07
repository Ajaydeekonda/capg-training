namespace InherTest
{
    interface IMovable
    {
        void Move();
    }
    class Machine
    {
        public void start()
        {
            Console.WriteLine("Start the machine");
        }
    }

    class Robot: Machine, IMovable 
    {
        public void Move()
        {
            Console.WriteLine("move the Robot");
        }

    }

    class MachineMain
    {
        public static void Main(string[] args)
        {
            Robot robot = new Robot();
            robot.Move();
            robot.start();
        }
    }
}
