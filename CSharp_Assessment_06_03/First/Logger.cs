using System;
using System.IO;

interface ILogger
{
    void Log(string message);
}

class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine($"Console Log: {message}");
    }
}

class FileLogger : ILogger
{
    private string filePath = "log.txt";

    public void Log(string message)
    {
        File.AppendAllText(filePath, $"File Log: {message}{Environment.NewLine}");
    }
}

class Application
{
    private readonly ILogger _logger;

    public Application(ILogger logger)
    {
        _logger = logger;
    }

    public void Run()
    {
        _logger.Log("Application started.");
    }
}

class LoggerMain
{
    static void Main()
    {
        ILogger logger = new ConsoleLogger(); // Switch to new FileLogger() if needed
        Application app = new Application(logger);
        app.Run();
    }
}
