# coding: utf-8
#!/usr/bin/env python


ans0  ={'category' :'where',
	   'what'      :'講演会',
	   'where'     :'東3-501',
	   'who'       :'西野教授',
	   'when_time' :'13',
	   'when_day'  :'17',
	   'how'       :'3時間'}

ans1  ={'category' :'where',
	   'what'      :'講演会',	
	   'where'     :'講堂',
	   'who'       :'高木教授',
	   'when_time' :'13',
	   'when_day'  :'17',
	   'how'       :'1時間30分'}

ans2  ={'category' :'where',
	   'what'      :'講演会',
	   'where'     :'東5-202',
	   'who'       :'野田教授',
	   'when_time' :'13',
	   'when_day'  :'17',
	   'how'       :'2時間'}


#sum_of_ans = [ans0,ans1,ans2]
#print(sum_of_ans)

for anser in [ans0,ans1,ans2]:
	print(anser['where'])
	#print('----' + str(i) + '回目----')
 
