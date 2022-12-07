amount = int(input("Enter number of files"))
allowed_operations = {}
operation_meaning_dict = {
    "WRITE": "W",
    "READ": "R",
    "EXECUTE": "X"
}

for i in range(amount):
    user_input = input("Enter file and operation")
    arguments = user_input.split(" ")
    file_name = arguments[0]
    permission = arguments[1::]
    allowed_operations[file_name] = permission


m = int(input("Enter amount of operation"))

request_list = []

for i in range(m):
    request_list.append(input("Enter operation and file"))


for request in request_list:
    operation = request.split(" ")[0]
    normalizedOperation = operation_meaning_dict[operation]
    file_name = request.split(" ")[1]

    try:
        file_permissions = allowed_operations[file_name]
        file_permissions.index(normalizedOperation)
        print("OK!")
    except:
        print("Access Denied")






