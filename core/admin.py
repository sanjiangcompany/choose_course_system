
#管理员视图层
from interface import common_interface
from interface import admin_interface
from lib import common


admin_info={
    'user':None
}
#注册
def register():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        re_password=input('请输入确认密码：').strip()

        if password == re_password:
            flag,msg=admin_interface.register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('两次密码不一致')


#登录
def login():
    while True:
        username=input('请输入用户名：').strip()
        password=input('请输入密码：').strip()
        flag,msg=common_interface.login_interface(username,password,user_type='admin')
        if flag:
            print(msg)
            admin_info['user']=username
            break
        else:
            print(msg)



#创建学校
#加登录装饰器
@common.login_auth('admin')

def create_school():
    while True:
        #学校名和学校地址
        school_name=input('请输入学校名：').strip()
        school_addr=input('请输入学校地址：').strip()
        flag,msg=admin_interface.create_school_interface(
            admin_info.get('user'),school_name,school_addr)

        if flag:
            print(msg)
            break
        else:
            print(msg)


#创建老师
@common.login_auth('admin')
def create_teacher():
    while True:
        teacher_name=input('请输入老师姓名：').strip()
        flag,msg=admin_interface.create_teacher_interface(
            admin_info.get('user'),teacher_name
        )
        if flag:
            print(msg)
            break

        else:
            print(msg)


#创建课程
@common.login_auth('admin')
def create_course():
    while True:
        #1、获取所有的学校
        school_list=common_interface.get_school_interface()
        if not school_list:
            print('没有这个学校，请去创建！')
            break

        for index,school in enumerate(school_list):
            print(index,school)

        #2、选择学校
        choice=input('请选择学校编号：').strip()

        if not choice.isdigit():
            print('请输入数字：')
            continue

        choice=int(choice)

        if choice not  in range(len(school_list)):
            print('输入有误！')
            continue
        #3、添加课程给学校
        #获取学校名字
        school_name=school_list[choice]
        course_name=input('请输入课程名称：').strip()

        flag,msg=admin_interface.create_course_interface(
            admin_info.get('user'),school_name,course_name
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)



func_dic={
    '1':register,
    '2':login,
    '3':create_school,
    '4':create_teacher,
    '5':create_course

}

#管理员视图
def admin_view():
    while True:
        print("""
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程
        q、退出
        
        """)

        choice=input('请选择管理员功能：q 退出').strip()

        if choice=='q':
            break

        if choice not in func_dic:
            print('选择有误')
            continue
        func_dic.get(choice)()














