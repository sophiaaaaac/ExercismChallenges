class RemoteControlCar
{
    private int _distanceDriven = 0;
    private int _batteryPercentage = 100;
    
    public static RemoteControlCar Buy() => new RemoteControlCar();
    
    public string DistanceDisplay()
    {
        return $"Driven {_distanceDriven} meters";
    }

    
    public string BatteryDisplay()
    {
        return _batteryPercentage > 0  ? $"Battery at {_batteryPercentage}%":"Battery empty";
    }

    public void Drive()
    {
        if (this._batteryPercentage > 0){
            this._batteryPercentage -= 1;
            this._distanceDriven += 20;
        }
        
        
    }
}
