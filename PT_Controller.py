import pandas as pd
from models.Product_translation import Producttranslation

class PTController:
    @staticmethod
    def read_excel(file_path, sheet_name):
        # Đọc file Excel với pandas, chỉ định sheet cần đọc
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Chuyển dữ liệu trong DataFrame thành các đối tượng Producttranslation
        product_translations = []
        for _, row in df.iterrows():
            translation = Producttranslation(
                productnumber=row['PRODUCTNUMBER'],
                languageid='us-EN',
                description=row['DESCRIPTION']
            )
            product_translations.append(translation)
        
        return product_translations

    @staticmethod
    def export_to_excel(product_translations, output_file):
        # Chuyển list các đối tượng Producttranslation thành DataFrame
        data = []
        for translation in product_translations:
            data.append({
                'ProductNumber': translation.productnumber,
                'LanguageId': translation.languageid,
                'Description': translation.description
            })
        
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False, engine='openpyxl')