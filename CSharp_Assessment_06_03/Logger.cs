using System;
using System.Collections.Generic;

namespace CSharpPractice2
{

    class Logger
    {
        private List<string> logs = new List<string>();

        public void Log(string message)
        {
            logs.Add($"{DateTime.Now}: {message}");
        }

        public IReadOnlyList<string> GetLogs()
        {
            return logs.AsReadOnly();
        }
    }

}
