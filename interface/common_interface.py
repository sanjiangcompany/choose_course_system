
from db import models
import os
from conf import settings

#公共登录接口
def login_interface(username,password,user_type):   #user_type--> admin
    if user_type == 'admin':
        #查询用户名是否存在
        obj=models.Admin.select(username)

    elif user_type == 'student':

        obj=models.Student.select(username)
    elif user_type == 'teacher':

        obj=models.Teacher.select(username)
    else:

        return False,f'没有权限'

    #判断用户是否存在(admin_obj ,student_obj, teacher_obj)
    if not obj:
        return False,f'用户不存在'
    if obj.pwd == password:
        return  True,f'{username}---登录成功'
    else:
        return False,f'密码错误'


#获取所有学校的接口
# 返回一个列表
def get_school_interface():
    school_path=os.path.join(
        settings.DB_PATH,'School'
    )

    if os.path.exists(school_path):
        school_list=os.listdir(school_path)

        return school_list


#获取所有课程的接口
def get_courses_interface():

    #1、拼接课程文件路径
    course_path=os.path.join(
        settings.DB_PATH,'Course'
    )

    if os.path.exists(course_path):

        return os.listdir(course_path)








