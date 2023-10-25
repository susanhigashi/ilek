import sqlite3
import smtplib
from email.mime.text import MIMEText

class WineAlertSystem:
    def __init__(self, db_file, email_config):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.email_config = email_config

    def check_criteria_and_alert(self):
        # Query the database for user criteria and emails
        self.cursor.execute('''
            SELECT user_id, wine_type, flavor, country, region, min_vintage, max_vintage, max_price, email
            FROM user_search_criteria
            INNER JOIN users ON user_search_criteria.user_id = users.user_id
        ''')
        user_criteria = self.cursor.fetchall()

        # Query the database for new wines matching criteria
        for criteria in user_criteria:
            user_id, wine_type, flavor, country, region, min_vintage, max_vintage, max_price, email = criteria

            self.cursor.execute('''
                SELECT name, type, flavor, country, region, vintage, price
                FROM wine_properties
                WHERE type = ? AND flavor = ? AND country = ? AND region = ? AND vintage BETWEEN ? AND ? AND price <= ?
            ''', (wine_type, flavor, country, region, min_vintage, max_vintage, max_price))

            matching_wines = self.cursor.fetchall()

            if matching_wines:
                self.send_email_notification(email, matching_wines)

    def send_email_notification(self, recipient_email, matching_wines):
        # Configure the email
        msg = MIMEText("New wines matching your criteria:\n\n" + "\n".join(map(str, matching_wines)))
        msg['Subject'] = "Wine Alert"
        msg['From'] = self.email_config['sender_email']
        msg['To'] = recipient_email

        # Connect to the email server and send the email
        try:
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['sender_email'], self.email_config['sender_password'])
            server.sendmail(self.email_config['sender_email'], [recipient_email], msg.as_string())
            server.quit()
        except Exception as e:
            print(f"Email notification error: {str(e)}")

    def close(self):
        self.conn.close()
