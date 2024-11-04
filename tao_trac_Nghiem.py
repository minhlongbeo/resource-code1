import numpy as np
from tkinter import *
from tkinter import ttk

class tao_bien:
    def __init__(self, x1, y1, testv1, testv2):
        self.x = x1
        self.y = y1
        self.cau_hoi = testv1
        self.thoi_gian = testv2
        self.don_vi = ''

    def make_gui(mang_test: list):
        gui2 = Tk()
        gui2.title(mang_test[0])
        gui2.geometry(mang_test[1])
        
        if len(mang_test) > 2:
            gui2.config(bg = mang_test[2])

        return gui2

# Biến
global_font = ('Times New Roman', 20)
bien_1 = tao_bien(5, 82, False, False)

# Chính
gui = Tk()
gui.title('tạo mẫu trắc nghiệm của file')
gui.geometry('370x370')

dai_dien = Label(gui, text='Tạo mẫu trắc nghiệm', font=('Times New Roman', 20))
dai_dien.place(x=60, y=30)

# Các giao diện nhỏ trong gui
text_sign = 'khi nhập sai hoặc nhập nhanh có thể gây ra lỗi !!! cẩn thận khi chọn dữ liệu do nhiều lỗi vẫn chưa được phát hiện '
ghi_chu = Label(gui, text = text_sign, font = global_font, wraplength = 350)
text1_cau_hoi = Label(gui, text = 'số câu hỏi :', font = global_font)
time_text = Label(gui, text = 'thời gian làm bài :', font = global_font)

chon1_cau_hoi = Entry(gui, font = global_font, width = 15)
chon1_time = Entry(gui, font = global_font, width = 5)
chon2_time = ttk.Combobox(gui, font = global_font, value = ['giây', 'phút', 'giờ'], width = 4)

def tao_du_lieu(du_lieu):
    if len(du_lieu) > 1:
        for number in range(1, int(du_lieu[0]) + 1):
        
            mang_so = np.array( ['A', 'B', 'C', 'D'], dtype = str)
            so_y = 93
            name = str(f'nhập câu hỏi thứ {number}')
            gui_test = tao_bien.make_gui(['nhập đáp án cho câu hỏi', '500x500', 'BLUE'])   

            if gui_test is not None:

                chu_cau_hoi = Label(gui_test,  text = name,  font = global_font)
                nhap_cau_hoi = Entry(gui_test,  font = global_font,  width = 33)
                hinh_nut1 = PhotoImage(file = 'C:/Users/Minh Long/Pictures/Button_dark.png')
                hinh_nut2 = PhotoImage(file = 'C:/Users/Minh Long/Pictures/Button_light.png')

                complete = Button(gui_test,  image = hinh_nut1,  width = 100)
                complete.config(borderwidth = 0,  highlightthickness = 0,  bg = 'BLUE',  activebackground = 'BLUE',  text = 'Hoàn thành',  font = global_font)
                complete.place(x = 195, y = 450)

                def doi_anh(su_kien):
                    tong = str(su_kien)

                    if 'Enter' in tong:
                        complete.config(image = hinh_nut2)
                    else:
                        complete.config(image = hinh_nut1)


                for number2 in mang_so:
                    thu_tu = Label(gui_test,  text = 'nhập đáp án câu ' + number2,  font = global_font).place(x = 11, y = so_y)
                    tao_cau_hoi = Entry(gui_test,  font = global_font,  width = 33).place(x = 10, y = so_y + 40)

                    so_y += 93

                nhap_cau_hoi.place(x = 10, y = 40)
                chu_cau_hoi.pack()
                complete.bind('<Enter>',  doi_anh)
                complete.bind('<Leave>',  doi_anh)
                gui_test.mainloop()


def kiem_tra_so(value):
    for v in value:
        if v.isdigit():
            if value[0] == v:
                bien_1.cau_hoi = True
            elif value[1] == v:
                bien_1.thoi_gian = True
            elif value[2] == v:
                bien_1.don_vi = v
        else:
            gui2 = tao_bien.make_gui(['lỗi', '180x100'])
            if value[0] == v and value[1] == v:
                Label(gui2, font=global_font, text='nhập lại số \n câu hỏi, thời \n gian làm bài').pack()
                break
            elif value[0] == v:
                Label(gui2, font=global_font, text='nhập lại \n số câu hỏi').pack()
                break
            elif value[1] == v:
                Label(gui2, font=global_font, text='nhập lại thời \n gian làm bài').pack()
                break
            elif value[2] == v:
                if v.isalpha():
                    gui2.destroy()
                    gui.destroy()
                    tao_du_lieu( np.array(value, dtype=str) )
                else:
                    Label(gui2, font=global_font, text='chọn đơn \n vị thời gian').pack()
                break

nut_cuoi = Button(gui, text='Xong', font=global_font, width=8, height=1, command=lambda: kiem_tra_so([chon1_cau_hoi.get(), chon1_time.get(), chon2_time.get()]))

nut_cuoi.place(x=bien_1.x + 100, y=bien_1.y + 210)
text1_cau_hoi.place(x=bien_1.x, y=bien_1.y)
chon1_cau_hoi.place(x=bien_1.x * 28, y=bien_1.y)
time_text.place(x=bien_1.x, y=bien_1.y + 38)
ghi_chu.place(x=20, y=150)

chon1_time.place(x=bien_1.x * 42, y=bien_1.y + 40)
chon2_time.place(x=bien_1.x * 58, y=bien_1.y + 40)

gui.mainloop()
