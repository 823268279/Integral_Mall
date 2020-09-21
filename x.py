import turtle
from datetime import *
 
# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
  
 
def drawCircle(content,content_len,init_data,init_data_type,circle_radius,circle_radius_step,color,font_size):
    '''
	content:传入的数组，代表要画的圆上面写的内容，比如1-12月
	content_len：数组长度，用这个元素来做循环，便于调整每次的偏置角度
	init_data： x轴正方向显示当前时间，这个数据就是当前时间
	init_data_type:代表这个是什么类型的，时，分，秒之类的
	circle_radius：圆的半径
	circle_radius_step： 圆环上的数据根据半径和这个长度结合写上内容
	color： 画笔颜色
    '''
    #turtle.pos()
    turtle.home()
    #turtle.mode("logo")
    turtle.pensize(3)
    turtle.pencolor(color)
    turtle.fillcolor('#33BB00')
 
    #turtle.right(90)
    # turtle.right(-360/content_len)
    # Skip(circle_radius+circle_radius_step+10*3)
    # turtle.write(' ', align="center", font=("Courier", font_size,'bold'))
    # Skip(-circle_radius-circle_radius_step-10*3)
    # #turtle.right(360/content_len)
 
 
    Skip(circle_radius+circle_radius_step+10*3)
    turtle.write(init_data_type, align="center", font=("Courier", font_size,'bold'))
    Skip(-circle_radius-circle_radius_step-10*3)
 
    #turtle.right(-90)
 
 
    initdata_index=content.index(init_data)
    for i in range(initdata_index,content_len):
        Skip(circle_radius)
        fantilen=len(content[i])
        if i == initdata_index:
        	turtle.forward(75)
        	turtle.forward(-90)
        	turtle.forward(15)
 
        for name in range(fantilen):
            turtle.write(content[i][name], align="center", font=("Courier", font_size))
            Skip(15)
        Skip(-15*fantilen)
        Skip(-circle_radius)
        turtle.left(360/content_len)
    for i in range(initdata_index):
        Skip(circle_radius)
        fantilen=len(content[i])
        for name in range(fantilen):
            turtle.write(content[i][name], align="center", font=("Courier", font_size))
            Skip(15)
        Skip(-15*fantilen)
        Skip(-circle_radius)
        turtle.left(360/content_len)
 
 
def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s-%d-%d" % (y, m, d)
 
def  runclock():
    turtle.reset()
    t = datetime.today()
    print(t)
    second = t.second #+ t.microsecond * 0.000001
    minute = t.minute #+ second / 60.0
    hour = t.hour# + minute / 60.0
 
 
    Traditional_Chinese= [' ','壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', 
    '拾', '拾壹', '拾贰', '拾叁', '拾肆', '拾伍', '拾陆', '拾柒', '拾捌', '拾玖', 
 '贰拾', '贰拾壹', '贰拾贰', '贰拾叁', '贰拾肆', '贰拾伍', '贰拾陆', '贰拾柒', '贰拾捌', '贰拾玖',
 '叁拾', '叁拾壹', '叁拾贰', '叁拾叁', '叁拾肆', '叁拾伍', '叁拾陆', '叁拾柒', '叁拾捌', '叁拾玖',
 '肆拾', '肆拾壹', '肆拾贰', '肆拾叁', '肆拾肆', '肆拾伍', '肆拾陆', '肆拾柒', '肆拾捌', '肆拾玖',
 '伍拾', '伍拾壹', '伍拾贰', '伍拾叁', '伍拾肆', '伍拾伍', '伍拾陆', '伍拾柒', '伍拾捌', '伍拾玖']
    Simplified_Chinese=[' ','一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
'十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九',
'二十','二十一', '二十二', '二十三', '二十四', '二十五', '二十六', '二十七', '二十八', '二十九',
 '三十','三十一', '三十二', '三十三', '三十四', '三十五', '三十六', '三十七', '三十八', '三十九', 
  '四十','四十一', '四十二', '四十三', '四十四', '四十五', '四十六', '四十七', '四十八', '四十九', 
'五十', '五十一', '五十二', '五十三', '五十四', '五十五', '五十六', '五十七', '五十八', '五十九' 
]
 
    hours= ['壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖','拾', '拾壹','拾贰',
    '拾叁', '拾肆', '拾伍', '拾陆', '拾柒', '拾捌', '拾玖',  '贰拾', '贰拾壹', '贰拾贰', '贰拾叁', '贰拾肆']
    Simplified_hours=['一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
'十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九',
'二十' ,'二十一', '二十二', '二十三', '二十四']
 
    drawCircle(Simplified_Chinese,len(Simplified_Chinese),Simplified_Chinese[second],'秒',250,25,'blue',10)
    drawCircle(Simplified_Chinese,len(Simplified_Chinese),Simplified_Chinese[minute],'分',170,20,'green',10)
    drawCircle(Simplified_hours,len(Simplified_hours),Simplified_hours[hour-1],'时',80,15,'red',10)
 
    printer = turtle.Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.color('#11CCFF')
    printer.right(-90)
    printer.penup()
    printer.forward(40)
    printer.write(Week(t), align="center",font=("Courier", 10, "bold"))
    printer.back(80)
    printer.write(Date(t), align="center",font=("Courier", 14, "bold"))
    print(Week(t),Date(t))
    printer.right(90)
    turtle.ontimer(runclock, 1000)
 
 
 
def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)
    ts = turtle.getscreen()
    ts.bgcolor("black")
 
    runclock()
    turtle.mainloop()     
if __name__ == "__main__":
    main()