'''

Исправь класс Tester так, чтобы:

    при вызове метода work_hard у экземпляра класса tester_1 печаталось 'tester_1 Можно отдыхать';
    при вызове метода work_hard у экземпляра класса tester_2 печаталось 'tester_2 Что ж, ещё часок поработаю!'.

'''


class Tester:

    def __init__(self,name, deadline):
        self.name = name
        self.deadline = deadline

    def work_hard(self):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1',deadline=False)
tester_1.work_hard()  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2', deadline=True)
tester_2.work_hard()   # 'tester_2 Что ж, ещё часок поработаю!' 