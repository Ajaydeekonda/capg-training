using System;

public sealed class ConfigurationManager
{
    private static readonly Lazy<ConfigurationManager> instance = new Lazy<ConfigurationManager>(() => new ConfigurationManager());

    private ConfigurationManager()
    {

    }

    public static ConfigurationManager Instance
    {
        get
        {
            return instance.Value;
        }
    }

    public string GetSetting(string key)
    {
        return "DummyValue";
    }
}

class test18
{
    static void Main(string[] args)
    {
        ConfigurationManager configManager1 = ConfigurationManager.Instance;
        ConfigurationManager configManager2 = ConfigurationManager.Instance;

        Console.WriteLine(configManager1 == configManager2); 

        string settingValue = configManager1.GetSetting("exampleKey");
        Console.WriteLine(settingValue);
    }
}
