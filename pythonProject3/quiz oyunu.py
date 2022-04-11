class Questions:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f'Soru {self.question_index + 1}: {question.text}')

        for q in question.choices:
            print(f'-{q}')

        answer = input('cevap: ')
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

    def load_question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print('Score: ',self.score)
        print('Quiz bitti.')

    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            pass
        else:
            print(f'Question {question_number} of {total_question}'.center(100,'*'))

q1 = Questions('En iyi programlama dili hangisidir ?',['python','java','php','c#'],'python')
q2 = Questions('En popüler programlama dili hangisidir ?',['python','java','php','c#'],'python')
q3 = Questions('En çok kazandıran programlama dili hangisidir ?',['python','java','php','c#'],'python')
q4 = Questions('En çok sevilen programlama dili hangisidir ?',['python','java','php','c#'],'python')
q5 = Questions('En kolay programlama dili hangisidir ?',['python','java','php','c#'],'python')

questions=[q1,q2,q3,q4,q5]
quiz = Quiz(questions)
quiz.load_question()
