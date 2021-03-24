part_of_verse = "day of christmas, my true love sent to me, "
first_part = "On the "

days = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eight",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}
verses = {
    1: "a partridge in a pear tree.",
    2: "two turtle doves,",
    3: "three French hens, ",
    4: "four calling birds, ",
    5: "five gold rings, ",
    6: "six geese a-laying, ",
    7: "seven swans a-swimming, ",
    8: "eight maids a-milking, ",
    9: "nine ladies dancing, ",
    10: "ten lords a-leaping, ",
    11: "eleven pipers piping, ",
    12: "twelve drummers drumming, "
}


def days_of_christmas():
    returned_verse = " "
    for i, day_value in days.items():
        returned_day = day_value
        for j, verse_value in verses.items():
            if i == j:
                new_verse = returned_verse
                returned_verse = verse_value
                returned_verse += new_verse
                print(f"{first_part} {returned_day}  {part_of_verse} {returned_verse}")


days_of_christmas()
