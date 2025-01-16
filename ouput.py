import pandas as pd

def search_and_export(input_file, sheet_name, item_codes, output_file):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(input_file, sheet_name=sheet_name)
    
    # Danh sách để lưu kết quả
    results = []
    
    # Lặp qua tất cả mã items cần tìm
    for item in item_codes:
        # Tìm kiếm các dòng chứa mã item
        item_rows = df[df.apply(lambda row: item in row.values.astype(str), axis=1)]
        
        # Nếu tìm thấy mã item, lấy tất cả các giá trị trên dòng đó
        if not item_rows.empty:
            for _, row in item_rows.iterrows():
                results.append(row.tolist())  # Chuyển dòng thành danh sách
    
    # Chuyển kết quả thành DataFrame
    results_df = pd.DataFrame(results, columns=df.columns)
    
    # Xuất kết quả ra file Excel mới
    results_df.to_excel(output_file, index=False)
    print(f"Đã xuất kết quả vào file {output_file}")

# Ví dụ sử dụng
input_file = 'Quản lý Item - FA - Vendor (21).xlsx'  # Đường dẫn đến file Excel đầu vào
sheet_name = 'Khai báo Item'
item_codes = input("Nhập các mã Items cách nhau bằng dấu phẩy: ").split(",")
output_file = 'output_file.xlsx'  # Đường dẫn đến file Excel xuất ra

search_and_export(input_file, sheet_name, item_codes, output_file)
