

namespace CsharpTest
{
    public delegate void ButtonClickHandler();

    public class Button
    {
        public event ButtonClickHandler OnClick;

        public void Click()
        {
            Console.WriteLine("Button clicked!");
            OnClick?.Invoke();
        }
    }

    public class EventListener
    {
        public void HandleButtonClick()
        {
            Console.WriteLine("Button click event handled!");
        }
    }

    class ButtonMain
    {
        static void Main()
        {
            Button button = new Button();
            EventListener listener = new EventListener();

            button.OnClick += listener.HandleButtonClick;

            button.Click();
        }
    }
}
