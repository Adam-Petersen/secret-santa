class Person:
    target = None
    cant_get = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cant_get = []
    def set_cant_get(self, cant_get):
        self.cant_get = cant_get
    def add_cant_get(self, person):
        self.cant_get.append(person)
    def has_target(self):
      return self.target != None
    def print(self):
      print(self.name)
      print(self.email)
      for cant_get in self.cant_get:
        print("Can't get " + cant_get.name)
      print("-----------------")
