class Skill:
    def __init__(self, skill_name, skill_level):
        self.name = skill_name
        self.level = skill_level

    def does_work(self, skill):
        return self.name == skill.name and self.level <= skill.level
