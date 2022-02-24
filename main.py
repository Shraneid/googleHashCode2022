import parserInputFiles


def writeOutput(projects):
    f = open("output.txt", "w")

    f.write(str(len(projects)) + "\n")

    for project in projects:
        f.write(project.name + "\n")
        f.write(' '.join([c.name for c in project.contributors]) + "\n")

    f.close()


def all_projects_not_completed(projects):
    return not all(project.completed for project in projects)


def optimize_projects():
    file_path = "./b_better_start_small.in.txt"
    with open(file_path) as f:
        contributors, projects = parserInputFiles.parse(f.readlines())

        # sorting by score first
        projects.sort(key=lambda project: project.max_score, reverse=True)

        while all_projects_not_completed(projects):
            for project in projects:
                for pskill in project.skills_needed:
                    for contributor in contributors:
                        for cskill in contributor.skills:
                            if pskill.does_work(cskill):
                                project.assign_contributor(contributor)
                                contributor.improve_skill(cskill.name)

        writeOutput(projects)


if __name__ == '__main__':
    optimize_projects()
