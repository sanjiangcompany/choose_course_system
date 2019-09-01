
import  pickle
import os
from conf import settings



#用户保存
def db_save(obj):
    #Admin
    class_name=obj.__class__.__name__
    #获取保存文件目录
    dir_path=os.path.join(
        settings.DB_PATH,class_name
    )
    #判断文件夹是否存在，不存在则创建
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    #拼接pickle文件路径
    user_path=os.path.join(
        dir_path,obj.name
    )
    with open(user_path,'wb')as f:
        pickle.dump(obj,f)
        f.flush()




#用户查询
def db_select(cls,username):
    # 1、获取当前用户文件夹
    class_name=cls.__name__
    #获取保存文件夹目录
    dir_path=os.path.join(
        settings.DB_PATH,class_name
    )
    #判断文件夹是否存在
    if os.path.isdir(dir_path):
        user_path=os.path.join(
            dir_path,username
        )
        #判断文件是否存在
        if os.path.exists(user_path):
            #把对洗那个从pickle文件中读出来，如果不存在，则返回none
            with open(user_path,'rb')as f:

                obj=pickle.load(f)

                return obj
















