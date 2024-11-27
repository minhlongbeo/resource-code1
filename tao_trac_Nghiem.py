import numpy as nr
from tkinter import *
from text_config import *

mang_du_lieu = nr.array([ 
    {
        'question1' : '1 + 1 = ?',  'awer1' : '2',  'awer2' : '3',  'awer3' : '4',  'awer4' : '5',  'answer' : '1'
    },

    {
        'question2' : '5 + 5 = ?',  'awer1' : '4',  'awer2' : '6',  'awer3' : '10',  'awer4' : '14',  'answer' : '3'
    },

    {
        'question3' : '5 + 7 = ?',  'awer1' : '3',  'awer2' : '65646755406',  'awer3' : '8',  'awer4' : '12',  'answer' : '4'
    },

    {
        'question4' : '10 + 10 = ?', 'awer1' : '4',  'awer2' : '10',  'awer3' : '15',  'awer4' : '20',  'answer' : '4'
    },

    {
        'question5' : '155 + 155 = ?',  'awer1' : '10',  'awer2' : '500',  'awer3' : '310',  'awer4' : '305',  'answer' : '3'
    },

    {
        'question6' : '5 x 5 = ?',  'awer1' : '4',  'awer2' : '6',  'awer3' : '10',  'awer4' : '25',  'answer' : '4'
    },

    {
        'question7' : '9 + 7 = ?',  'awer1' : '10',  'awer2' : '26',  'awer3' : '38',  'awer4' : '16',  'answer' : '4'
    },

    {
        'question8' : '10 x 10 = ?', 'awer1' : '100',  'awer2' : '20',  'awer3' : '5',  'awer4' : '27',  'answer' : '1'
    },

    {
        'question9' : '125 + 125 = ?',  'awer1' : '100',  'awer2' : '500',  'awer3' : '150',  'awer4' : '305',  'answer' : '3'
    },

    {
        'question10' : '1 + 7 = ?',  'awer1' : '10',  'awer2' : '20',  'awer3' : '13',  'awer4' : '8',  'answer' : '4'
    }

    ], dtype = dict )

def tao_widget(giao_dien,  kick_thuoc,  widget_nho,  kieu,  vi_tri,  x1,  x2,  x3, y_s, y_x):
    chu_cau_hoi = widget_nho[ 'question' + str(vi_tri+1) ]

    #tạo label
    dap_an_bien = nr.array([
    Label(giao_dien,  text=f'{vi_tri+1} |',  font=kieu),
    Label(giao_dien,  text=chu_cau_hoi,  font = kieu),
    Button(giao_dien,  text=widget_nho['awer1'],  font=kieu),
    Button(giao_dien,  text=widget_nho['awer2'],  font=kieu),
    Button(giao_dien,  text=widget_nho['awer3'],  font=kieu),
     Button(giao_dien,  text=widget_nho['awer4'],  font=kieu)
    ], dtype=object)

    #place
    dap_an_bien[0].place(x = x1, y = y_x)
    dap_an_bien[1].place(x = x1 + 40 , y = y_x)

    index_y = y_x + 50

    dap_an_bien[2].place(x = x2,  y = index_y)
    dap_an_bien[3].place(x = x2 +x3,  y = index_y)
    dap_an_bien[4].place(x = x2 + x3 * 2,  y = index_y)
    dap_an_bien[5].place(x = x2 + x3 * 3,  y = index_y)

    giao_dien.update()

    #tạo gui hiển thị nhỏ
    def tao_gui_hien_thi(textz):
        gui_new = Tk()
        gui_new.title(f'câu hỏi thứ {vi_tri}')
        chu = Label(gui_new,  text=textz,  font=kieu)
        chu.pack()
        chu.update()
        gui_new.geometry(f'{chu.winfo_width() + 70}x{chu.winfo_height() + 20}')

    #kiểm tra độ dài
    for v in range(0, len(dap_an_bien)-1):
        mini = dap_an_bien[v]
        x_mini = mini.winfo_x()
        y_mini = mini.winfo_y()
        with_mini = mini.winfo_width()
        height_mini = mini.winfo_height()

        if v >= 2 and x_mini + with_mini >= dap_an_bien[v+1].winfo_x():
            chu_luu = mini.cget('text')
            mini.config(text='...')
            mini.config(command=lambda : tao_gui_hien_thi(chu_luu) )

        elif y_mini + height_mini >= kick_thuoc:
            #kéo thêm dòng nếu gần
            if y_mini + height_mini - y_s < kick_thuoc:
                giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc + y_s}')
                return True
                
    return False
#------------------------------------------------------------------------------------------------------

class system_code:
    def __init__(self, mang, thoi_gian, don_vi, kieu, kick_thuoc):
        do_khoang_cach_y = int(kick_thuoc/8.3)
        bien_x_cau_hoi = kick_thuoc/2.6
        chuyen_trang_old = False
        chua_gui = nr.array([], dtype=object)
        khoang_cach_x = 145
        bien_x_dap_an = 60
        bien_y = 20
        i = 1

        giao_dien = Tk()
        giao_dien.title(f"trang trắc nghiệm {i}")
        giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc}')

        #lặp tạo câu hỏi 
        for vi_tri, phan_con in enumerate(mang):
            chuyen_trang = tao_widget(giao_dien,  kick_thuoc,  phan_con,  kieu,  vi_tri,  bien_x_cau_hoi,   bien_x_dap_an,  khoang_cach_x,  do_khoang_cach_y,  bien_y)

            bien_y += 125

            if chuyen_trang == True and vi_tri + 1 < len(mang):
                chua_gui = nr.append(chua_gui, giao_dien)

                giao_dien = Tk()
                giao_dien.title(f'trang trắc nghiệm {i+1}')
                giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc}')

                bien_y = 20

        giao_dien.mainloop()
system_code(mang_du_lieu, 0, 'giây', ('Times New Roman', 20), 600)


