import bcrypt

from database.connection import get_connection


class UserService:

    def login(self, username, password):

        conn = get_connection()

        if conn is None:
            return None

        try:

            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    UserID,
                    UserName,
                    PasswordHash,
                    FullName,
                    IsAdmin,
                    Active
                FROM Users
                WHERE UserName=?
            """, username)

            user = cursor.fetchone()

            if user is None:
                return None

            if not user.Active:
                return None

            password_hash = user.PasswordHash

            if isinstance(password_hash, str):
                password_hash = password_hash.encode()

            if bcrypt.checkpw(
                password.encode(),
                password_hash
            ):

                return user

            return None

        except Exception as e:

            print(e)
            return None

        finally:

            conn.close()