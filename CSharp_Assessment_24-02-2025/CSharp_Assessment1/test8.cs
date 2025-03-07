using System;
public interface IPlayable
{
    void Play();
}

public class MusicPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing music");
    }
}

public class VideoPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing video");
    }
}

public class test8
{
    public static void Main()
    {
        MusicPlayer mp = new MusicPlayer();
        VideoPlayer vp = new VideoPlayer();
        mp.Play();
        vp.Play();
    }
}