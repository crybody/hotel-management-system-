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

# 退订房间
def tuiding(conn,cursor,uid,room,stime,ftime):
	l = len(room)
	t=chaxun2.time
	for i in range(1):
		if (stime[i]<=t)and(ftime[i]>t):
			sql="update history set finish_time= '"+str(chaxun2.time)+"' where ((room_id = "+str(room[i])+') and (user_id = '+str(uid)+')'
			print(sql)
			cursor.execute(sql)
		if (stime[i]>t):
			sql="delete from history where (room_id="+str(room[i])+")and(user_id="+str(uid)+")and(start_time="+str(stime[i])+")and(finish_time="+str(ftime[i])+")"
			print(sql)
			cursor.execute(sql)


# 升级VIP
def vip(conn,cursor,n,gid):
	sql="update guest set vip_class ="+str(n)+"where id="+str(gid)
	cursor.execute(sql)
	conn.commit()

# 判断输入信息是否存在
def panduan_shuru(cursor,a,s,l):
	'''A为输入的信息，s为表名,l为列名'''
	sql="select * from "+str(s)+' where '+str(l)+'='+str(a)
	cursor.execute(sql)		
	m = cursor.fetchall()
	if m:
		return 1
	else:
		return 0	
# 判断输入信息是否符合要求
def panduan_ruzhu(a,s):
	'''a为输入的房间号，s为未入住的房间列表'''
	for i in s:
		if str(a) in i:
			return 0
	return 1


# 判断输入起始和终止日期是否为日期（需要 import import dateutil.parser）
def pandun_riqi(s,f):
	try:
		d = dateutil.parser.parse(s)
		o = dateutil.parser.parse(f)
		return 1
	except:
		return 0
	c
# 判断输入日期是否符合要求
def panduan_time(a,b,o):
	'''a，b为起止日期，o为日期格式判断结果'''
	if o == 1:
		if a<=b:
			return 1
	else:
		return 0
	
