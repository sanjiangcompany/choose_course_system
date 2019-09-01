#管理员接口层

from db import models

#管理员注册接口
def register_interface(username,password):
    #1、首先判断该用户是否已经注册过了
    admin_obj=models.Admin.select(username)
    if admin_obj:
        return False,f'用户已存在'

    #2、不存在就保存用户数据
    models.Admin(username,password)
    return True,f'{username}---注册成功'


#管理员创建学校接口
def create_school_interface(admin_name,school_name,school_addr):
    #1、判断学校是否存在
    school_obj=models.Student.select(school_name)
    if school_obj:
        return False,f'学校已经存在'

    #2、如果学校不存在则保存学校
    #获取管理员对象，让管理员来创建学校
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_school(
        school_name,school_addr
    )

    return True,f'{school_name}----学校创建成功'




#管理员创建老师接口
def create_teacher_interface(admin_name,teacher_name,teacher_pwd='123'):
    teacher_obj=models.Teacher.select(teacher_name)
    if teacher_obj:
        return False,'老师已存在'

    #通过管理员对象，来创建老师
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,teacher_pwd)

    return True,f'{teacher_name}---创建成功'




#管理员创建学校课程
def create_course_interface(admin_name,school_name,course_name):
    #1、获取学校对象中的课程列表，判断当前课程是否在列表中
    school_obj=models.School.select(school_name)
    # print(school_obj)
    # print(school_obj.school_course_list)

    if course_name in school_obj.school_course_list:

        return False,f'该学校已经存在此课程'

    #2、管理员创建课程
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_course(school_name,course_name)

    return True,f'{course_name}-----课程创建成功！'















