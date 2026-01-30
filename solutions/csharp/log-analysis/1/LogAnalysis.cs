public static class LogAnalysis 
{
    // TODO: define the 'SubstringAfter()' extension method on the `string` type
    public static string SubstringAfter(this string str, string delim){
        return str[(str.IndexOf(delim) + delim.Length)..];
    }

    // TODO: define the 'SubstringBetween()' extension method on the `string` type
    public static string SubstringBetween(this string str, string delimOne, string delimTwo){
        return str[(str.IndexOf(delimOne)+ delimOne.Length)..(str.IndexOf(delimTwo))].Trim();
    }
    
    // TODO: define the 'Message()' extension method on the `string` type

    public static string Message(this string str){
        return str = SubstringAfter(str, ": ");
    }

    // TODO: define the 'LogLevel()' extension method on the `string` type

    public static string LogLevel(this string str){
        return str = SubstringBetween(str, "[", "]");
    }
}