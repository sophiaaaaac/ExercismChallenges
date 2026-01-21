static class LogLine
{

    //todo - make string static so it can be accessed everywhere
    
    public static string Message(string logLine)
    {
        logLine = logLine[(logLine.IndexOf(':')+ 1)..].Trim();
        return logLine;
    }

    public static string LogLevel(string logLine)
    {
        logLine = logLine[1..(logLine.IndexOf(']'))].Trim().ToLower();
        return logLine;
        
    }

    public static string Reformat(string logLine)
    {
        logLine = $"{Message(logLine)} ({LogLevel(logLine)})";
        return logLine;
        
    }
}
