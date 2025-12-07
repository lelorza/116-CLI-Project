import mysql.connector


def insert_agent_client(uid, username, email, cardno, cardholder, expire, cvv, zip, interests):
    db = None

    try:
        db = mysql.connector.connect(
            host="host",
            user="user",
            password="password",
            database="cs122a_hw2",
        )

        cursor = db.cursor()

        # Insert into User table
        cursor.execute(
            "INSERT INTO User (uid, username, email) VALUES (%s, %s, %s)",
            (uid, username, email)
        )

        # Insert into AgentClient table
        cursor.execute(
            """
            INSERT INTO AgentClient
            (uid, interests, cardholder, expire, cardno, cvv, zip)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (uid, interests, cardholder, expire, cardno, cvv, zip)
        )

        db.commit()

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if db is not None and db.is_connected():
            cursor.close()
            db.close()
