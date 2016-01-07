#!/usr/bin/env python3
# -*- coding: utf-8 -*-
first_list = {"1": "东北地区",
              "2": "华北地区",
              "3": "华东地区",
              "4": "华中地区"
              }
# 第一级区域级字点。
second_list = {"东北地区": {
                     "1": "吉林省",
                     "2": "辽宁省",
                     "3": "黑龙江省",
                                },
            "华北地区": {
                     "1": "北京市",
                     "2": "天津市",
                     "3": "河北省",
                     "4": "山西省",
                                },
            "华东地区": {
                     "1": "上海市",
                     "2": "江苏省",
                     "3": "浙江省",
                     "4": "安徽省",
                                },
            "华中地区": {
                     "1":"河南省",
                     "2":"湖北省",
                     "3":"湖南省",
                            }
                }
# 第二级省级字典。
end_list = {"吉林省": ['长春市', '吉林市', '辽源市', '通化市'],
            "辽宁省": ["铁岭市", "阜新市", "朝阳市", "沈阳市"],
            "黑龙江省": ['哈尔滨市', '齐齐哈尔市'],
            "北京市": ['东城区', '西城区', '崇文区', '宣武区', '朝阳区', '海淀区'],
            "天津市": ['和平区', '河东区', '河西区', '南开区', '河北区', '红桥区'],
            "河北省": ['石家庄市', '秦皇岛市'],
            "山西省": ['太原市', '大同市'],
            "上海市": ["浦东新区", "长宁区", "宝山区", "青浦区"],
            "江苏省": ['南京市', '徐州市'],
            "浙江省": ['杭州市', '宁波市'],
            "安徽省": ['合肥市', '淮南市'],
            "河南省": ['郑州市', '洛阳市'],
            "湖北省": ['武汉市', '荆门市'],
            "湖南省": ['长沙市', '株洲市'],
                     }
# 第三级市级字典。
while True:
    for k, v in first_list.items():
        print("%s:%s" % (k, v))
        # 取出并打印区域信息与序号。
    print("退出请输入:exit.")
    first_input_info = input("请输入地区序列编号:").strip()
    if first_input_info == "exit":
        print("谢谢您的访问,再见。")
        break
    # 判断用户输入信息并做处理。
    elif first_input_info == "":
        print("请输入正确序号。")
        continue
        # 当用户输入空信息时，打印提示信息，弄做返回处理。
    else:
        province_list = first_list[first_input_info]
        # 根据输入信息取出省级列表。
        print(province_list)
        for k, v in second_list[province_list].items():
            print("--%s:%s" % (k, v))
            # 遍历省级字典打印省级信息。
        print("反回上一级请输入:b,退出请输入:exit.")
        second_input_info = input("请输入地区序列编号:").strip()
        if second_input_info == "exit":
            # 判断用户输入信息。
            print("谢谢您的访问,再见。")
            break
        elif second_input_info == "b":
            continue
            # 用户输入b时返回到上一级。
        elif second_input_info == "":
            print("请输入正确序号。")
            continue
            # 当用户输入空信息时，打印提示信息，弄做返回处理。
        else:
            city_list = second_list[province_list][second_input_info]
            # 取出省级信息，根据省级信息与输入信息取出相对应的市级列表。
            print(province_list)
            print("--%s" %city_list)
            for k in end_list[city_list]:
                print("----%s" %k)
                # 便利市级字典，并打印信息。
        exit()
