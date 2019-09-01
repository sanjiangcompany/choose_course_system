
#教师接口
from db import models

#查看老师自己教授的课程接口
def check_course_interface(teacher_name):
    teacher_obj=models.Teacher.select(teacher_name)

    #老师去获取教授课程的数据
    teacher_course_list=teacher_obj.check_course()
    if teacher_course_list:
        return True,teacher_course_list

    return False,f'没有课程'

# 老师选择教授的课程接口
def choose_course_interface(teacher_name,course_name):
    #1、判断课程是否在老师教授课程列表中
    teacher_obj=models.Teacher.select(teacher_name)
    #如果存在，则返回课程已存在
    if course_name in teacher_obj.teacher_course_list:
        return False,f'课程已经存在'

    #如果该课程不存在，则添加该课程
    teacher_obj.choose_course(course_name)
    return True,f'{course_name}----课程添加成功'



#查看老师该课程下的学生接口
def check_student_interface(teacher_name,course_name):
    #1、获取老师对象
    teacher_obj=models.Teacher.select(teacher_name)

    #2、让老师对象去查看该课程下的学生
    student_list=teacher_obj.check_student(course_name)

    if student_list:
        return True,student_list

    return False,f'课程下没有学生'



#老师修改学生成绩接口
def change_score_interface(teacher_name,course_name,student_name,score):
    #1、获取老师对象
    teacher_obj=models.Teacher.select(teacher_name)

    #2、让老师对象去修改成绩
    teacher_obj.change_score(course_name,student_name,score)

    return True,f'修改成绩成功！'













