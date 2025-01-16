from controller.PT_Controller import PTController
if __name__ == "__main__":


    item_keys = input("Nhập các mã Items cách nhau bằng dấu phẩy: ").split(",")
    # Đọc file Excel từ sheet chỉ định
    excel_file = 'Quản lý Item - FA - Vendor (21).xlsx'
    sheet_name = '5 Product translation'
    product_translations = PTController.read_excel(excel_file, sheet_name)

    # Xuất dữ liệu ra CSV
    csv_file = 'datasheet\Producttranslation.xlsx'
    PTController.export_to_excel(product_translations, csv_file)

    print(f"CSV file '{csv_file}' has been generated successfully!")