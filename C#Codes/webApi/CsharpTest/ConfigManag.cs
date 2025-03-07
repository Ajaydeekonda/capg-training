using System;

namespace CsharpTest
{
    class ConfigManag
    {
        private static ConfigManag _instance;
        private static readonly object _lock = new object();

        private ConfigManag() { }

        public static ConfigManag GetInstance()
        {
            if (_instance == null)
            {
                lock (_lock)
                {
                    if (_instance == null)
                        _instance = new ConfigManag();
                }
            }
            return _instance;
        }

        public void ShowConfig()
        {
            Console.WriteLine("Configuration Loaded");
        }
    }

    class ConfigManagMain
    {
        static void Main()
        {
            ConfigManag config1 = ConfigManag.GetInstance();
            ConfigManag config2 = ConfigManag.GetInstance();

            config1.ShowConfig();

            Console.WriteLine(ReferenceEquals(config1, config2));
        }
    }
}
