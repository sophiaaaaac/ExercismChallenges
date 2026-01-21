static class LogLine
{

    //todo - make string static so it can be accessed everywhere
    
    public static string Message(string logLine)
    {
        List<string> stringsToRemove = new List<string> {"[INFO]:", "[WARNING]:", "[ERROR]:"};

        foreach (string s in stringsToRemove){
            logLine = logLine.Replace(s, "").Trim();
        };
        return logLine;
    }

    public static string LogLevel(string logLine)
    {
        List<string> stringsToFind = new List<string> {"[INFO]:", "[WARNING]:", "[ERROR]:"};

        foreach (string s in stringsToFind){
            if (logLine.Contains(s)){
                char[] TrimMe = {'[', ']', ':'};
                logLine = s.Trim(TrimMe).ToLower();
            };
        };
        return logLine;
        
    }

    public static string Reformat(string logLine)
    {
        List<string> stringsToFind = new List<string> {"[INFO]:", "[WARNING]:", "[ERROR]:"};

        foreach (string s in stringsToFind){
            if (logLine.Contains(s)){
                char[] TrimMe = {'[', ']', ':'};
                logLine = logLine.Replace(s, "").Trim();
                logLine = logLine + " (" + s.Trim(TrimMe).ToLower() + ")";
            };
        };
        return logLine;
        
    }
}
