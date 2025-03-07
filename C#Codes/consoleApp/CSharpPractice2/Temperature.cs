namespace CSharpPractice2
{
    class Temperature
    {
        private double celsius;

        public Temperature(double celsius)
        {
            if (celsius < -273.15)
                throw new ArgumentException("Temperature cannot be below absolute zero.");
            this.celsius = celsius;
        }

        public double ToFahrenheit()
        {
            return (celsius * 9 / 5) + 32;
        }

        public double ToKelvin()
        {
            return celsius + 273.15;
        }
    }

}
