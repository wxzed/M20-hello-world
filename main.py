"""
Hello World 应用示例

这是一个简单的示例应用，演示如何使用 M20 框架创建应用。
"""

import customtkinter as ctk
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
# 优先使用 PYTHONPATH（由 app_launcher 设置），如果没有则尝试计算
current_dir = Path(__file__).parent
if 'PYTHONPATH' not in os.environ:
    # 如果是从 GitHub 下载的，路径结构是：installed_apps/hello_world/
    # 需要向上2级到项目根目录 M20-XML-GUI/
    if 'installed_apps' in str(current_dir):
        project_root = current_dir.parent.parent
        sys.path.insert(0, str(project_root))
    # 如果在 M20-app 仓库中开发，尝试找到 M20-XML-GUI（假设在同一个父目录下）
    else:
        potential_root = current_dir.parent.parent.parent / "M20-XML-GUI"
        if potential_root.exists():
            sys.path.insert(0, str(potential_root))
        else:
            # 最后尝试直接向上3级（兼容旧逻辑）
            project_root = current_dir.parent.parent.parent
            sys.path.insert(0, str(project_root))

# 导入框架
from lib import build_ui_from_xml

# 动态导入handlers
import importlib.util
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
