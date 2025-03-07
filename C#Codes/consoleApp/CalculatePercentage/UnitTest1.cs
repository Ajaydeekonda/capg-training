using System;
using NBomber.CSharp;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading.Tasks;

namespace CalculatePercentage
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var scenario = Scenario.Create("calculate_percentage_test", async context =>
            {
                var options = new ChromeOptions();
                options.AddArgument("--headless"); // Run in headless mode for better performance
                options.AddArgument("--disable-gpu");
                options.AddArgument("--no-sandbox");

                using var driver = new ChromeDriver(options);
                driver.Navigate().GoToUrl("https://www.calculator.net/percent-calculator.html");

                driver.FindElement(By.Id("cpar1")).SendKeys("50");
                driver.FindElement(By.Id("cpar2")).SendKeys("200");
                driver.FindElement(By.Name("x")).Click();

                driver.Quit();

                // Explicitly use NBomber's Response class
                return NBomber.Contracts.Response.Success();
            })
            .WithLoadSimulations(
                Simulation.Inject(rate: 100, // Simulate 100 users per second
                                  interval: TimeSpan.FromSeconds(1),
                                  during: TimeSpan.FromMinutes(2)) // Run the test for 2 minutes
            );

            NBomberRunner
                .RegisterScenarios(scenario)
                .Run();
        }
    }
}
