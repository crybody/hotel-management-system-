import cx_Oracle
import easygui as g
import datetime

def look_stock():
    con=cx_Oracle.connect('root/123456@49.140.125.49/hotel')
    cur=con.cursor()
    exc1='select * from stock'
    cur.execute(exc1)
    rows=cur.fetchall()
    text=''
    for row in rows:
        text=text+'物品'+str(row[0])+'数量为'+str(row[-1])+'\n'
    g.msgbox(text,'立天大酒店')
    return text
    
def support():
    msg='欢迎你后勤人员'
    title='立天大酒店'
    choice0=['添加物品','消耗物品','查看物品储备情况']
    Tnow=datetime.datetime.now().strftime("%Y-%m-%d")##timenow::2017-12-19 21:15:56.898989    
    while 1:
        answer0=g.choicebox(msg,title,choice0)
        if(answer0 is None):
            g.msgbox('你选择了退出')
            break
        if(answer0=='查看物品储备情况'):
            while 1:
                look_stock()
                break
        if(answer0=='消耗物品'):
            while 1:
                #链接
                con=cx_Oracle.connect('root/123456@49.140.125.49/hotel')
                cur=con.cursor()
                ans=look_stock()
                rows=cur.execute("select * from stock").fetchall()
                #获得原先的值
                choice=[]
                old_amount=[]
                for row in rows:
                    choice.append(row[0])
                    old_amount.append(row[-1])
                #获得数量
                long=len(choice)
                b=g.multenterbox('物品消耗多少',msg,choice)
                for i in range(0,len(choice)):
                    new_amount=old_amount[i]-int(b[i])
                    if(new_amount<0):
                        g.msgbox('输入数据有误')
                        break
                    else:
                        exc='update stock set amount='+str(new_amount)+' where type='+"'"+str(choice[i])+"'"
                        cur.execute(exc)
                con.commit()
                g.msgbox("修改成功")
                cur.close()
                con.close()
                break
        if(answer0=='添加物品'):
            while 1:
                #链接
                con=cx_Oracle.connect('root/123456@49.140.125.49/hotel')
                cur=con.cursor()
                exc1="select type from stock "
                cur.execute(exc1)
                row1=cur.fetchall()
                msg2="请选择对下面的哪种物品进行添加"
                choice2=[]
                for row in row1:
                    choice2.append(row[0])
                    
                #生成对话框
                answer2=g.choicebox(msg2,title,choice2)#answer2为物品的种类
                if(answer2 is None):
                    g.msgbox("正在退出")
                    break

                #生成进阶对话框
                answer3=g.enterbox("请输入进货数量",title)#answer3为进货数量
                
                if(answer3 is None):
                    break
                amount=int(answer3)

                #查找进货价格
                exc2="select rate from price where type="+"'"+answer2+"'"
                cur.execute(exc2)
                row2=cur.fetchone()
                money=int(row2[0])#进货价格

                #--------------------------------------写入数据库------------------------------------------------
                ok1=0
                ok2=0

                #判断当天是否产生流水,没有则生成今天记录,引用自上方预订
                exc1_2="select * from flow where time_now =to_date('"+Tnow+"','yyyy-mm-dd')"
                cur.execute(exc1_2)
                row1_1=cur.fetchone()
                if(row1_1 is None):
                    exc1_3="insert into flow(time_now) values(to_date('"+Tnow+"','yyyy-mm-dd'))"
                    try:
                        cur.execute(exc1_3)
                    except:
                        g.msgbox("插入新数据flow出错")
                    con.commit()
                    cur.execute(exc1_2)
                    row1_1=cur.fetchone()
                    #获得当天的流水
                    outcome=row1_1[2]
                    final=row1_1[3]
                else:
                    outcome=row1_1[2]
                    final=row1_1[3]

                #修改flow表
                exc3="update flow set outcome="+str(money*amount+outcome)+",final="+str(final-(money*amount))+" where time_now =to_date('"+Tnow+"','yyyy-mm-dd')"
                try:
                    cur.execute(exc3)
                    ok1=1
                except:
                    g.msgbox("更新flow表出现错误")
                    ok1=0

                #查找原有数量
                exc4="select amount from stock where type="+"'"+answer2+"'"
                cur.execute(exc4)
                row4=cur.fetchone()
                amount1=int(row4[0])#原有数量
                print(amount+amount1)

                #修改stock表
                exc5="update stock set amount="+str(amount1+amount)+" where type="+"'"+answer2+"'"
                try:
                    cur.execute(exc5)
                    ok2=1
                except:
                    g.msgbox("更新amount表出现错误")
                    ok2=0

                if(ok1==ok2==1):
                    con.commit()
                    g.msgbox('修改成功')
                    cur.close()
                    con.close()
                    break
                else:            
                    g.msgbox("修改失败")
                    cur.close()
                    con.close()
                    break
                
                

            
         



        
        
            
        
        
        
            
        
        
        

            
            
