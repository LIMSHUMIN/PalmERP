from services.supplier_service import SupplierService


service = SupplierService()


suppliers= service.get_all_suppliers()


for s in suppliers:
    print(s)