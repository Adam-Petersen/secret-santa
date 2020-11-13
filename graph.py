import random
from random import randint
from random import shuffle

class Graph:
  def __init__(self, people):
    self.people = people
    self.targeted = {} # Specifies whether a person is currently being targeted
    self.old_edges_collection = {} # Used in assigning algorithm for restoring destroyed edges
    self.visited = {} # Used in DFS
    for p in people:
      self.visited[p] = False
      self.targeted[p] = False
      self.old_edges_collection[p] = {}
    self.init_edges()

  # Set edges between every person and remove ones that violate people's cant_get list
  def init_edges(self):
    self.edges = {}
    for p1 in self.people:
      self.edges[p1] = {}
      for p2 in self.people:
        self.edges[p1][p2] = True
      self.edges[p1][p1] = False
      for p2 in p1.cant_get:
        self.edges[p1][p2] = False

  # Returns true if every person has a target
  def complete(self):
    for p in self.people:
      if not p.has_target():
        return False
    return True

  # Returns true if person has no potential targets or if person can't be targeted, false otherwise
  def bad_state(self):
    for p1 in self.people:
      if not p1.has_target():
        no_targets = True
        for p2 in self.people:
          if self.edges[p1][p2]:
            no_targets = False
        if no_targets:
          return True
      if not self.targeted[p1]:
        cant_be_targeted = True
        for p2 in self.people:
          if self.edges[p2][p1]:
            cant_be_targeted = False
        if cant_be_targeted:
          return True
    return False

  # Returns possible targets for given person
  def get_targets(self, person):
    targets = []
    for p2 in self.people:
      if self.edges[person][p2]:
        targets.append(p2)
    return targets

  # Returns possible targets for given person in random order
  def get_targets_random(self, person):
    targets = self.get_targets(person)
    shuffle(targets)
    return targets

  # Gets blank data structure representing old edges that could need to be restored
  def get_blank_old_edge_dict(self):
    d = {}
    for p in self.people:
      d[p] = []
    return d

  # Assigns target to person, removes other edges pointing out from person, and removes other edges pointing to target
  def set_target(self, person, target):
    person.target = target
    self.targeted[target] = True
    old_edges = self.get_blank_old_edge_dict()
    for p2 in self.people:
      if p2 != target and self.edges[person][p2]:
        old_edges[person].append(p2)
        self.edges[person][p2] = False
      if p2 != person and self.edges[p2][target]:
        old_edges[p2].append(target)
        self.edges[p2][target] = False
    self.old_edges_collection[person] = old_edges

  # Reverts target assignment and restores all edges destroyed when assignemnt happened
  def revert_target(self, person):
    self.targeted[person.target] = False
    person.target = None
    old_edges = self.old_edges_collection[person]
    for p1 in self.people:
      for p2 in old_edges[p1]:
        self.edges[p1][p2] = True
    self.old_edges_collection[person] = {}

  # Main algorithm that randomly assigns people using recursion
  def assign_targets(self, person):
    if self.complete():
      return True
    elif self.bad_state():
      return False

    targets = self.get_targets_random(person)
    valid_target_found = False

    for target in targets:
      if not self.targeted[target]:
        self.set_target(person, target)
        valid_target_found = self.assign_targets(target)
        if valid_target_found:
          return True
        else:
          self.revert_target(person)
    return False

  # Determines possible number of assignment combinations given a root node
  def get_num_combos(self, person, tally):
    if self.complete():
      return tally + 1
    elif self.bad_state():
      return tally

    targets = self.get_targets(person)
    valid_target_found = False

    for target in targets:
      if not self.targeted[target]:
        self.set_target(person, target)
        new_tally = self.get_num_combos(target, tally)
        if new_tally > tally:
          self.revert_target(person)
          tally = new_tally
        else:
          self.revert_target(person)
    return tally

  # Overload for initial call
  def get_num_combos(self):
    return get_num_combos(self.people[0], 0)
