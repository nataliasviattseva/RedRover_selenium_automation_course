class OrderData:
    user_data_with_invalid_credentials = [["", "Ivanov", "12345", "Error: First Name is required"],
                                          ["Ivan", "", "12345", "Error: Last Name is required"],
                                          ["Ivan", "Ivanov", "", "Error: Postal Code is required"]]

    user_data_with_valid_credentials = ["Ivan", "Ivanov", "12345", "Error: First Name is required"]

    successful_message = "Thank you for your order!"
