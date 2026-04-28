class Password_Checker:
    def __init__ (self):
        self.strength = 0
        self.characters = 0 
        self.special_char = 0 
        self.upper = 0 
        self.numbers = 0 
        self.upassword = None
        self.special = ('!', '@', '#', '$', '%', '^', '&', '*')
        self.suggestions = {
            '8<characters':'You need atleast 12 characters for a strong password!',
            '1<specialchar': f'You need atleast one special character {self.special}!',
            '1<upper':'You need atleast 1 uppercase letter',
            '1<num': 'You need atleast 1 number'
        }
        self.problems = []
        self.progress = [] # make a bar of percent and shows the percent

    def password(self):
        print('Testing password')
        self.upassword = input('What is your password: ')
        
        self.upper = len([char for char in self.upassword if char.isupper()])
        
        self.characters = len(self.upassword)
        
        self.numbers = sum(char.isdigit() for char in self.upassword)

        for spec in self.special:
            for i in self.upassword:
                if spec == i:
                    self.special_char += 1


    
    def check(self):
        #Characters
        if self.characters == 8:
            self.strength += 3
            self.problems.append(self.suggestions['8<characters'])
        elif self.characters >= 12:
            self.strength += 4
        elif self.characters < 8:
            self.problems.append(self.suggestions['8<characters'])
        #Special Characters
        if self.special_char >= 1:
            self.strength += 2
        else:
            self.problems.append(self.suggestions['1<specialchar'])

        #Upper characters
        if self.upper >= 1:
            self.strength += 2
        else:
            self.problems.append(self.suggestions['1<upper'])

        #Numbers
        if self.numbers >= 1:
            self.strength += 2
        else:
            self.problems.append(self.suggestions['1<num'])

        #percent
        for i in range(self.strength):
            self.progress.append('█') 
        for i in range(10-self.strength):
            self.progress.append('░')
    
    def result (self):
        print(f'('+ ''.join(self.progress) + f'{self.strength*10}%)')
        print('Suggestions:')
        
        for i in self.problems:
            print(i)
        
        if self.strength <= 4:
            rating = "Weak"
        elif self.strength <= 7:
            rating = "Medium"
        elif self.strength <= 9:
            rating = "Strong"
        else:
            rating = "Very Strong"

        print(f"Strength: {rating}")






main = Password_Checker()

while True:
    main.password()
    main.check()
    main.result()
    main = Password_Checker()