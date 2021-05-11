import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()


def Translate(w):
    w = w.lower()
    wc = w.capitalize()
    wu = w.upper()

    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % w)
    results = cursor.fetchall()
    if results:
        return results
    
    Cquery = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % wc)
    Cresults = cursor.fetchall()
    if Cresults:
        return Cresults
    
    Uquery = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % wu)
    Uresults = cursor.fetchall()
    
    if Uresults:
        return Uresults

    close_query = cursor.execute("SELECT Expression FROM Dictionary")
    close_results = cursor.fetchall()
    close_results = [r[0] for r in close_results]
    bestmatches = get_close_matches(w, close_results, n = 5, cutoff = 0.7)

    if len(bestmatches) > 0:
        yn = input("Did you mean '%s' instead? Enter Y if yes, or N if no: " % bestmatches[0])
        if yn == 'Y':
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s' " % bestmatches[0])
            results = cursor.fetchall()
            return results
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "Please enter Y or N."
    else:
        return "The word doesn't exist. Please double check it."



typein = input("Enter a word: ")
word = Translate(typein)
#print(word)

if type(word) == list:
    for explanation in word:
        print(explanation[0])
else:
    print(word)

