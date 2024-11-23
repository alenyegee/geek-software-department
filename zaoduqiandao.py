# 极客数码软件部（Geek Digital Software Department）

import sys
import time
import pyautogui
from PIL import ImageGrab
import cv2

# # 延时模块：等待八小时 (7小时 * 60分钟 * 60秒)
# delay_hours = 7
# print(f"程序将在 {delay_hours} 小时后启动...")
# time.sleep(delay_hours * 60 * 60)  # 7小时延时
#
# print("延时结束，程序开始运行...")


# 定义日志记录函数
def log(message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")


# 检测是否有缩略图并点击
def detect_and_click_thumbnail():
    try:
        # 截取指定区域（微信聊天窗口中的图片区域）
        screenshot = ImageGrab.grab(bbox=(1220, 579, 1467, 831))
        screenshot.save(r'D:\qian_dao\thumbnail.png')  # 保存缩略图便于调试
        log("缩略图已截图保存")

        # 使用 OpenCV 加载彩色图像
        img = cv2.imread(r'D:\qian_dao\thumbnail.png')

        # 判断是否有明显的缩略图（假设缩略图含有大量的亮色或白色）
        if img is not None and img.mean() > 200:
            # 点击缩略图
            pyautogui.moveTo(1283, 727)  # 移动到缩略图位置，具体坐标需根据实际调整
            pyautogui.click()  # 单击放大
            log("已点击缩略图，放大图片。")
            return True
        else:
            log("缩略图检测失败或图像亮度不足")
    except Exception as e:
        log(f"检测缩略图时发生错误: {e}")
    return False


# 扫描二维码
def scan_qr_code():
    try:
        # 右键点击并选择“扫描二维码”
        pyautogui.rightClick(949, 496)  # 右键点击二维码大致位置，坐标根据实际情况调整
        time.sleep(1)  # 等待右键菜单弹出
        pyautogui.moveRel(59, 146)  # 向下移动选择“扫描二维码”选项，具体数值调整
        pyautogui.click()  # 点击“扫描二维码”
        log("已成功扫码！")
    except Exception as e:
        log(f"扫码操作失败: {e}")


# 主循环
def main_loop():
    while True:
        time.sleep(5)  # 每隔5秒检测一次
        # 检查是否出现缩略图并点击
        if detect_and_click_thumbnail():
            time.sleep(2)  # 等待图片放大加载

            # 截取放大后的图片区域
            try:
                screenshot = ImageGrab.grab(bbox=(784, 364, 1132, 721))
                full_image_path = r'D:\qian_dao\full_image.png'
                screenshot.save(full_image_path)
                log("放大后的图片已保存")
            except Exception as e:
                log(f"截图放大图片时发生错误: {e}")
                continue

            # 执行扫码操作
            log("准备执行扫码操作...")
            scan_qr_code()

            # 等待2秒后自动结束运行
            time.sleep(2)
            log("程序即将退出...")
            sys.exit()


if __name__ == "__main__":
    main_loop()
