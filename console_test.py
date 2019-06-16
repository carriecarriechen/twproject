import console

c = console.getconsole()

c.title("Console Example")

# 输出到指定位置
c.text(0, 0, "here's some white text on white background", 0x1f)
c.text(10, 5, "line five, column ten")

