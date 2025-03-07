namespace CsharpTest
{

    public interface IPlayable
    {
        public abstract void play();
    }

    class MusicPlayer: IPlayable
    {
        public void play()
        {
            Console.WriteLine("Playing in Music Player");
        }
    }

    class VideoPlayer : IPlayable
    {
        public void play()
        {
            Console.WriteLine("Playing in Video Player");
        }
    }

    class Player
    {
        public static void Main(string[] args)
        {
            MusicPlayer mp = new MusicPlayer();
            mp.play();
            VideoPlayer vp = new VideoPlayer();
            vp.play();
        }
    }
}
