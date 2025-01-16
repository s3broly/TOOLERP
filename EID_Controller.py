import pandas as pd
from models.External_item_descriptions import Externalitemdescriptions

class EIDController:


    @staticmethod
    def export_to_excel(external_item_descriptions, output_file):
        # Chuyển list các đối tượng Producttranslation thành DataFrame
        data = []
        for external in external_item_descriptions:
            data.append({
                'ITEMNUMBER': external.itemnumber,
                'PRODUCTCOLORID': external.productcolorid,
                'PRODUCTCONFIGURATIONID': external.productconfigurationid,
                'PRODUCTSIZEID': external.productsizeid,
                'PRODUCTSTYLEID': external.productstyleid,
                'VENDORACCOUNTNUMBER': external.vendoraccountnumber,
                'PRODUCTDESCRIPTIONVENDORGROUPID': external.productdescriptionvendorgroupid,
                'VENDORABCCODE': external.vendorabccode,
                'VENDORABCCODENOTE': external.vendorabccodenote,
                'VENDORPRODUCTDESCRIPTION': external.vendorproductdescription,
                'VENDORPRODUCTNUMBER': external.vendorproductnumber,
            })
        
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False, engine='openpyxl')