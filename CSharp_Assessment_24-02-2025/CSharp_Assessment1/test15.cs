using System;

public class Button
{
    public delegate void ClickHandler();

    public event ClickHandler OnClick;

    public void Click()
    {
        if (OnClick != null)
        {
            OnClick();
        }
    }
}

public class test15
{
    public static void Main()
    {
        Button button = new Button();

        button.OnClick += ButtonClicked;

        button.Click();
    }

    public static void ButtonClicked()
    {
        Console.WriteLine("Button was clicked!");
    }
}

