using System.Text;

public static class Identifier
{
    public static bool IsGreekLower(char c) => (c >= 'α' && c <= 'ω');
    public static string Clean(string identifier)
    {
        
        bool IsDashBefore = false;
        var cleanString = new StringBuilder();
        foreach (char c in identifier){
            cleanString.Append(c switch {
                _ when IsGreekLower(c) => default,
                _ when IsDashBefore => char.ToUpper(c),
                _ when char.IsWhiteSpace(c) => '_',
                _ when char.IsControl(c) => "CTRL",
                _ when char.IsLetter(c) => c,
                _ => default,
            });
            IsDashBefore = c.Equals('-');
        }
        return cleanString.ToString();
            
    }

  
}