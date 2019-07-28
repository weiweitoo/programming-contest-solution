ORDINALS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

GIFTS = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]

def recite(start_verse, end_verse):
    recite = []
    for i in range(start_verse, end_verse + 1):
        result = "On the "
        result += ORDINALS[i-1] + " day of Christmas my true love gave to me: "
        if i == 1:
            result += GIFTS[0] + "."
        else:
            for x in range(i, 0, -1):
                if x != 1:
                    result += GIFTS[x-1] + ", "
                else:
                    result += "and " + GIFTS[x-1] + "."
        recite.append(result)
    return recite




