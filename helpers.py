from person import *
from graph import *

def init_people(cfg):
  people = []
  people_dict = {}

  for person in cfg:
    new_person = Person(person["name"], person["email"])
    people.append(new_person)
    people_dict[new_person.name] = new_person

  for person in cfg:
    people_dict[person["name"]].add_cant_get(people_dict[person["name"]])
    for had_person in person["cant_get"]:
      people_dict[person["name"]].add_cant_get(people_dict[had_person])
  
  return people

def validate(people):
  targets = []
  for person in people:
    if person.target in person.cant_get:
      print(person.name + " can't get " + person.target.name)
      return False
    targets.append(person.target.name)
  for target in targets:
    if targets.count(target) != 1:
      print(target + " was targeted more than once")
      return False
  return True

def validate_x_times(people, x):
  for i in range(0,1000):
    for p in people:
      p.target = None
    G = Graph(people)
    success = G.assign_targets(G.people[0])

    if not success:
      print("Algorithm failed")
    if not validate(people):
      print("Invalid Result")
  print("success!")

def print_num_combos(people):
  G = Graph(people)
  combos = G.get_num_combos()
  print(combos)

def print_sample_run(people):
  G = Graph(people)
  res = G.assign_targets(G.people[0])
  if res:
    for p in people:
      print(p.name + " has " + p.target.name)

