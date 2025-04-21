import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename="qrcode.png", fill_color="black", back_color="white", size=10, border=4):
    """
    生成二维码并保存为图片
    
    参数:
        data: 要编码的数据(字符串或URL)
        filename: 保存的文件名(默认: qrcode.png)
        fill_color: 二维码颜色(默认: black)
        back_color: 背景颜色(默认: white)
        size: 控制二维码大小(默认: 10)
        border: 边框大小(默认: 4)
    """
    try:
        # 创建QRCode对象
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=border,
        )
        
        # 添加数据
        qr.add_data(data)
        qr.make(fit=True)
        
        # 生成二维码图像
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # 保存图像
        img.save(filename)
        print(f"二维码已成功生成并保存为 {os.path.abspath(filename)}")
        
        # 可选: 显示图像
        if input("是否要显示二维码? (y/n): ").lower() == 'y':
            img.show()
            
    except Exception as e:
        print(f"生成二维码时出错: {e}")

if __name__ == "__main__":
    print("=== Python二维码生成器 ===")
    
    # 获取用户输入
    data = input("请输入要编码的文本或URL: ")
    filename = input("请输入保存文件名(默认: qrcode.png): ") or "qrcode.png"
    fill_color = input("请输入二维码颜色(默认: black): ") or "black"
    back_color = input("请输入背景颜色(默认: white): ") or "white"
    
    # 生成二维码
    generate_qr_code(
        data=data,
        filename=filename,
        fill_color=fill_color,
        back_color=back_color
    )
