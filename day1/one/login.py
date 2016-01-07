#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_count = 0
# 循环次数起始值。
while True:
    AA = 0
    # 给下面判断用户输入的用户名是否存在做准备。
    input_username = input("请输入您的用户名：").strip()
    # 获取用户输入用户名并脱去空格。
    file_info = open("user_info.txt", "r")
    lock_file = open("lock.txt", "r+")
    # 打开用户名信息表与账号锁定表。
    if input_username == "":
        print("请输入正确信息。")
    else:
        for i in file_info.readlines():
            if input_username in i:
                # 判断输入的用户名是否在用户文件列表内（user_info.txt）。
                if input_username not in lock_file.read():
                    # 判断输入的用户名是否在锁定文件内（lock.txt）。
                    AA = 1
                    # 给下面判断用户输入的用户名是否存在做准备。
                    while input_count < 3:
                        # 判断循环次数。
                        input_password = input("请输入您的密码：").strip()
                        password_info = i.split(",")[1].strip("\n")
                        # 在用户名列表文件内取用户名与密码并进行处理。
                        if input_password == "":
                            print("请不要输入空密码。")
                        else:
                            if input_password == password_info:
                                # 判断输入的密码是否与用户信息列表内的相同。
                                print("登录成功。")
                                exit()
                            else:
                                print("密码错误。")
                            # 此循环是当用户连续三次输入错误密码，将会所用户名添加到lock.txt文件内。
                            input_count += 1
                            # 每输错一次密码input_count变量会加1。
                    lock_file.write(input_username + "\n")
                    # 将输错用户名的账号写入到锁定文件列表。
                    lock_file.close()
                    # 关闭文件。
                    print("输入三次错误密码账号被锁定.....")
                    exit()
                else:
                    print("此用户名已经锁定,请输入其他用户名.......")
                    AA = 1
                    # 给下面判断用户输入的用户名是否存在做准备。
                    break
            else:
                AA = 0
                # 给下面判断用户输入的用户名是否存在做准备。
        file_info.close()
        if AA == 0:
            print("此用户名不存在，请输入正确用户名.")
            # 用户输入的用户名是否存在，如果不存在打印信息。

