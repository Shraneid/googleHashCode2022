from models.contributor import Contributor
from models.project import Project
from models.skill import Skill


def parse(txt):
    nb_of_contributors, nb_of_projects = int(str(txt[0]).strip().split(' ')[0]), int(str(txt[0]).strip().split(' ')[1])

    index = 1

    conts = []
    projs = []

    for i in range(nb_of_contributors):
        contributor = Contributor( str(txt[index]).strip().split(' ')[0], int(str(txt[index]).strip().split(' ')[1]) )
        index += 1

        for j in range(contributor.number_of_skills):
            skill = Skill( str(txt[index]).strip().split(' ')[0], int(str(txt[index]).strip().split(' ')[1]) )

            contributor.add_skill(skill)
            index += 1

        conts.append(contributor)

    for i in range(nb_of_projects):
        project = Project(
            str(txt[index]).strip().split(' ')[0],
            int(str(txt[index]).strip().split(' ')[4]),
            int(str(txt[index]).strip().split(' ')[1]),
            int(str(txt[index]).strip().split(' ')[2]),
            int(str(txt[index]).strip().split(' ')[3])
        )
        index += 1

        for j in range(project.nb_of_skills):
            skill = Skill( str(txt[index]).strip().split(' ')[0], int(str(txt[index]).strip().split(' ')[1]) )

            project.add_skill(skill)
            index += 1

        projs.append(project)

    return conts, projs
