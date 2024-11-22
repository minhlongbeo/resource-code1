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


class system_code:
    def __init__(self, mang, thoi_gian, don_vi, kieu, kick_thuoc):

        bien_x_dap_an = 6
        bien_y = 20
        dem = 0

        giao_dien = Tk()
        giao_dien.title("trắc nghiệm")
        giao_dien.geometry(f'{kick_thuoc}x{kick_thuoc}')

        for vi_tri, widget_nho in enumerate(mang):

            chu_cau_hoi = widget_nho[ 'question' + str(vi_tri+1) ]

            #kiểm tra 1
            if len(chu_cau_hoi) > 10:
                textz = ''
                st = 0

                #xử lí text
                for e in chu_cau_hoi:
                    if st!=kick_thuoc:       textz+=e
                    elif st==kick_thuoc:    textz+=(e + '\n');   st=0

                    st+=1
                
                chu_cau_hoi = textz


            #kiểm tra 1

            cau_hoi = Label(giao_dien,  text=chu_cau_hoi, font = kieu)

            cau_hoi.place(x = 6, y = bien_y)

            bien_y += 100


        giao_dien.mainloop()



system_code(mang_du_lieu, 0, 'giây', ('Times New Roman', 20), 600)


