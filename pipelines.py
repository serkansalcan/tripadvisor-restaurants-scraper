import mysql.connector


class MysqlPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS istanbul(
                    name VARCHAR(255),
                    cuisine VARCHAR(255),
                    reviews VARCHAR(255),
                    rating FLOAT,
                    address VARCHAR(255),
                    email VARCHAR(255),
                    phone VARCHAR(255)
                )
                """)

    def process_item(self, item, spider):
        name = item.get('name')
        cuisine = item.get('cuisine')
        reviews = item.get('reviews')
        rating = item.get('rating')
        address = item.get('address')
        email = item.get('email')
        phone = item.get('phone')

        if all((name, cuisine, reviews, rating, address, email, phone)):
            cuisine_str = ', '.join(cuisine)  # Convert list to comma-separated string
            self.cur.execute("""INSERT INTO istanbul VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (
                name,
                cuisine_str,
                reviews,
                rating,
                address,
                email,
                phone
            ))

            self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
