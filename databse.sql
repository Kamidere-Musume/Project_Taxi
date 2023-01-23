create database taxi;
 use taxi;
 create table user(
 User_Id int(10) not null primary key auto_increment ,
 User_Fname varchar(255) not null,
 User_Lname varchar(255) not null,
 User_Address varchar(255) not null,
 User_Email varchar(255) not null unique,
 User_Phone_Number int(10) not null,
 Payment_Method varchar(255) not null,
 User_Password varchar(255) not null
 );

create table driver(

Driver_Id int(10) primary key auto_increment,
Driver_Fname varchar(255) not null,
Driver_Lname varchar(255) not null,
Driver_Email varchar(255) not null unique,
Driver_Password varchar(255) not null,
Vehicle_Id varchar(255) not null,
Driver_Phone_Number int(10) not null,
Driver_Address varchar(255) not null,
Assign_Status varchar(255) not null
);
 
 create table booking(
Booking_Id int(10) primary key auto_increment,
Current_location varchar(255) not null,
Destination varchar(255) not null,
Price varchar(255) not null,
Distance varchar(255) not null,
User_Id	int(10) not null,
foreign key (User_Id) references user(User_Id),
Booking_Status varchar(255) not null,
Driver_Id int(10),
Foreign key (Driver_Id) references driver(Driver_Id),
Pickup_Date varchar(255) not null,
Pickup_Time varchar(255) not null
 );

create table admin(
Admin_Id int primary key,
Admin_Fname varchar(255) not null,
Admin_Lname varchar(255) not null,
Admin_Email varchar(255) not null,
Admin_Password varchar(255) not null
);
 show databases;
 