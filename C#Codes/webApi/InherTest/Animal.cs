namespace InherTest
{
    abstract class Animal
    {
        public abstract void makeSound();
    }

    class Cat: Animal
    {
        public override void makeSound()
        {
            Console.WriteLine("Cat is making sound");
        }
    }

    class Dog : Animal
    {
        public override void makeSound()
        {
            Console.WriteLine("Dog is making sound");
        }
    }

    class AnimalMain
    {
        public static void Main(string[] args)
        {
            Cat cat = new Cat();
            cat.makeSound();
            Dog dog = new Dog();
            dog.makeSound();
        }
    }

}
