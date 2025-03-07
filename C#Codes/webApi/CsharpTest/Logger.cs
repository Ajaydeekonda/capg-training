using System;

namespace CsharpTest
{
    public interface ILogger
    {
        void Log(string message);
    }

    public class FileLogger : ILogger
    {
        public void Log(string message)
        {
            Console.WriteLine($"File Log: {message}");
        }
    }

    public class TimestampLogger : ILogger
    {
        private readonly ILogger _logger;

        public TimestampLogger(ILogger logger)
        {
            _logger = logger;
        }

        public void Log(string message)
        {
            _logger.Log($"[{DateTime.Now}] {message}");
        }
    }

    public class ErrorCategoryLogger : ILogger
    {
        private readonly ILogger _logger;

        public ErrorCategoryLogger(ILogger logger)
        {
            _logger = logger;
        }

        public void Log(string message)
        {
            _logger.Log($"[ERROR] {message}");
        }
    }

    class LoggerMain
    {
        static void Main()
        {
            ILogger logger = new FileLogger();
            logger = new TimestampLogger(logger);
            logger = new ErrorCategoryLogger(logger);

            logger.Log("Something went wrong.");
        }
    }
}
