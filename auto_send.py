import time as t
import pyautogui as auto
import os

def inputs():
    auto.hotkey('ctrl','v')
def send():
    auto.click(mouse.x,mouse.y)
def main():
    os.system('cls')
    os.system('color 0a')
    global macz,times
    macz = input("请复制要发送的信息,之后点回车\n")
    times = input("请输入发送次数：\n")
    print("请在五秒钟之内将鼠标移到发送键位置")
    
main()
t.sleep(5)
mouse = auto.position()

for i in range(int(times)):
    inputs()
    send()
