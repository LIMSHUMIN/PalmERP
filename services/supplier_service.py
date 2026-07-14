from database.connection import get_connection


class SupplierService:

    def get_all_suppliers(self):

        conn = get_connection()

        if conn is None:
            return []

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    SupplierID,
                    SupplierCode,
                    SupplierName,
                    Phone,
                    Address,
                    IsActive
                FROM Suppliers
                ORDER BY SupplierCode
                """
            )

            return cursor.fetchall()

        except Exception as e:

            print("Get supplier error:")
            print(e)

            return []

        finally:

            conn.close()

    ####################################################################

    def add_supplier(
        self,
        supplier_code,
        supplier_name,
        phone,
        address
    ):

        conn = get_connection()

        if conn is None:
            return False

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Suppliers
                (
                    SupplierCode,
                    SupplierName,
                    Phone,
                    Address,
                    IsActive
                )
                VALUES
                (?, ?, ?, ?, 1)
                """,
                supplier_code,
                supplier_name,
                phone,
                address
            )

            conn.commit()

            return True

        except Exception as e:

            print("Add supplier error:")
            print(e)

            return False

        finally:

            conn.close()

    ####################################################################

    def update_supplier(
        self,
        supplier_id,
        supplier_code,
        supplier_name,
        phone,
        address
    ):

        conn = get_connection()

        if conn is None:
            return False

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE Suppliers
                SET
                    SupplierCode=?,
                    SupplierName=?,
                    Phone=?,
                    Address=?
                WHERE SupplierID=?
                """,
                supplier_code,
                supplier_name,
                phone,
                address,
                supplier_id
            )

            conn.commit()

            return True

        except Exception as e:

            print("Update supplier error:")
            print(e)

            return False

        finally:

            conn.close()

    ####################################################################

    def delete_supplier(self, supplier_id):

        conn = get_connection()

        if conn is None:
            return False

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE Suppliers
                SET IsActive = 0
                WHERE SupplierID = ?
                """,
                supplier_id
            )

            conn.commit()

            return True

        except Exception as e:

            print("Delete supplier error:")
            print(e)

            return False

        finally:

            conn.close()

    ####################################################################

    def hard_delete_supplier(self, supplier_id):

        conn = get_connection()

        if conn is None:
            return False

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM Suppliers
                WHERE SupplierID = ?
                """,
                supplier_id
            )

            conn.commit()

            return True

        except Exception as e:

            print("Hard delete supplier error:")
            print(e)

            return False

        finally:

            conn.close()

    ####################################################################

    def search_supplier(self, keyword):

        conn = get_connection()

        if conn is None:
            return []

        try:

            cursor = conn.cursor()

            sql = """
            SELECT
                SupplierID,
                SupplierCode,
                SupplierName,
                Phone,
                Address,
                IsActive
            FROM Suppliers
            WHERE
                SupplierCode LIKE ?
                OR SupplierName LIKE ?
                OR Phone LIKE ?
            ORDER BY SupplierCode
            """

            key = f"%{keyword}%"

            cursor.execute(
                sql,
                key,
                key,
                key
            )

            return cursor.fetchall()

        except Exception as e:

            print("Search supplier error:")
            print(e)

            return []

        finally:

            conn.close()