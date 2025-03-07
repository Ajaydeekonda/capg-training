namespace CsharpTest
{
    interface IPrintable
    {
        void displayDetails();
    }

    interface ISerializable
    {
        void saveFile(string filename);
    }

    class Report : IPrintable, ISerializable
    {
        private string reportContent;

        public Report(string content)
        {
            reportContent = content;
        }

        public void displayDetails()
        {
            Console.WriteLine("Report Details:");
            Console.WriteLine(reportContent);
        }

        public void saveFile(string filename)
        {
            try
            {
                File.WriteAllText(filename, reportContent);
                Console.WriteLine($"Report saved to file: {filename}");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error saving file: " + ex.Message);
            }
        }


        static void Main()
        {
            Report report = new Report("This is the report content.");
            report.displayDetails();
            report.saveFile("report.txt");
        }

    }
}
