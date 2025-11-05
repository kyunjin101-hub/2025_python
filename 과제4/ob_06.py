class Playlist:
    def __init__(self,name):
        self.name = name
        self.tracks = []

    def add(self,track):
        self.tracks.append(track)

    def count(self):
        return len(self.tracks)
    
    def show(self):
        return f"플리명: {self.name}, 곡 수: {self.count()}, 곡들: {self.tracks}"
    
p1 = Playlist("MyList")
p1.add("괴수의 꽃노래")
p1.add("Garden")
print(p1.show())