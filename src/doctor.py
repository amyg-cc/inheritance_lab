class Doctor:
    def __init__(self, name, medical_school):
        self.name = name
        self.medical_school = medical_school

    def treat(self):
        return "You should feel better now!"

class Surgeon(Doctor): 
    def __init__(self, name, medical_school, surgical_specialty):
        super().__init__(name, medical_school)
        self.surgical_specialty = surgical_specialty

    def treat(self):
        return f"Snip snip! You should feel better now!"

class GP(Doctor):
    def __init__(self, name, medical_school, patients_assigned):
        super().__init__(name, medical_school)
        self.patients_assigned = patients_assigned

surgeon = Surgeon("Dr Jeckell", "Harvard", "General")
print(surgeon.treat())
print(surgeon.surgical_specialty)

gp = GP("Dr Hyde", "Oxford", 120)
print(gp.treat())
print(gp.patients_assigned)