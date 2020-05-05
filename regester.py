import easygui as g
import cx_Oracle
import sys
import traceback

def regester(tu):
    ok1=ok2=0
    if(tu is None):
        g.msgbox('谢谢使用！')
        return 1
    elif(''in tu):
        g.msgbox('输入的数据不全')
        return 1
    elif(tu[-1]!=tu[-2]):
        g.msgbox('两次输入的密码不同')
        return 1
    else:
        con = cx_Oracle.connect('root/123456@49.140.125.49/hotel')
        cur = con.cursor()
        names =tu[0]
        ids = str(tu[-3])
        passwards =str(tu[-1])
        judge1 ='select * from user_hotel where id='+ids
        cur.execute(judge1)
        row=cur.fetchone()
        if(row is not None):
            g.msgbox('该账号已被注册过！请重新申请！')
            cur.close()
            con.close()
            return 1
        exc1 ='insert into user_hotel(name,id,passward) values('+"'"+names+"',"+ids+","+passwards+")"
        try:
            cur.execute(exc1)
            ok1=1
        except:
            traceback.print_exc()
            g.msgbox('账号和密码的大小不超过十位！')
            ok1=0
            cur.close()
            con.close()
            return 1
        exc2 ='insert into guest(name,sex,id_card,id,tel) values('+"'"+names+"','"+tu[1]+"',"+str(tu[2])+","+ids+","+str(tu[3])+")"
        try:
            cur.execute(exc2)
            ok2=1
        except:
            traceback.print_exc()
            g.msgbox('性别请填m或者w代表男女\n请填写正确格式的身份证号')
            ok2=0
            cur.close()
            con.close()
            return 1
        if(ok1==ok2==1):
            con.commit()
            g.msgbox('注册成功！！')
            return 0;



