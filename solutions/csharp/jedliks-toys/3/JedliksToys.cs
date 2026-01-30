class RemoteControlCar
{
    public static RemoteControlCar Buy()
    {
        var newCar = new RemoteControlCar();
        return newCar;
    }
    
    public int DistanceDriven;
    public string DistanceDisplay()
    {
        if (DistanceDriven <= 2000){
            return $"Driven {DistanceDriven} meters";
        } else{
            return "Driven 2000 meters";
        }
        
    }

    private int _batteryPercentage = 100;
    public string BatteryDisplay()
    {
        if (_batteryPercentage > 0) {
            return $"Battery at {_batteryPercentage}%";
        } else{
            return "Battery empty";
        }
        
    }

    
    public void Drive()
    {
        _batteryPercentage = _batteryPercentage - 1;
        DistanceDriven = DistanceDriven + 20;
        
    }
}
