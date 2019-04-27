-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 27, 2019 at 01:23 AM
-- Server version: 5.7.25
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `images`
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
('cat_animals', 'Animals'),
('cat_automobile', 'Automobiles'),
('cat_bird', 'Birds'),
('cat_electronics', 'Electronics'),
('cat_fashion', 'Fashion'),
('cat_food', 'Food'),
('cat_footwear', 'Footwear'),
('cat_household', 'Household'),
('cat_humanbody', 'Humanbody'),
('cat_monuments', 'Monuments'),
('cat_nature', 'Nature'),
('cat_sports', 'Sports'),
('cat_weapon', 'Weapon');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `X` int(20) NOT NULL,
  `Y` int(20) NOT NULL,
  `Z` int(20) NOT NULL,
  `image_id` varchar(100) NOT NULL,
  `image_name` varchar(200) NOT NULL,
  `image_resolution` varchar(400) NOT NULL,
  `image_size` varchar(400) NOT NULL,
  `image_type` varchar(400) NOT NULL,
  `image` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`X`, `Y`, `Z`, `image_id`, `image_name`, `image_resolution`, `image_size`, `image_type`, `image`) VALUES
(0, 0, 0, 'img_1', 'category1_subcat1_objectname1_X0_Y0_Z0_Yes.jpg', '(194, 259, 3)\r\n', '5616\r\n', 'uint8\r\n', 0x63617465676f7279315f737562636174315f6f626a6563746e616d65315f58305f59305f5a305f5965732e6a70670d0a);

-- --------------------------------------------------------

--
-- Table structure for table `object`
--

CREATE TABLE `object` (
  `object_id` varchar(100) NOT NULL,
  `object_name` varchar(200) NOT NULL,
  `subcategory_id` varchar(100) NOT NULL,
  `texture_id` varchar(100) NOT NULL,
  `background_id` varchar(100) NOT NULL,
  `object_image` blob NOT NULL,
  `shadow_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
-- Table structure for table `shadow`
--

CREATE TABLE `shadow` (
  `shadow_id` varchar(10) NOT NULL,
  `shadow_presence` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `sub_category`
--

CREATE TABLE `sub_category` (
  `subcategory_id` varchar(100) NOT NULL,
  `subcategory_name` varchar(100) NOT NULL,
  `category_id` varchar(100) NOT NULL,
  `subcategory_image` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sub_category`
--

INSERT INTO `sub_category` (`subcategory_id`, `subcategory_name`, `category_id`, `subcategory_image`) VALUES
('bcat_mam', 'Mammal', 'cat_animals', 0x622761673d3d27),
('subcat_audi', 'Audi', 'cat_automobile', 0x622761673d3d27),
('subcat_bike', 'Bike', 'cat_automobile', 0x622761673d3d27),
('subcat_bmw', 'BMW', 'cat_automobile', 0x622761673d3d27),
('subcat_dodge', 'Dodge', 'cat_automobile', 0x622761673d3d27),
('subcat_ford', 'Ford', 'cat_automobile', 0x622761673d3d27),
('subcat_hyundai', 'Hyundai', 'cat_automobile', 0x622761673d3d27),
('subcat_jeep', 'Jeep', 'cat_automobile', 0x622761673d3d27),
('subcat_lamborghini', 'Lamborghini', 'cat_automobile', 0x622761673d3d27),
('subcat_landrover', 'Land Rover', 'cat_automobile', 0x622761673d3d27),
('subcat_mercedes', 'Mercedes', 'cat_automobile', 0x622761673d3d27),
('subcat_parts', 'Part', 'cat_automobile', 0x622761673d3d27),
('subcat_porsche', 'Porsche', 'cat_automobile', 0x622761673d3d27),
('subcat_predator', 'Predator', 'cat_bird', 0x622761673d3d27),
('subcat_volkswagen', 'Volkswagen', 'cat_automobile', 0x622761673d3d27);

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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `background`
--
ALTER TABLE `background`
  ADD PRIMARY KEY (`background_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`image_id`);

--
-- Indexes for table `object`
--
ALTER TABLE `object`
  ADD PRIMARY KEY (`object_id`),
  ADD KEY `background_id` (`background_id`),
  ADD KEY `texture_id` (`texture_id`),
  ADD KEY `object_ibfk_3` (`shadow_id`);

--
-- Indexes for table `object_image_junction`
--
ALTER TABLE `object_image_junction`
  ADD PRIMARY KEY (`object_id`,`image_id`);

--
-- Indexes for table `shadow`
--
ALTER TABLE `shadow`
  ADD PRIMARY KEY (`shadow_id`);

--
-- Indexes for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD PRIMARY KEY (`subcategory_id`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `texture`
--
ALTER TABLE `texture`
  ADD PRIMARY KEY (`texture_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `object`
--
ALTER TABLE `object`
  ADD CONSTRAINT `object_ibfk_1` FOREIGN KEY (`background_id`) REFERENCES `background` (`background_id`),
  ADD CONSTRAINT `object_ibfk_2` FOREIGN KEY (`texture_id`) REFERENCES `texture` (`texture_id`),
  ADD CONSTRAINT `object_ibfk_3` FOREIGN KEY (`shadow_id`) REFERENCES `shadow` (`shadow_id`);

--
-- Constraints for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD CONSTRAINT `sub_category_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`);
