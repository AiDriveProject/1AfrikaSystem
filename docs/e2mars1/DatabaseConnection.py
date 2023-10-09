import mysql.connector


# MySQL database configuration
host = "35.215.126.220"
user = "uwaixbzxcrdnd"
password = "hj8uk7zmeu7l"
database_name = "dbuy9apvyook4r"



try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )

    if connection.is_connected():
       print("Connected to the MySQL database")
    # Create a cursor to interact with the database
       cursor = connection.cursor()


    def TABLE_creation():
        cursor = connection.cursor()
        insert_query =f"CREATE TABLE `User_Details`(`User_Details_id`bigint unsigned NOT NULL AUTO_INCREMENT,`image`LONGBLOB NOT NULL,`full_name`varchar(50)NOT NULL,`email`varchar(50) NOT NULL,`phone`  INT(11) NOT NULL,`select`varchar(50)  NOT  NULL,`password`varchar(50)NOT NULL,`last_update`timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY(`User_Details_id`))"
        cursor.execute(insert_query)
        connection.commit()
        print("Creating Table processed as successfully.")


    def saving_in_MySQL_User_details_with_images(FilePath: str, name: str, email: str, phone: int, select: str, password: str):
        cursor = connection.cursor()
        with open(FilePath, "rb")as File_Ma:
          BinaryData = File_Ma.read()

        insert_query = f"INSERT INTO `User_Details`(`image`,`full_name`, `email`, `phone`, `select`, `password`) VALUES (%s,'{name}','{email}','{int(phone)}','{select}','{password}')"
        cursor.execute(insert_query, (BinaryData,))
        connection.commit()
        print("Value processed as successfully.")



    def saving_in_MySQL_Books(name: str, email: str, spacial_request: str, service_date: str, spacial_r: str):
        cursor = connection.cursor()
        insert_query = f"INSERT INTO `User_Services_Books`(`name`, `email`, `spacial_request`, `selected_service`, `service_date`) VALUES ('{name}','{email}','{spacial_request}','{service_date}','{spacial_r}')"
        cursor.execute(insert_query)
        connection.commit()
        print("Value processed as successfully.")


    def Read_in_MySQL_Image(email: str, password: str):
        cursor = connection.cursor()
        select_query = f"SELECT * FROM `User_Details` WHERE email ='{email}' AND password = {password}"
        cursor.execute(select_query)
        result = cursor.fetchone()
        cursor.close()
        if result is not None:
            print("Operation Successful Completed ", result[2])
            return result

        else:
            print("Not Found")
        # Commit the transaction to save the changes
        connection.commit()
        print("Value processed as successfully.")




    def Read_in_MySQL_Image_ALL():
        cursor = connection.cursor()
        select_query = f"SELECT * FROM `User_Details`"
        cursor.execute(select_query)
        result = cursor.fetchall()
        cursor.close()

        if result is not None:
            print("Operation Successfully Completed")
            # Commit the transaction to save the changes
            connection.commit()
            print("Value processed successfully.")
            return result
        else:
            print("Not Found")
            return None



except mysql.connector.Error as error:
    print(f"Error: {error}")
finally:
    if connection.is_connected():

        print("Action Finish.")