import re

input = open("2023/inputs/19.txt").read()

workflows, part_ratings = [x.splitlines() for x in input.split("\n\n")]


workflows_by_name = {}
for workflow in workflows:
    workflow = workflow.replace("}", "")
    name, rest = workflow.split("{")
    workflows_by_name[name] = [r for r in rest.split(",") if r]

accepted = 0
for part_rating in part_ratings:
    xmas = {m[0]: int(m[1]) for m in re.findall(r"(\w)=(\d+)", part_rating)}
    locals().update(xmas)

    name = "in"
    while name not in "AR":
        workflows = workflows_by_name[name]
        for workflow in workflows_by_name[name]:
            if ":" in workflow:
                test, move_to = workflow.split(":")
                if eval(test):
                    name = move_to
                    break
            else:
                name = workflow
                break

    if name == "A":
        accepted += sum(xmas.values())

print(accepted)
