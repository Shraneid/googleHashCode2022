class Project:
    def __init__(self,
                 project_name: str,
                 nb_of_skills: int,
                 nb_of_days_to_finish_project: int,
                 deadline: int,
                 max_score: int):
        self.name = project_name
        self.nb_of_skills = nb_of_skills

        self.nb_of_days_to_finish_project = nb_of_days_to_finish_project
        self.deadline = deadline

        self.max_score = max_score
        self.current_score = max_score

        self.completed = False

        self.skills_needed = []
        self.contributors = []
        
    def add_skill(self, skill):
        self.skills_needed.append(skill)
        if len(self.skills_needed) > self.nb_of_skills:
            raise Exception("number of skills too high, bugged")

    def assign_contributor(self, contributor):
        self.contributors.append(contributor)

        if len(self.contributors) == self.nb_of_skills:
            self.completed = True
