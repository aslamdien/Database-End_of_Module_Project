-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: End_of_Module
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `next_of_kin`
--

DROP TABLE IF EXISTS `next_of_kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `next_of_kin` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `next_of_kin_of` varchar(25) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `next_of_kin`
--

LOCK TABLES `next_of_kin` WRITE;
/*!40000 ALTER TABLE `next_of_kin` DISABLE KEYS */;
INSERT INTO `next_of_kin` VALUES (1,'Kayoum','0829782837','Ayyoob'),(2,'Earl','0321456987','James'),(3,'Kevin','0321456986','Dwayne'),(4,'Candice','0258974613','Jason'),(5,'Godwin1','0735887757','Thapelo');
/*!40000 ALTER TABLE `next_of_kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `date_of_entry` date DEFAULT NULL,
  `name` varchar(25) NOT NULL,
  `surname` varchar(25) NOT NULL,
  `id_number` varchar(13) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `reason` varchar(25) NOT NULL,
  `next_of_kin_ID` int unsigned DEFAULT NULL,
  `loged_in` time DEFAULT NULL,
  `loged_out` time DEFAULT NULL,
  `in_or_out` varchar(25) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `next_of_kin_ID` (`next_of_kin_ID`),
  CONSTRAINT `register_ibfk_1` FOREIGN KEY (`next_of_kin_ID`) REFERENCES `next_of_kin` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES (1,'2021-07-11','Ayyoob','Slamdien','9808165433084','0614170272','turbostar','Visitor',NULL,'10:04:58','00:00:00','Log In'),(2,'2021-07-11','James','Brown','0256478951365','0259876431','starwars','Visitor',NULL,'10:26:14','00:00:00','Log In'),(3,'2021-07-10','Dwayne','Johnson','0321654789654','0213654789','jumanji','Visitor',NULL,'20:03:47','09:37:00','Log Out'),(4,'2021-07-10','Jason','Wandrag','4587956231475','0735990312','lifechoices2020','Employee',NULL,'21:09:48','21:09:48','Log Out'),(5,'2021-07-10','Thapelo','Tsotetsi','669854751234','0670220764','python3','Employee',NULL,'20:03:47','00:00:00','Log In');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:19:08
