using System;
public class Studentt
{
    private string _name;
    private int _rollNo;

    public string Name
    {
        get { return _name; }
        set
        {
            if (value == null)
            {
                throw new ArgumentNullException("Name cannot be null");
            }
            _name = value;
        }
    }

    public int RollNo
    {
        get { return _rollNo; }
        set
        {
            if (value <= 0)
            {
                throw new ArgumentOutOfRangeException("RollNo cannot be less than or equal to 0");
            }
            _rollNo = value;
        }
    }

    public Studentt(string name, int rollno)
    {
        Name = name;
        RollNo = rollno;
    }
}

public class test2
{
    public static void Main()
    {
        Studentt s = new Studentt("John", 1);
        Studentt s1 = new Studentt(null, 0);
    }
}
