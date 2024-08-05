database = []
create_user = lambda user_id, name, email, age: {
 'user_id': user_id,
 'name': name,
 'email': email,
 'age': int(age)
}
add_user = lambda user_record: database.append(user_record)
fetch_all_users = lambda: database

def decode_smartscan_code(smartscan_code, user_id):
    parts = smartscan_code.split(',')
    if len(parts) == 3:
        name, email, age = parts
        return add_user(create_user(user_id, name, email, age))
    else:
        print("Invalid format: Ensure the format is 'name,email,age'")
