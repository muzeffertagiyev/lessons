class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.number_of_correct_answer = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        # if this statement true our
        # input function will until it is false,and it will return true and false

    def next_question(self):
        our_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Category: {our_question.q_category}\nDifficulty: {our_question.q_difficulty}")
        user_answer = input(f"Q.{self.question_number}: {our_question.q_text}.(True/False): ").capitalize()
        self.check_answer(user_answer, our_question.q_answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.number_of_correct_answer += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.number_of_correct_answer} / {self.question_number}\n")
