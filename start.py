import easygui as g
import cx_Oracle
import sys
import regester
import newboss
import suppot
import guest
import qiantai



title = 'welcome'
msg = '立天大酒店自助服务程序'
choices = ['用户登录','用户注册']
con =cx_Oracle.connect('root/123456@49.140.125.49/hotel')
def main():
    while 1:
        answer=g.choicebox(msg,title,choices)
        if(answer is None):
            g.msgbox("欢迎下次使用")
            break
        if(answer=="用户登录"):
            a = g.multpasswordbox(msg,'用户登录界面',('账号','密码'))
            if(a is None):
                g.msgbox('再见！',title,'退出')
                sys.exit(0)
            pn=str(a[0])
            pa=str(a[-1])
            cur=con.cursor()
            exc='select * from user_hotel where id='+ pn +' and passward=' + pa
            cur.execute(exc)
            row =cur.fetchone()
            if(row is None):
                g.msgbox("登录失败，未注册")
            else:
                level =row[-1]
                print(row[-1])
                if(row[-1]=='s'):#老板界面
                    newboss.boss()
                    break
                if(row[-1]=='0'):#顾客界面
                    exc2="select vip_class from guest where id="+pn
                    cur.execute(exc2)
                    row2=cur.fetchone()
                    guest.guest(int(row2[0]),int(pn))
                    break
                if(row[-1]=='1'):#前台界面
                    qiantai.qiantai(pn)
                    break
                if(row[-1]=='2'):#后勤界面
                    suppot.support()
                    break
                if(row[-1]=='9'):
                    g.msgbox("普通员工你好，你的等级还不需要使用该系统")
                    break
                if(row[-1]=='8'):
                    g.msgbox("尊敬的经理你好,你的等级已经不再需要使用该系统，你直接吩咐就行~~~")

                cur.close()
                con.close()
         
        elif(answer=="用户注册"):
            b = g.multenterbox(msg,'用户注册界面',('姓名','性别','身份证号','电话','申请账号','输入密码','确认密码'))
            a=1
            while(regester.regester(b)):
                g.msgbox('输入的数据有误请核对后重新输入')
                b = g.multenterbox(msg,'用户注册界面',('姓名','性别','身份证号','电话','申请账号','输入密码','确认密码'))
                a=a+1
                if(a==3):
                    g.msgbox('输入次数过多自动退出！')
                    break

    

main()
