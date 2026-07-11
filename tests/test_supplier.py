from services.supplier_service import SupplierService


service = SupplierService()


result = service.search_supplier("AHMAD")


for row in result:
    print(row)