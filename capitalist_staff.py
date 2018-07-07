# Contains Data and actions related to employees
import capitalist_business
import capitalist_math
class employee:
    first_name = "Capitalist"
    last_name = "Worker"
    gender = "male"
    age = 21
    profession = "Guard"
    bio = "Default employee preset"
    job = None
    project = 0
    salary = 0 #Value in currency units
    moral = 1
    health = 1
    body_type = "Muscular"
    intimidation_skill = 1
    fighting_skill = 1
    cooking_skill = 1
    logic_skill = 1
    engineering_skill = 1
    organisation_skill = 1
    leadership_skill = 1
    def edit_meta(self):
        pass
    def set_skills(self):
        pass
    def randomise_skills(self):
        pass
    def hire(self,business,job,salary):
        self.job = job
        self.salary = salary
        self.moral = 1 #capitalist_math.calculate_moral()
        business.employees.append(self)
    def fire(self,business):
        #I don't like this implementation but could not think of one where i dont have to use business as an argument.
        #Python experts do your thing!
        business.employees.remove(self)
        self.job = None
        self.salary = 0
        self.moral = 1 #capitalist_math.calculate_moral()
def seach():
    pass
