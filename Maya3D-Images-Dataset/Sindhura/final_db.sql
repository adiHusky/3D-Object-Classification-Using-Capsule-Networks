CREATE DATABASE  IF NOT EXISTS `capsule_images` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `capsule_images`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: capsule_images
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `background`
--

DROP TABLE IF EXISTS `background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `background` (
  `background_id` varchar(45) NOT NULL,
  `background_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`background_id`),
  UNIQUE KEY `background_name_UNIQUE` (`background_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `background`
--

LOCK TABLES `background` WRITE;
/*!40000 ALTER TABLE `background` DISABLE KEYS */;
INSERT INTO `background` VALUES ('bk_01','black'),('bk_02','white');
/*!40000 ALTER TABLE `background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `category` (
  `category_id` varchar(45) NOT NULL,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `category_name_UNIQUE` (`category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('C_01','Animal'),('C_02','Automobile'),('C_03','Bird'),('C_04','Electronics'),('C_05','Fantasy'),('C_06','Fashion'),('C_07','Food'),('C_08','Footware'),('C_09','Household'),('C_10','Humanbody'),('C_11','Monuments'),('C_12','Nature'),('C_13','Others'),('C_14','Sports'),('C_15','Weapon');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `image` (
  `image_id` varchar(45) NOT NULL,
  `image_size` varchar(100) DEFAULT NULL,
  `image_type` varchar(100) DEFAULT NULL,
  `image_path` varchar(100) DEFAULT NULL,
  `X` int(11) NOT NULL,
  `Y` int(11) NOT NULL,
  `Z` int(11) NOT NULL,
  `object_id` varchar(45) DEFAULT NULL,
  `image` blob,
  `image_shape` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`image_id`),
  KEY `object_id_idx` (`object_id`),
  CONSTRAINT `object_id` FOREIGN KEY (`object_id`) REFERENCES `object` (`object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object`
--

DROP TABLE IF EXISTS `object`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `object` (
  `object_id` varchar(45) NOT NULL,
  `object_name` varchar(100) DEFAULT NULL,
  `sub_category_id` varchar(45) DEFAULT NULL,
  `texture_id` varchar(45) DEFAULT NULL,
  `background_id` varchar(45) DEFAULT NULL,
  `shadow_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`object_id`),
  KEY `sub_category_id_idx` (`sub_category_id`),
  KEY `background_id_idx` (`background_id`),
  KEY `texture_id_idx` (`texture_id`),
  KEY `shadow_id_idx` (`shadow_id`),
  CONSTRAINT `background_id` FOREIGN KEY (`background_id`) REFERENCES `background` (`background_id`),
  CONSTRAINT `shadow_id` FOREIGN KEY (`shadow_id`) REFERENCES `shadow` (`shadow_id`),
  CONSTRAINT `sub_category_id` FOREIGN KEY (`sub_category_id`) REFERENCES `sub_category` (`sub_category_id`),
  CONSTRAINT `texture_id` FOREIGN KEY (`texture_id`) REFERENCES `texture` (`texture_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object`
--

LOCK TABLES `object` WRITE;
/*!40000 ALTER TABLE `object` DISABLE KEYS */;
INSERT INTO `object` VALUES ('O_01','Mammal','S_01',NULL,NULL,NULL);
/*!40000 ALTER TABLE `object` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shadow`
--

DROP TABLE IF EXISTS `shadow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `shadow` (
  `shadow_id` varchar(45) NOT NULL,
  `shadow_presence` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`shadow_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shadow`
--

LOCK TABLES `shadow` WRITE;
/*!40000 ALTER TABLE `shadow` DISABLE KEYS */;
INSERT INTO `shadow` VALUES ('sh_01','yes'),('sh_02','no');
/*!40000 ALTER TABLE `shadow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_category`
--

DROP TABLE IF EXISTS `sub_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sub_category` (
  `sub_category_id` varchar(45) NOT NULL,
  `category_id` varchar(45) DEFAULT NULL,
  `sub_category_namel` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sub_category_id`),
  UNIQUE KEY `sub_category_namel_UNIQUE` (`sub_category_namel`),
  KEY `category_id_idx` (`category_id`),
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_category`
--

LOCK TABLES `sub_category` WRITE;
/*!40000 ALTER TABLE `sub_category` DISABLE KEYS */;
INSERT INTO `sub_category` VALUES ('S_01','C_01','Mammal'),('S_02','C_02','Audi'),('S_03','C_02','Bike'),('S_04','C_02','BMW'),('S_05','C_02','Dodge'),('S_06','C_02','Ford'),('S_07','C_02','Hyundai'),('S_08','C_02','Jeep'),('S_09','C_02','Lamborghini'),('S_10','C_02','Landrover'),('S_11','C_02','Mercedes'),('S_12','C_02','Part'),('S_13','C_02','Porche'),('S_14','C_02','Volkswagen'),('S_15','C_03','Predator'),('S_16','C_04','Accessories'),('S_17','C_04','Appliance'),('S_18','C_04','Battery'),('S_19','C_04','Gaming'),('S_20','C_04','Light'),('S_21','C_04','Storage');
/*!40000 ALTER TABLE `sub_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `test` (
  `category_id` varchar(45) NOT NULL,
  `category_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES ('C_01','Animal');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `texture`
--

DROP TABLE IF EXISTS `texture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `texture` (
  `texture_id` varchar(45) NOT NULL,
  `texture_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`texture_id`),
  UNIQUE KEY `texture_name_UNIQUE` (`texture_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `texture`
--

LOCK TABLES `texture` WRITE;
/*!40000 ALTER TABLE `texture` DISABLE KEYS */;
INSERT INTO `texture` VALUES ('t_01','black'),('t_02','white');
/*!40000 ALTER TABLE `texture` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-23 15:37:00
