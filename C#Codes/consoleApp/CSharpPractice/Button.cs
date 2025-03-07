using System;

class Button
{
    public event Action OnClick;

    public void Click()
    {
        OnClick?.Invoke();
    }
}

class Subscriber
{
    public void HandleClick()
    {
        Console.WriteLine("Button was clicked.");
    }
}
