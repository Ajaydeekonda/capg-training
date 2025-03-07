namespace UnitTesting.Tests
{
    [TestClass()]
    public class ProgramTests
    {
        public Program program = new Program();

        [TestMethod()]
        public void addTest()
        {
            Assert.AreEqual(3, program.add(1, 2));
        }
    }
}