class BirdCount
{
    private int[] birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        int[] newArray = new int[] {0, 2, 5, 3, 7, 8, 4};
        return newArray;
    }

    public int Today()
    {
        return birdsPerDay[^1];
    }

    public void IncrementTodaysCount()
    {
        this.birdsPerDay[^1] = birdsPerDay[^1] + 1;
    }

    public bool HasDayWithoutBirds()
    {
        foreach (int i in birdsPerDay){
            if (i == 0) {
                return true;
                }
            }
        return false;
    }

    public int CountForFirstDays(int numberOfDays)
    {
        int BirdCount = 0;
        for (int i = 0 ; i < numberOfDays ; i++){
            BirdCount = BirdCount + birdsPerDay[i];
        }
        return BirdCount;
    }

    public int BusyDays()
    {
        int BirdDays = 0;
        for (int i = 0; i < birdsPerDay.Length ; i++){
            if (birdsPerDay[i] >= 5) {
                BirdDays++ ;
            }
        }
        return BirdDays;
    }
}
