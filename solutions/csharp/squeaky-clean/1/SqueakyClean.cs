using System.Text;

public static class Identifier
{
    public static string Clean(string identifier)
    {
        /* Step 3 - Kebab-Case to camelCase */
        var cleanString = new StringBuilder();
        bool nextCharDash = false;
        foreach (char c in identifier){
            if (c == '-'){
                nextCharDash = true;
                continue;
            } 
            if (nextCharDash) {
                cleanString.Append(char.ToUpper(c));
                nextCharDash = false;
                continue;
            }
             if (!char.IsLetter(c) && (c != ' ' && c != '\0')){
                 /* step 4 remove chars that are not letters */
                continue;
            }
            if (char.IsLower(c) && (c >= '\u0370' && c <= '\u03FF') && (c != ' ' && c != '\0')){
                /* remove lowercase greek letters*/
                continue;
                
            }
            else {
                cleanString.Append(c);
                continue;
            }
            
        }
        /* Step 1 and 2 string cleaner */
        return cleanString.ToString().Replace(" ", "_").Replace("\0","CTRL");
            
        }

        
    }

/*
   string newString;
        newString = identifier.Replace(" ", "_").Replace("\0","CTRL");

        foreach ()
        int indexChar
        char charAtCase = identifier["-"+1];
        newString = identifier.Replace($"{charAtCase}", $"{charAtCase.ToUpper}");
        newString = identifier.Replace("-", "");
        return newString;

        foreach (char c in cleanString) {
            if (c == '-'){
                char stringDash = '-';
                int charToFind = cleanString.IndexOf(c);
                int charToReplace = cleanString.IndexOf(c) + 1;
            }
    }    
identifier.Replace(" ", "_").Replace("\0","CTRL");
        return identifier;



    foreach (char c in identifier){
            if (char.IsLetter(c)){
                cleanString.Append(c);
            }
    */
    
/*
        
*/