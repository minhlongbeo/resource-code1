from module_mini import *

from tkinter import *
import numpy as nr

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

def tao_widget(giao_dien,  kick_thuoc,  widget_nho,  kieu,  vi_tri,  x_y):
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
    dap_an_bien[0].place(x = x_y[0], y = x_y[-1])
    dap_an_bien[1].place(x = x_y[0] + 40 , y = x_y[-1])

    index_y = x_y[-1] + 50

    dap_an_bien[2].place(x = x_y[1],  y = index_y)
    dap_an_bien[3].place(x = x_y[1] + x_y[2],  y = index_y)
    dap_an_bien[4].place(x = x_y[1] + x_y[2] * 2,  y = index_y)
    dap_an_bien[5].place(x = x_y[1] + x_y[2] * 3,  y = index_y)

    giao_dien.update()

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
            mini.config(command=lambda : mo_to_gui(chu_luu, vi_tri) )

        elif y_mini + height_mini >= kick_thuoc:
            #kéo thêm dòng nếu gần
            
            if y_mini + height_mini - x_y[-2] < kick_thuoc:                
                giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc + x_y[-2]+20}')
                
                print(f'widget là 2{widget_nho}')
                return True
            
    return False
#------------------------------------------------------------------------------------------------------

class system_code:
    def __init__(self, mang, thoi_gian, don_vi, kieu, kick_thuoc):
        
        do_khoang_cach_y = int(kick_thuoc/8.1)
        chua_gui = []
        bien_x_cau_hoi = kick_thuoc/2.6
        chuyen_trang_old = False
        bien_y = 6
        i = 0

        giao_dien = Tk()
        giao_dien.title(f"trang trắc nghiệm {i}")
        giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc}')

        #lặp tạo câu hỏi 
        for vi_tri, phan_con in enumerate(mang):
            chuyen_trang = tao_widget(giao_dien,  kick_thuoc,  phan_con,  kieu,  vi_tri,  [bien_x_cau_hoi, 60,  145,  do_khoang_cach_y,  bien_y])

            bien_y += 125
            
            if chuyen_trang == True:
                print(f'yessssss {vi_tri} và {len(mang)}')

            vi_tri_set = vi_tri + 1 < len(mang)

            if chuyen_trang == True and vi_tri_set == True:
                
                chua_gui.append(giao_dien)
                anh_undo = PhotoImage(file='C:/Users/Minh Long/AppData/Roaming/Txt_file/Icon/view_undo.png')

                anh_next = PhotoImage(file='C:/Users/Minh Long/AppData/Roaming/Txt_file/Icon/view_more.png')
                nut_next = Button(giao_dien, image=anh_next)
                nut_next.place(x = kick_thuoc/1.75,  y = bien_y)

                nut_undo = Button(giao_dien,   image=anh_undo)
                nut_undo.place(x = kick_thuoc/3,  y = bien_y)

                giao_dien = Tk()
                giao_dien.title(f'trang trắc nghiệm {i+2}')
                giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc}')
                giao_dien.withdraw()

                def chuyen_trang(linh_tinh):
                    chua_gui[i].withdraw()
                    giao_dien.deiconify()
                
                nut_next.bind('<Button>',  chuyen_trang)
                
                bien_y = 20
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #chuyển trang
        giao_dien.mainloop()
        
system_code(mang_du_lieu, 0, 'giây', ('Times New Roman', 20), 600)
        
system_code(mang_du_lieu, 0, 'giây', ('Times New Roman', 20), 600)




