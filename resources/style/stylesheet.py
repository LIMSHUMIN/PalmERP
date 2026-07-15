APP_STYLE = """
QMainWindow{
    background:#F5F7FA;
}

QWidget{
    background:#F5F7FA;
    font-family:Segoe UI;
    font-size:13px;
}

QFrame#Sidebar{
    background:white;
    border-right:1px solid #E5E7EB;
}

QFrame#TopBar{
    background:white;
    border-bottom:1px solid #E0E0E0;
}

QPushButton{
    background:transparent;
    border:none;
    text-align:left;
    padding:12px 20px;
    color:#374151;
    font-size:14px;
}

QPushButton:hover{
    background:#E8F5E9;
    color:#2E7D32;
}

QPushButton:checked{
    background:#C8E6C9;
    color:#1B5E20;
    font-weight:bold;
}

QLabel#Title{
    font-size:22px;
    font-weight:bold;
    color:#2E7D32;
}

QLabel#Subtitle{
    color:#757575;
}

QStackedWidget{
    background:#F5F7FA;
}
"""