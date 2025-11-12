from tkinter import *

class Animal:
    def speak(self):
        return "알 수 없음"
    
class Dog(Animal):
    def speak(self):
        return "멍멍!"
    
    
class Cat(Animal):
    def speak(self):
        return "야옹!"
    
class Duck(Animal):
    def speak(self):
        return "꽥꽥!"
    
def make_sound(animal: Animal):
    sound = animal.speak()
    label_result.config(text=sound)
    
root=Tk()
root.title("동물 소리 듣기")
root.geometry("430x180")

Label(root, text="동물 버튼을 눌러 소리를 들어보세요.").pack(pady=8)

frame_btn = Frame(root)
frame_btn.pack(pady=10)
Button(frame_btn, text="강아지", width=12, command=lambda:make_sound(Dog())).pack(side="left", padx=10)
Button(frame_btn, text="고양이", width=12, command=lambda:make_sound(Cat())).pack(side="left", padx=10)
Button(frame_btn, text="오리", width=12, command=lambda:make_sound(Duck())).pack(side="left", padx=10)

label_result = Label(root, text="여기에 울음소리가 나옵니다")
label_result.pack(pady=5)

root.mainloop()