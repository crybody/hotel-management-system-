import cx_Oracle
import easygui as g
#import chaxun2
#import reserve
#import guest
def qiantai(id):
    while 1:
        con = cx_Oracle.connect('root/123456@49.140.125.49/hotel')
        cursor = cur = con.cursor()
        msg = '前台'+ str(id) + '号，你已登录酒店，你可选择以下功能'
        title = "前台登录页面"
        choice0 = ['为客人服务','查询住房信息','查询房间价格']
        answer0 = g.choicebox(msg,title,choice0)
#出口------------------------------------------------------------------------------------------------------------------------------------------------#
        if(answer0 is None):
            g.msgbox("你选则了退出")
            break
#为客人服务------------------------------------------------------------------------------------------------------------------------------------------#
        if(answer0 == "为客人服务"):
            while 1:
                answer1 = g.enterbox("请输入客人的id")
                if(answer1 is None):
                    g.msgbox("退出")
                    break
                exc1 = "select vip_class from guest where id =" + answer1
                cur.execute(exc1)
                row1 = cur.fetchone()
                if(row1 is None):
                    g.msgbox("没有该用户")
                    break
                else:
                    vip=row1[0]
                    
                cur.close()
                con.close()
                pass
                break
#查询房间价格------------------------------------------------------------------------------------------------------------------------------------------#
        if(answer0 =="查询房间价格"):
            while 1:
                pass
                break
#查询住房信息------------------------------------------------------------------------------------------------------------------------------------------#
        if(answer0 =="查询住房信息"):
            while 1:
                msg2='选择以下功能'
                title2 = '查询住房信息'
                choice2 = ['根据姓名查询客人详细信息','根据ID查询客人详细信息', '根据客人ID查询其入住房间','根据房间号查询入住客人',]
                answer2 = g.choicebox(msg, title, choice2)
                #-------------------------------------------------------
                if(answer2 is None):
                    g.msgbox('你选择了退出')
                    break
                #-------------------------------------------------------
                if(answer2 == '根据姓名查询客人详细信息'):
                    while 1:
                        name = ''
                        back=0
                        while 1:
                            name = g.enterbox(msg='请输入客人姓名', title='根据姓名查询客人详细信息')
                            name = "'"+ name + "'"
                            pass
                            break
                #---------------------------------------------------------
                if(answer2 =='根据ID查询客人详细信息'):
                    while 1:
                        id=''
                        back=0
                        while 1:
                            id = g.enterbox(msg='请输入客人ID', title='根据ID查询客人详细信息')
                            pass
                            break
                #--------------------------------------------------------
                if(answer2 =='根据客人ID查询其入住房间'):
                    while 1:
                        answer2_3=g.enterbox("请输入客人的id")
                        if(answer2_3 is None):
                            g.msgbox("退出")
                            break
                        exc1="select * from guest where id ="+answer2_3
                        cur.execute(exc1)
                        row1=cur.fetchone()
                        if(row1 is None):
                            g.msgbox("没有该用户")
                            break
                        text='该用户的具体订单\n'
                        exc2="select * from history where user_id ="+answer2_3
                        cur.execute(exc2)
                        row2=cur.fetchall()
                        for row in row2:
                            text=text+"房间号 "+str(row[1])+"订单起始时间"+str(row[2])[0:-9]+"订单结束时间"+str(row[-2])[0:-9]+"\n"
                        g.msgbox(text)
                        break
                #---------------------------------------------------------
                if(answer2 =="根据房间号查询入住客人"):
                    while 1:
                        answer2_4=g.enterbox("请输入房间号")
                        if(answer2_4 is None):
                            g.msgbox("退出")
                            break
                        exc1="select * from room where id ="+answer2_4
                        cur.execute(exc1)
                        row1=cur.fetchone()
                        if(row1 is None):
                            g.msgbox("没有该房间")
                            break
                        text="该房间的入住情况如下\n"
                        exc2="select * from history where room_id ="+answer2_4
                        cur.execute(exc2)
                        row2=cur.fetchall()
                        for row in row2:
                            if(row[-1]==0):
                                text=text+"客人编号"+str(row[0])+"在"+str(row[2])[0:-9]+"到"+str(row[-2])[0:-9]+"入住"
                        g.msgbox(text)
                        break
