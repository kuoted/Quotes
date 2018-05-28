import os
all_files = os.walk('.')
print(type(all_files))

env_dist = os.environ # environ是在os.py中定义的一个dict environ = {}

old_path = env_dist.get('PATH')
env_dist['PATH'] = "C:\\ProgramData\\Anaconda3\\envs\\Quotes\\Scripts;" + old_path
#print(env_dist.get('PATH'))
#print(env_dist['PATH'])

# 打印所有环境变量，遍历字典
'''
for key in env_dist:
    print(key + ' : ' + env_dist[key])
'''
for root, dirs, files in os.walk('./res'):
    '''
    print("root=" + root)
    print("dirs=" + str(dirs))
    print("files=" + str(files))
    '''
    #os.chdir(root)
    for file in files:
        if file.endswith('.ui'):
            print( str( file ) )
            os.system('pyuic5 -o %s.py %s/%s' % (file.rsplit('.', 1)[0], root, file))
        elif file.endswith('.qrc'):
            print( str( file ) )
            os.system('pyrcc5 -o %s_rc.py %s/%s' % (file.rsplit('.', 1)[0], root, file))