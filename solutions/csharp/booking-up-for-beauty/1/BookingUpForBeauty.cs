static class Appointment
{
    public static DateTime Schedule(string appointmentDateDescription)
    {
        return DateTime.Parse(appointmentDateDescription);
    }

    public static bool HasPassed(DateTime appointmentDate)
    {
        int compareValue;
        compareValue = appointmentDate.CompareTo(DateTime.Now);
        return compareValue < 0 ? true : false;
    }

    public static bool IsAfternoonAppointment(DateTime appointmentDate)
    {
        return appointmentDate.Hour >= 12 && appointmentDate.Hour < 18 ? true : false;
    }

    public static string Description(DateTime appointmentDate)
    {
        return $"You have an appointment on {appointmentDate.ToString("G")}.";
    }

    public static DateTime AnniversaryDate(){

        int thisYear = DateTime.Now.Year;
        return new DateTime(thisYear, 9, 15, 0, 0, 0);
        
    }
}
