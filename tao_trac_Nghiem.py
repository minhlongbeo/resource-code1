import numpy as nr
from tkinter import *

mang_du_lieu = nr.array([ 
    {
        'question1' : '1 + 1 = ?',  'awer1' : '2',  'awer2' : '3',  'awer3' : '4',  'awer4' : '5',  'answer' : '1'
    },
    {
        'question2' : '5 + 5 = ?',  'awer1' : '4',  'awer2' : '6',  'awer3' : '10',  'awer4' : '14',  'answer' : '3'
    },
    {
        'question3' : '5 + 7 = ?',  'awer1' : '3',  'awer2' : '6',  'awer3' : '8',  'awer4' : '12',  'answer' : '4'
    },
    {
        'question4' : '10 + 10 = ?', 'awer1' : '4',  'awer2' : '10',  'awer3' : '15',  'awer4' : '20',  'answer' : '4'
    },
    {
        'question5' : '155 + 155 = ?',  'awer1' : '10',  'awer2' : '500',  'awer3' : '310',  'awer4' : '305',  'answer' : '3'
    }
], dtype=dict)


def tao_data_output(data, thoi_gian, don_vi, kieu):
    #biến
    kick_thuoc = 600
    guiz = Tk()
    guiz.title("Bảng Kết Quả")
    so_chieu = data.shape[0]
    guiz.geometry(str(kick_thuoc) + 'x' + str(kick_thuoc))

    mang_lon = nr.empty( (so_chieu, 6), dtype=object )

    # Vòng lặp tạo các phần và tạo label
    for so, du_lieu_nho in enumerate(data):
        so_thu_tu = Label(guiz, text= ( str(so) + '|' ), font=kieu)
        so_cau_hoi = Label(guiz, text= du_lieu_nho['question' + str(so+1)], font=kieu )
        
        mang_lon[so, 0] = so_thu_tu
        mang_lon[so, 1] = so_cau_hoi

        # Lặp qua các đáp án
        for i in range(1, 5):
            dap_an = Button(guiz, text=du_lieu_nho['awer' + str(i)], font=kieu)
            dap_an.pack()

            mang_lon[so, i+1] = dap_an

        so_thu_tu.pack()
        so_cau_hoi.pack()

    guiz.update()
    print('Dữ liệu đầu ra:')
    print(mang_lon)


tao_data_output(mang_du_lieu, 0, 'giây', ('Times New Roman', 20) )
