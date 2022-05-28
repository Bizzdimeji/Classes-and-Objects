class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, tracks:list, score:float):
        self.name=name
        self.age=age
        self.score=score
        self.tracks=tracks
    def change_name(self, new_name:str):
    	self.new_name=new_name
    	self.name=new_name
    	print(self.name)
    def change_age(self, new_age:int):
    	self.new_age=new_age
    	self.age=new_age
    	print(self.age)
    def add_track(self,new_track:str):
    	self.new_track=new_track
    	self.tracks.append(new_track)
    	print(self.tracks)
    def get_score(self):
    	 print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()