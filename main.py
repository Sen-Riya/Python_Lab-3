from user_registration import create_user, add_user, fetch_all_users,decode_smartscan_code
from scanqr import generate_qr_code
if __name__ == "__main__":
 # Request the number of user records to add
 num = int(input("Enter the number of user records to add: "))

 for i in range(num):
    print(f"Enter SmartScan Code for user {i + 1}")
 smartscan_code = input("Enter SmartScan Code in format'name,email,age': ")
 user_id = i + 1
 decode_smartscan_code(smartscan_code, user_id)

 all_users = fetch_all_users()
 print("All user records:")
 for user in all_users:
    print(user)

 for user in all_users:
    qr_filename = generate_qr_code(user)
 print(f"QR code for user {user['user_id']} saved as {qr_filename}")