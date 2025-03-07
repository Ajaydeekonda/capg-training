using TestNinja.Fundamentals;

namespace TestNinja.UnitTests
{
    [TestFixture]
    public class ReservationTest
    {
        private Reservation reservation;
        private Reservation reservation2;
        private User user;
        private User user2;
        [SetUp]
        public void Setup()
        {
            reservation = new Reservation();
            user = new User();
            reservation2 = new Reservation() { MadeBy = user };
            user2 = new User();
        }

        [Test]
        public void CanBeCancelledBy_UserIsAdmin_ReturnsTrue()
        {
            var result = reservation.CanBeCancelledBy(new User() { IsAdmin = true});

            Assert.IsTrue(result);
        }

        [Test]
        public void CanBeCancelledBy_SameUserCancelling_ReturnTrue()
        {
            var result = reservation2.CanBeCancelledBy(user);
            Assert.IsTrue(result);
        }

        [Test]
        public void CanBeCanelledBy_AnotherUserCancelling_ReturnTrue()
        {
            var result = reservation.CanBeCancelledBy(user2);
            Assert.IsFalse(result);
        }
    }
}