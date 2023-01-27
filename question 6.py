def student_data(student_id,**kwargs):
    print("Student ID is ",student_id)
    if 'student_name' in kwargs:
        print("Student name is ",kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student class is ",kwargs['student_class'])
    print()

student_data(student_id="22105032")
student_data(student_id="22105032", student_name="Devansh Vashisht")
student_data(student_id="22105032", student_name="Devansh Vashisht", student_class="1st Year ECE")