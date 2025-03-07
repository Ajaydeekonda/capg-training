using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public interface IMovable
{
    void Move();
}

public class Machine
{
    public void Start()
    {
        Console.WriteLine("Machine is starting");
    }
}
public class Robot : Machine, IMovable
{
    public void Move()
    {
        Console.WriteLine("Robot is moving");
    }
}

public class test5
{
    public static void Main()
    {
        Robot robot = new Robot();
        robot.Start();
        robot.Move();
    }
}