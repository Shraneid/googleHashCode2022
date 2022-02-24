from models.skill import Skill


class Contributor:
    def __init__(self, name, number_of_skills):
        self.name = name
        self.number_of_skills = number_of_skills
        self.skills = []
        self.assigned = False

    def add_skill(self, skill):
        self.skills.append(skill)
        if len(self.skills) > self.number_of_skills:
            raise Exception("too many skills, bug")

    def improve_skill(self, skill_name):
        skill: Skill
        for skill in self.skills:
            if skill.name == skill_name and skill.level <= 10:
                skill.level += 1
