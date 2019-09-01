
from interface import common_interface
from lib import  common
from interface import teacher_interface

teacher_info={
    'user':None
}


#登录
def login():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        flag,msg=common_interface.login_interface(username,password,user_type='teacher')
        if flag:
            teacher_info['user']=username
            print(msg)
            break
        else:
            print(msg)


#查看老师自己教授的课程
@common.login_auth('teacher')
def check_course():
    flag,teacher_course_list_msg=teacher_interface.check_course_interface(
        teacher_info.get('user')
    )

    if flag:
        print(teacher_course_list_msg)
    else:
        print(teacher_course_list_msg)


#老师选择自己教授的课程
@common.login_auth('teacher')
def choose_course():
    while True:
        #1、查看所有课程
        course_list=common_interface.get_courses_interface()

        if not course_list:
            print('没有该课程')
            break

        #2、打印所有课程，并选择课程
        for index,course in enumerate(course_list):
            print(index,course)

        choice = input('请输入课程编号：').strip()

        if not choice.isdigit():
            print('必须是数字')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('请选择正确的编号！')
            continue

        course_name=course_list[choice]

        flag,msg=teacher_interface.choose_course_interface(teacher_info.get('user'),course_name)

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


#查看课程下的学生
@common.login_auth('teacher')
def check_student():
    while True:
        #1、获取老师下的所有课程
        flag,course_list_or_msg=teacher_interface.check_course_interface(
            teacher_info.get('user')
        )

        if not flag:
            print('没有课程')
            break

        for index,course in enumerate(course_list_or_msg):
            print(index,course)

        choice = input('请输入课程编号：').strip()

        if not choice.isdigit():
            continue
        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            continue

        course_name=course_list_or_msg[choice]
        #调用查看课程下的学生接口
        flag,msg=teacher_interface.check_student_interface(
            teacher_info.get('user'),course_name
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


#修改课程下的学生成绩
@common.login_auth('teacher')
def change_score():
    while True:
        #1、获取当前老师下的所有课程
        flag,teacher_course_list=teacher_interface.check_course_interface(
            teacher_info.get('user')
        )

        if not flag:
            print('该老师下没有课程！')
            break
        #有课程的老师，循环打印老师的课程列表
        for index,course in enumerate(teacher_course_list):
            print(index,course)

        choice = input('请选择课程编号：').strip()

        if not choice.isdigit():
            continue

        choice=int(choice)
        if choice not in range(len(teacher_course_list)):
            continue

        course_name = teacher_course_list[choice]
        #查看老师对应课程下的学生情况
        flag,student_list=teacher_interface.check_student_interface(
            teacher_info.get('user'),course_name
        )

        if not flag:
            print('没有学生')
            break
        #如果有学生，则循环打印学生列表，让老师选择学生
        for index,student_name in enumerate(student_list):
            print(index,student_name)

        #老师选择学生编号
        choice2=input('请选择学生编号：').strip()
        if not choice2.isdigit():
            continue

        choice2 =int(choice2)

        if choice2 not  in range(len(student_list)):
            continue

        student_name = student_list[choice2]

        #请输入修改学生的成绩
        score=input('请输入修改的成绩：').strip()

        flag,msg=teacher_interface.change_score_interface(
            teacher_info.get('user'),course_name,student_name,score
        )

        if flag:
            print(msg)
            break




func_dic={
    '1':login,
    '2':choose_course,
    '3':check_course,
    '4':check_student,
    '5':change_score,

}

#老师视图
def teacher_view():
    while True:
        print("""
        1、登录
        2、老师选择教授的课程
        3、查看老师教授的课程
        4、查看课程下的学生
        5、修改课程下的学生成绩
        q、退出
        """)
        choice=input('请选择老师功能：q 退出').strip()

        if choice=='q':
            break

        if choice not in func_dic:
            print('选择有误')
            continue
        func_dic.get(choice)()






