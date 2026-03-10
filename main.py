"""
Hello World 应用示例

这是一个简单的示例应用，演示如何使用 M20 框架创建应用。
"""

import customtkinter as ctk
from pathlib import Path

# 导入框架（由 app_launcher 设置 PYTHONPATH，或通过 pip install 安装）
from m20gui import build_ui_from_xml

# 动态导入 handlers
import importlib.util
current_dir = Path(__file__).parent
handlers_path = current_dir / "handlers.py"
if handlers_path.exists():
    spec = importlib.util.spec_from_file_location("handlers", handlers_path)
    handlers = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(handlers)
else:
    handlers = None

if __name__ == "__main__":
    # 设置主题
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    # 加载XML文件
    xml_file = current_dir / "ui.xml"
    
    if xml_file.exists():
        # 构建界面
        app = build_ui_from_xml(str(xml_file), handlers)
        app.mainloop()
    else:
        # 如果没有 XML，创建一个简单的窗口
        app = ctk.CTk()
        app.title("Hello World")
        app.geometry("400x200")
        
        label = ctk.CTkLabel(
            app,
            text="Hello, World!",
            font=ctk.CTkFont(size=24)
        )
        label.pack(expand=True)
        
        app.mainloop()
