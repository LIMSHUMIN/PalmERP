from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from ui.components.sidebar import Sidebar
from ui.components.topbar import TopBar

from ui.pages.dashboard_page import DashboardPage
from ui.pages.supplier_page import SupplierPage
from ui.pages.purchase_page import PurchasePage
from ui.pages.harvest_page import HarvestPage
from ui.pages.fertiliser_page import FertiliserPage
from ui.pages.advance_page import AdvancePage
from ui.pages.settlement_page import SettlementPage
from ui.pages.report_page import ReportPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PalmERP Enterprise")
        self.resize(1400, 800)

        self.build_ui()
        self.load_pages()
        self.connect_navigation()

    def build_ui(self):

        # Central Widget
        central = QWidget()
        self.setCentralWidget(central)

        # Main Layout
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        # Right Layout
        right = QVBoxLayout()
        right.setContentsMargins(0, 0, 0, 0)
        right.setSpacing(0)

        # Top Bar
        self.topbar = TopBar()
        right.addWidget(self.topbar)

        # Content Area
        self.stack = QStackedWidget()
        right.addWidget(self.stack)

        root.addLayout(right)

    def load_pages(self):

        self.dashboard_page = DashboardPage()
        self.supplier_page = SupplierPage()
        self.purchase_page = PurchasePage()
        self.harvest_page = HarvestPage()
        self.fertiliser_page = FertiliserPage()
        self.advance_page = AdvancePage()
        self.settlement_page = SettlementPage()
        self.report_page = ReportPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.supplier_page)
        self.stack.addWidget(self.purchase_page)
        self.stack.addWidget(self.harvest_page)
        self.stack.addWidget(self.fertiliser_page)
        self.stack.addWidget(self.advance_page)
        self.stack.addWidget(self.settlement_page)
        self.stack.addWidget(self.report_page)

        self.stack.setCurrentWidget(self.dashboard_page)

    def connect_navigation(self):

        self.sidebar.btn_dashboard.clicked.connect(
            lambda: self.show_page(self.dashboard_page)
        )

        self.sidebar.btn_supplier.clicked.connect(
            lambda: self.show_page(self.supplier_page)
        )

        self.sidebar.btn_purchase.clicked.connect(
            lambda: self.show_page(self.purchase_page)
        )

        self.sidebar.btn_harvest.clicked.connect(
            lambda: self.show_page(self.harvest_page)
        )

        self.sidebar.btn_fertiliser.clicked.connect(
            lambda: self.show_page(self.fertiliser_page)
        )

        self.sidebar.btn_advance.clicked.connect(
            lambda: self.show_page(self.advance_page)
        )

        self.sidebar.btn_settlement.clicked.connect(
            lambda: self.show_page(self.settlement_page)
        )

        self.sidebar.btn_reports.clicked.connect(
            lambda: self.show_page(self.report_page)
        )

    def show_page(self, page):

        self.stack.setCurrentWidget(page)