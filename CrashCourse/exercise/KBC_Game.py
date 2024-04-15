# Create a KBC game where the user is asked question and the for correct answer the amount is given to the participants

print("\tNamaskar Deviyo Aur Sajano!!!!\n\tSwagat hai Apka Kaun Banega Crorpati mein!!!!!")

questionsSet = [("Which planet has the most moons?", 1000, ["Jupiter", "Neptune", "Saturn", "Mars"], "Saturn"),
                ("What country has won the most World Cups?", 5000, ["Germany", "Italy", "Brazil", "Argentina"],
                 "Brazil"),
                ("What Netflix show had the most streaming views in 2021?", 10000,
                 ["Squid Game", "Stranger Things", "Money Heist", "Wednesday"], "Squid Game"),
                ("In what country is the Chernobyl nuclear plant located?", 20000,
                 ["Russia", "Ukraine", "Poland", "Belarus"], "Ukraine")]


def check_answer(option, tup, correct_answer):
    match option:
        case "A" | "a":
            return check_index_with_answer(tup[0], correct_answer)
        case "B" | "b":
            return check_index_with_answer(tup[1], correct_answer)
        case "C" | "c":
            return check_index_with_answer(tup[2], correct_answer)
        case "D" | "d":
            return check_index_with_answer(tup[3], correct_answer)
        case _:
            return False


def check_index_with_answer(submitted_answer, correct_answer):
    if submitted_answer == correct_answer:
        return True
    else:
        return False


sum = 0

for idx, i in enumerate(questionsSet):
    print(idx + 1, "Question for Rs", i[1], "is :")
    print(i[0])
    # print("Your Options are :")
    print("A :", i[2][0], "\nB :", i[2][1], "\nC :", i[2][2], "\nD :", i[2][3])
    ans = input("Your Answer : ")
    if check_answer(ans, i[2], i[3]):
        sum += i[1]
        print("Amazing You have won Rs", sum)
        print("")
    else:
        print("Ohhh oh Sorry wrong answer... Your won Rs", sum)
        break
