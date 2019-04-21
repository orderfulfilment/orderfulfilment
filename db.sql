/*
SQLyog Community v12.4.3 (64 bit)
MySQL - 5.6.12-log : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project`;

/*Table structure for table `cart_table` */

DROP TABLE IF EXISTS `cart_table`;

CREATE TABLE `cart_table` (
  `cartid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `pdctid` int(11) DEFAULT NULL,
  PRIMARY KEY (`cartid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `cart_table` */

insert  into `cart_table`(`cartid`,`userid`,`pdctid`) values 
(4,2,1),
(5,2,1),
(6,2,1),
(9,9,1);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`name`) values 
(1,'pen'),
(2,'lap');

/*Table structure for table `like` */

DROP TABLE IF EXISTS `like`;

CREATE TABLE `like` (
  `like_id` int(50) NOT NULL,
  `user_id` int(50) NOT NULL,
  `product_id` int(50) NOT NULL,
  `like` int(50) NOT NULL,
  PRIMARY KEY (`like_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `like` */

insert  into `like`(`like_id`,`user_id`,`product_id`,`like`) values 
(1,1,1,1),
(2,2,2,2),
(3,3,3,3);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values 
(0,'admin','admin','admin'),
(3,'likhil@gmail.com','123','user'),
(4,'linil@gmail.com','123','user'),
(5,'nandini@gmail.com','123','user'),
(6,'mamtha@gmail.com','123','user'),
(7,'bindya@gmail.com','123','user'),
(8,'mridul@gmail.com','123','user'),
(9,'jhjhj@6666','123456','staff'),
(10,'jhjhj@6666','123456','staff'),
(11,'anu@gmail.com','123456','staff'),
(12,'anu@gmail.com','123456','staff'),
(13,'binu@gmail.com','1','staff');

/*Table structure for table `order_assign` */

DROP TABLE IF EXISTS `order_assign`;

CREATE TABLE `order_assign` (
  `asid` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `staffid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `dates` date DEFAULT NULL,
  PRIMARY KEY (`asid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order_assign` */

insert  into `order_assign`(`asid`,`orderid`,`staffid`,`status`,`dates`) values 
(1,1,6,'completed','2019-02-14');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(50) NOT NULL AUTO_INCREMENT,
  `bank` varchar(50) NOT NULL,
  `accountno` int(50) NOT NULL,
  `keyvalue` int(50) NOT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(50) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `brandname` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `details` varchar(150) DEFAULT NULL,
  `profile_picture` varchar(300) NOT NULL,
  `profit` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `FK_product` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`product_name`,`brandname`,`price`,`category_id`,`details`,`profile_picture`,`profit`) values 
(1,'lap','fyguh',33456,1,'1','static/userimgs/1.jpg',1),
(2,'sap','rrttyt',123467,1,' Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American','static/userimgs/2.jpg',3),
(3,'WEEEEEE','NOKIa ',45,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',5),
(4,'qwee','ttt',34,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',2),
(5,'jhh','vnbvnv',67,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',2),
(6,'ljhk','hjhj',23,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',1),
(7,'hgff','fgfgh',45,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',1),
(8,'jgfhfg','fhgfhg',23,2,'Hai Du Lam, known in-game as Hai is a retired League of Legends player. Hai previously played Mid lane for the Golden Guardians in the North American ','static/userimgs/3.jpg',1),
(9,'pr1','br1',1250,3,'good','static/userimgs/9.jpg',5);

/*Table structure for table `sales_master` */

DROP TABLE IF EXISTS `sales_master`;

CREATE TABLE `sales_master` (
  `transactionid` int(11) NOT NULL AUTO_INCREMENT,
  `total_amount` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `custid` int(11) DEFAULT NULL,
  PRIMARY KEY (`transactionid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `sales_master` */

insert  into `sales_master`(`transactionid`,`total_amount`,`date`,`custid`) values 
(1,16,'2018-09-11',8),
(2,80,'2018-09-11',8),
(3,90,'2018-09-11',8),
(4,63,'2018-09-11',8),
(5,38,'2018-09-11',8),
(6,9,'2018-10-05',8),
(7,66912,'2018-10-05',2),
(8,100368,'2018-10-05',2),
(9,100368,'2018-10-05',2),
(10,66912,'2018-10-11',8),
(11,33456,'2018-10-11',9),
(12,133824,'2019-02-14',8),
(13,66912,'2019-02-14',8);

/*Table structure for table `sales_sub` */

DROP TABLE IF EXISTS `sales_sub`;

CREATE TABLE `sales_sub` (
  `transactionid` int(11) DEFAULT NULL,
  `itemid` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `sales_sub` */

insert  into `sales_sub`(`transactionid`,`itemid`,`quantity`) values 
(1,1,1),
(1,3,1),
(1,5,1),
(2,1,6),
(2,2,2),
(2,3,2),
(2,6,5),
(3,4,2),
(3,2,1),
(3,3,1),
(3,1,1),
(3,5,6),
(3,7,5),
(4,1,3),
(4,2,1),
(4,4,4),
(4,5,3),
(5,1,2),
(5,2,1),
(5,4,2),
(5,6,2),
(6,3,3),
(8,1,1),
(8,1,1),
(8,1,1),
(8,1,1),
(8,1,1),
(9,1,1),
(9,1,1),
(9,1,1),
(7,2,4),
(7,1,3),
(10,1,1),
(10,1,1),
(11,1,1),
(12,1,1),
(12,1,1),
(12,1,1),
(12,1,1),
(13,1,1),
(13,1,1);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staffid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(15) DEFAULT NULL,
  `hname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `image` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staffid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staffid`,`name`,`gender`,`dob`,`hname`,`place`,`city`,`pincode`,`emailid`,`phone`,`image`) values 
(4,'Anujhgjh','Male','12/12/1991','Nandanam','Kizhakkummuri','KOzhikode','673611','anu@gmail.com','987451245','/static/staffimages/20190213-165951.jpg'),
(6,'Binu','Female','12/12/1991','Nandanam','Kizhakkummuri','KOzhikode','673611','binu@gmail.com','987451245','/static/staffimages/20190213-163840.jpg');

/*Table structure for table `transaction_master` */

DROP TABLE IF EXISTS `transaction_master`;

CREATE TABLE `transaction_master` (
  `transaction_id` int(50) NOT NULL,
  `user_id` int(50) NOT NULL,
  `date` date NOT NULL,
  `amount` double NOT NULL,
  `payment_id` int(50) NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `FK_transaction_master` (`user_id`),
  CONSTRAINT `FK_transaction_master` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `transaction_master` */

/*Table structure for table `transaction_sub` */

DROP TABLE IF EXISTS `transaction_sub`;

CREATE TABLE `transaction_sub` (
  `transactionsub_id` int(50) NOT NULL AUTO_INCREMENT,
  `transaction_id` int(50) NOT NULL,
  `product_id` int(50) NOT NULL,
  PRIMARY KEY (`transactionsub_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `transaction_sub` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(80) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `profilepic` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`name`,`email`,`phone`,`place`,`city`,`country`,`profilepic`) values 
(8,'Likhil','likhil@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/1.jpg'),
(9,'Linil','linil@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/9.jpg'),
(10,'Nandini','nandini@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/10.jpg'),
(11,'mamtha@gmail.com','mamtha@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/11.jpg'),
(12,'bindya','bindya@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/12.jpg'),
(13,'mridul','mridul@gmail.com','1111111111','Parambilbazar','Kozhikode','India','static/userimgs/13.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
