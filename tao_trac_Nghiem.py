import numpy as np
from tkinter import *                                    #dùng tkinter 
from tkinter import ttk                                #dùng combobox
from PIL import Image, ImageTk                          #dùng image

class tao_bien:
    def __init__(self, x1, y1, testv1, testv2):
        self.x = x1
        self.y = y1
        self.cau_hoi = testv1
        self.thoi_gian = testv2
        self.don_vi = ''

    def make_gui(name, size):
        gui2 = Tk()
        gui2.title(name)
        gui2.geometry(size)

        return gui2

#biến
global_font = ('Times New Roman', 20)
bien_1 = tao_bien(5, 82, False, False)

#chính
gui = Tk()
gui.title('tạo mẫu trắc nghiệm của file')
gui.geometry('370x370')

dai_dien = Label(gui, text = 'Tạo mẫu trắc nghiệm', font = ('Times New Roman', 20))
dai_dien.place(x = 60, y = 30)

#các giao diện nhỏ trong gui

#1
text_sign = 'khi nhập sai hoặc nhập nhanh có thể gây ra lỗi !!! cẩn thận khi chọn dữ liệu do nhiều lỗi vẫn chưa được phát hiện '

ghi_chu = Label(gui,  text = text_sign,  font = global_font,  wraplength = 350)
text1_cau_hoi = Label(gui, text = 'số câu hỏi :', font = global_font)
time_text = Label(gui, text = 'thời gian làm bài :', font = global_font)

chon1_cau_hoi = Entry(gui,  font = global_font,  width = 15)
chon1_time = Entry(gui,  font = global_font,  width = 5)
chon2_time = ttk.Combobox(gui,  font = global_font,  value = ['giây', 'phút', 'giờ'],  width = 4)


def tao_du_lieu(du_lieu):
    if len(du_lieu) > 1:
        for number in range(1, int(du_lieu[0]) + 1):
            name = str(f'nhập đáp án cho câu hỏi thứ {number}')
            print(name)
            gui_test = bien_1.make_gui(name, '350x350')
    else:
        print('nooooooooooooooooooooooooooooooooooooooooooooo')


def kiem_tra_so(value):
    for v in value:

        match (v.isdigit()):
            case (True):
                if value[0] == v: bien_1.cau_hoi = True
                elif value[1] == v: bien_1.thoi_gian = True
                elif value[2] == v: bien_1.don_vi = v

            case (False):
                gui2 = tao_bien.make_gui('Lỗi', '180x100')

                if value[0] == v and value[1] == v:
                    Label(gui2, font = global_font, text = 'nhập lại số \n câu hỏi, thời \n gian làm bài').pack()
                    break
                elif value[0] == v: 
                    Label(gui2, font = global_font, text = 'nhập lại \n số câu hỏi').pack()
                    break
                elif value[1] == v: 
                    Label(gui2, font = global_font, text = 'nhập lại thời \n gian làm bài').pack()
                    break
                elif value[2] == v:
                    if value[2].isalpha() == True :
                        gui2.destroy()
                        gui.destroy()
                        tao_du_lieu(np.array(value, dtype = str))

                    else: Label(gui2, font = global_font, text = 'chọn đơn \n vị thời gian').pack()
                    break
                

nut_cuoi = Button(gui,  text = 'Xong',  font = global_font,  width = 8,  height = 1,  command = lambda : kiem_tra_so([chon1_cau_hoi.get(), chon1_time.get(), chon2_time.get()]))

#chạy task 1
text1_cau_hoi.place(x = bien_1.x, y = bien_1.y)
chon1_cau_hoi.place(x = bien_1.x * 28, y = bien_1.y)
time_text.place(x = bien_1.x, y = bien_1.y + 38)

chon1_time.place(x = bien_1.x * 42, y = bien_1.y + 40)
chon2_time.place(x = bien_1.x * 58, y = bien_1.y + 40)
ghi_chu.place(x = bien_1.x,  y = bien_1.y + 80)

nut_cuoi.place(x = bien_1.x + 100, y = bien_1.y + 210)
#end task 1

gui.mainloop()