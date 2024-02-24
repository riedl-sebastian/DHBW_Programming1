def number_to_words(n):
    einser = ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    halbe = ["zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
    zehner = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
    hunderter = ["", "hundert", "zweihundert", "dreihundert", "vierhundert", "fünfhundert", "sechshundert", "siebenhundert", "achthundert", "neunhundert"]
    
    if n < 10:
        return einser[n]
    elif n < 20:
        return halbe[n-10]
    elif n < 100:
        return zehner[n//10] + (einser[n%10] if n%10 != 0 else "")
    elif n < 1000:
        return hunderter[n//100] + (number_to_words(n%100) if n%100 != 0 else "")
    elif n < 10000:
        return einser[n//1000] + "tausend" + (number_to_words(n%1000) if n%1000 != 0 else "")
    else:
        return "Zahl zu groß"

def count_letters(n):
    return len(number_to_words(n).replace(" ", ""))

print(count_letters(342))  # Beispiel
