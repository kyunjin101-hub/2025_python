class DStudent:
    def __init__(self,stu_id,name):
        self.stu_id=stu_id
        self.name=name
    
    def show_info(self):
        print(f"학번:{self.stu_id}, 이름:{self.name}")

dsstudent1 = DStudent("20251223", "김윤진")

dsstudent1.show_info()