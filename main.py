# main.py
import sys
import os
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QAction, QVBoxLayout,
    QWidget, QScrollArea, QMessageBox, QMenu, QProgressDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from preprocessing import preprocess
from visualization import generate_all_insights


class RetailDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retail Sales Data Visualization Dashboard")
        self.setGeometry(100, 100, 1000, 600)

        self.data = None
        self.image_label = QLabel()
        self.image_label.setScaledContents(True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.image_label)

        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self._create_menu()

    def _create_menu(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        load_action = QAction("Load and Preprocess Data", self)
        load_action.triggered.connect(self.load_data)
        file_menu.addAction(load_action)

        # Product menu
        product_menu = menu_bar.addMenu("Product")
        self._add_action(product_menu, "Top Product Categories", "top_categories_by_revenue_treemap.png")
        self._add_action(product_menu, "SKU Sales Distribution", "sku_sales_distribution.png")
        self._add_action(product_menu, "Zero Sales by Item Type", "zero_retail_by_type.png")
        self._add_action(product_menu, "Warehouse Sales by Item Type", "boxplot_warehouse_sales.png")
        self._add_action(product_menu, "Average Transfers by Item Type", "average_transfers_by_item_type.png")

        # Supplier menu
        supplier_menu = menu_bar.addMenu("Supplier")
        self._add_action(supplier_menu, "Top Suppliers by Item Type Diversity", "supplier_itemtype_bar_chart.png")
        self._add_action(supplier_menu, "Retail Sales by Top Suppliers", "boxplot_retail_by_supplier.png")
        self._add_action(supplier_menu, "Supplier vs Item Type Heatmap", "supplier_itemtype_heatmap.png")
        self._add_action(supplier_menu, "Supplier Sales Trend Comparison", "top_supplier_sales_comparison_bar.png")
        self._add_action(supplier_menu, "Supplier Performance Overview", "supplier_performance.png")

        # Inventory menu
        inventory_menu = menu_bar.addMenu("Inventory")
        self._add_action(inventory_menu, "Retail vs Warehouse Sales", "retail_vs_warehouse_sales.png")
        self._add_action(inventory_menu, "Transfer-to-Sales Ratio Distribution", "transfer_ratio_distribution.png")

        # Strategy menu
        strategy_menu = menu_bar.addMenu("Strategy")
        self._add_action(strategy_menu, "Pareto Distribution", "pareto_distribution.png")
        self._add_action(strategy_menu, "Scatter Matrix of Sales Channels", "scatter_matrix_sales.png")
        self._add_action(strategy_menu, "Monthly Retail Sales Trend", "monthly_retail_sales.png")
        self._add_action(strategy_menu, "Underperforming Products", "underperforming_products.png")

    def _add_action(self, menu, label, filename):
        action = QAction(label, self)
        action.triggered.connect(lambda checked, f=filename: self.show_image(f))
        menu.addAction(action)

    def load_data(self):
        try:
            progress = QProgressDialog("Starting...", None, 0, 0, self)
            progress.setWindowTitle("Please Wait")
            progress.setWindowModality(Qt.WindowModal)
            progress.setCancelButton(None)
            progress.setMinimumDuration(0)
            progress.show()
            QApplication.processEvents()

            progress.setLabelText("Loading dataset...")
            QApplication.processEvents()
            filepath = os.path.join("data", "Retail and wherehouse Sale.csv")
            df = pd.read_csv(filepath)

            progress.setLabelText("Cleaning and preprocessing...")
            QApplication.processEvents()
            df = preprocess(filepath)

            progress.setLabelText("Generating visualizations...")
            QApplication.processEvents()
            generate_all_insights(df)

            progress.setLabelText("Finalizing...")
            QApplication.processEvents()
            self.data = df

            progress.close()
            QMessageBox.information(self, "Success", "Data loaded and visualizations generated.")
        except Exception as e:
            progress.close()
            QMessageBox.critical(self, "Error", str(e))

    def show_image(self, filename):
        path = os.path.join("assets", filename)
        if os.path.exists(path):
            self.image_label.setPixmap(QPixmap(path))
        else:
            QMessageBox.warning(self, "Warning", f"Image file not found: {filename}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RetailDashboard()
    window.show()
    sys.exit(app.exec_())
