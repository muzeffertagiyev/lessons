def main():
    score1=int(input("Score1: "))
    score2=int(input("Score2: "))
    score3=int(input("Score3: "))

    print_scores(score1)
    print_scores(score2)
    print_scores(score3)


def print_scores(n):

    for i in range(n):
        print("#",end="")
    print()
    

main()