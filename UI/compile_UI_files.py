import os
all_files = os.walk('.')
print(type(all_files))
for root, dirs, files in os.walk('.'):
#    print("root=" + root)
#    print("dirs=" + str(dirs))
#    print("files=" + str(files))
    os.chdir(root)
    for file in files:        
        if file.endswith('.ui'):
            print( str( file ) )
            os.system('pyuic5 -o %s.py %s' % (file.rsplit('.', 1)[0], file))
        elif file.endswith('.qrc'):
            print( str( file ) )
            os.system('pyrcc5 -o %s_rc.py %s' % (file.rsplit('.', 1)[0], file))