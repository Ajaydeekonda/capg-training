using System;
using System.Collections.Generic;

public interface INotificationObserver
{
    void Update(string message);
}

public class EmailNotifier : INotificationObserver
{
    public void Update(string message)
    {
        Console.WriteLine($"EmailNotifier received: {message}");
    }
}

public class SMSNotifier : INotificationObserver
{
    public void Update(string message)
    {
        Console.WriteLine($"SMSNotifier received: {message}");
    }
}

public class NotificationSubject
{
    private List<INotificationObserver> observers = new List<INotificationObserver>();

    public void RegisterObserver(INotificationObserver observer)
    {
        observers.Add(observer);
    }

    public void UnregisterObserver(INotificationObserver observer)
    {
        observers.Remove(observer);
    }

    public void NotifyObservers(string message)
    {
        foreach (var observer in observers)
        {
            observer.Update(message);
        }
    }
}

public class test19
{
    static void Main(string[] args)
    {
        NotificationSubject subject = new NotificationSubject();

        INotificationObserver emailNotifier = new EmailNotifier();
        INotificationObserver smsNotifier = new SMSNotifier();

        subject.RegisterObserver(emailNotifier);
        subject.RegisterObserver(smsNotifier);

        subject.NotifyObservers("New message arrived!");

        subject.UnregisterObserver(emailNotifier);

        subject.NotifyObservers("Another message arrived!");
    }
}
