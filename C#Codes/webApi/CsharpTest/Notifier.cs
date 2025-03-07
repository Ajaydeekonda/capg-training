using System;
using System.Collections.Generic;

namespace CsharpTest
{
    public interface INotificationObserver
    {
        void Update(string message);
    }

    public class EmailNotifier : INotificationObserver
    {
        public void Update(string message)
        {
            Console.WriteLine($"Email Notification: {message}");
        }
    }

    public class SMSNotifier : INotificationObserver
    {
        public void Update(string message)
        {
            Console.WriteLine($"SMS Notification: {message}");
        }
    }

    public class Notifier
    {
        private List<INotificationObserver> observers = new List<INotificationObserver>();

        public void Subscribe(INotificationObserver observer)
        {
            observers.Add(observer);
        }

        public void Unsubscribe(INotificationObserver observer)
        {
            observers.Remove(observer);
        }

        public void Notify(string message)
        {
            foreach (var observer in observers)
            {
                observer.Update(message);
            }
        }
    }

    class NotifierMain
    {
        static void Main()
        {
            Notifier notifier = new Notifier();

            EmailNotifier emailNotifier = new EmailNotifier();
            SMSNotifier smsNotifier = new SMSNotifier();

            notifier.Subscribe(emailNotifier);
            notifier.Subscribe(smsNotifier);

            notifier.Notify("New notification received.");
        }
    }
}
