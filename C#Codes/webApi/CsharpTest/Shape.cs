namespace CsharpTest
{
    abstract class Shape
    {
        public abstract void calculateArea();
    }
    class Circle : Shape
    {
        private int radius;
        float pi = 3.14f;
        public Circle(int radius)
        {
            this.radius = radius;
        }
        public override void calculateArea()
        {
            Console.WriteLine($"The area of the circle: {pi * radius * radius}");
        }
    }

    class Rectangle : Shape
    {
        private int length;
        private int breadth;

        public Rectangle(int length, int breadth)
        {
            this.length = length;
            this.breadth = breadth;
        }

        public override void calculateArea()
        {
            Console.WriteLine($"The area of the rectangle: {length * breadth}");
        }
    }

    class ShapeMain
    {
        public static void Main(string[] args)
        {
            Circle circle = new Circle(10);
            circle.calculateArea();
            Rectangle rectangle = new Rectangle(10, 5);
            rectangle.calculateArea();
            
        }
    }

}
