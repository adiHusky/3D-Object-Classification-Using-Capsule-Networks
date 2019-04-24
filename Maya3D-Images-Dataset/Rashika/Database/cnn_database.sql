-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 22, 2019 at 02:20 AM
-- Server version: 5.7.24-log
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cnn_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `background`
--

CREATE TABLE `background` (
  `background_id` varchar(100) NOT NULL,
  `background_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `background`
--

INSERT INTO `background` (`background_id`, `background_name`) VALUES
('bk_1', 'white'),
('bk_2', 'black');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` varchar(100) NOT NULL,
  `category_name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`) VALUES
('cat_1', 'car'),
('cat_2', 'animals');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `image_id` varchar(100) NOT NULL,
  `image_name` varchar(200) NOT NULL,
  `image_size` varchar(400) NOT NULL,
  `image_resolution` varchar(400) NOT NULL,
  `image_type` varchar(400) NOT NULL,
  `image_path` varchar(200) NOT NULL,
  `X` int(20) NOT NULL,
  `Y` int(20) NOT NULL,
  `Z` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`image_id`, `image_name`, `image_size`, `image_resolution`, `image_type`, `image_path`, `X`, `Y`, `Z`) VALUES
('img_1', 'category1_subcat1_objectname1_X0_Y0_Z0_Yes.jpg', '5616\r\n', '(194, 259, 3)\r\n', 'uint8\r\n', 'category1_subcat1_objectname1_X0_Y0_Z0_Yes.jpg\r\n', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `object`
--

CREATE TABLE `object` (
  `object_id` varchar(100) NOT NULL,
  `object_name` varchar(200) NOT NULL,
  `subcategory_id` varchar(100) NOT NULL,
  `texture_id` varchar(100) NOT NULL,
  `background_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `object`
--

INSERT INTO `object` (`object_id`, `object_name`, `subcategory_id`, `texture_id`, `background_id`) VALUES
('obj_1', 'AudiA4', 'subcat_1', 'text_1', 'bk_2'),
('obj_2', 'AudiA8', 'subcat_1', 'text_1', 'bk_2');

-- --------------------------------------------------------

--
-- Table structure for table `object_image_junction`
--

CREATE TABLE `object_image_junction` (
  `object_id` varchar(100) NOT NULL,
  `image_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `object_image_junction`
--

INSERT INTO `object_image_junction` (`object_id`, `image_id`) VALUES
('obj_1', 'img_1');

-- --------------------------------------------------------

--
-- Table structure for table `sub_category`
--

CREATE TABLE `sub_category` (
  `subcategory_id` varchar(100) NOT NULL,
  `subcategory_name` varchar(100) NOT NULL,
  `category_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sub_category`
--

INSERT INTO `sub_category` (`subcategory_id`, `subcategory_name`, `category_id`) VALUES
('subcat_1', 'audi', 'cat_1'),
('subcat_2', 'hyundai', 'cat_1');

-- --------------------------------------------------------

--
-- Table structure for table `texture`
--

CREATE TABLE `texture` (
  `texture_id` varchar(100) NOT NULL,
  `texture_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `texture`
--

INSERT INTO `texture` (`texture_id`, `texture_name`) VALUES
('text_1', 'white'),
('text_2', 'black');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
