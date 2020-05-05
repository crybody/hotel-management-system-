import chaxun2
import dateutil.parser

# 订购房间
def yuding(conn,cursor,gid,n,stime,ftime,):
	# n为房间号
	m=n
	s=stime
	f=ftime
	l = len(m)
	for i in range (l):
		# 将记录写入订单表
		sql="INSERT INTO history VALUES ("+str(gid)+","+str(m[i])+","+str(s[0])+","+str(f[0])+")"
		print(sql)
		cursor.execute(sql)
		# 查询房间类型
		sql2="select class from room where id="+str(m[i])
		cursor.execute(sql2)
		ty=cursor.fetchall()
		# 查询类型对应价格
		sql3="select rate from price where type='"+"ho_"+str(ty[0][0]+1)+"'"
		print(sql3)
		cursor.execute(sql3)
		mo=cursor.fetchall()
		# 写入流水
		t=chaxun2.time
		sqlx="select time_now from flow where time_now="+str(t)
		cursor.execute(sqlx)
		p=cursor.fetchall()
		print(p)
		if p :	
			sql5="update flow set income =(income+"+str(mo[0][0])+")where time_now="+t
			sql6="update flow set final=(income-outcome)where time_now="+t
			cursor.execute(sql5)
			cursor.execute(sql6)
			conn.commit()
		else:
			sql4="insert into flow values ("+str(chaxun2.time)+","+""+str(mo[0][0])+",0,"+str(mo[0][0])+")"
			print(sql4)
			cursor.execute(sql4)
			conn.commit()
	conn.commit()

