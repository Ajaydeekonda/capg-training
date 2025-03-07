using System;

abstract class SmartDevice
{
    public string DeviceName { get; set; }
    public bool Status { get; protected set; }

    public SmartDevice(string deviceName)
    {
        DeviceName = deviceName;
    }

    public abstract void TurnOn();
    public abstract void TurnOff();
}

class LightBulb : SmartDevice
{
    public LightBulb(string deviceName) : base(deviceName) { }

    public override void TurnOn()
    {
        Status = true;
        Console.WriteLine($"{DeviceName} is now ON.");
    }

    public override void TurnOff()
    {
        Status = false;
        Console.WriteLine($"{DeviceName} is now OFF.");
    }
}

class SmartThermostat : SmartDevice
{
    public double Temperature { get; private set; }

    public SmartThermostat(string deviceName) : base(deviceName) { }

    public override void TurnOn()
    {
        Status = true;
        Temperature = 22.0;
        Console.WriteLine($"{DeviceName} is ON. Temperature set to {Temperature}°C.");
    }

    public override void TurnOff()
    {
        Status = false;
        Console.WriteLine($"{DeviceName} is OFF.");
    }
}
