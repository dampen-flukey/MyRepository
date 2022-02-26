-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 26, 2022 at 08:59 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_num` varchar(12) DEFAULT NULL,
  `msg` text DEFAULT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'first post', 'first_post@gmail.com', '123', 'first post', '2022-02-16 00:00:00'),
(25, 'Prateek', 'dm@gmil.com', '123', 'arya stark is no one', '2022-02-16 14:16:54'),
(26, 'gshd', 'a@gmail.com', '1234', 'sona', '2022-02-16 22:54:07');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` varchar(5000) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `slug` varchar(50) NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `subheading` varchar(30) DEFAULT 'Read the full article below...',
  `lower_img` varchar(25) DEFAULT 'kip.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `date`, `slug`, `img_file`, `subheading`, `lower_img`) VALUES
(1, 'Astronaut or Cosmonaut ?', '      Cosmonauts are people trained and certified by the Russian Space Agency to work in space. Astronauts are people trained and certified by NASA, ESA, CSA, or JAXA to work in space. Read Wikipedia for more info!!!!!   ', '2022-02-24', 'first-post', 'post-bg.jpg', 'Read the full article below...', 'post-sample-image.jpg'),
(2, 'Falcon Heavy', '     Falcon Heavy is a partially reusable heavy-lift launch vehicle designed and manufactured by SpaceX. It is derived from the Falcon 9 vehicle and consists of a strengthened Falcon 9 first stage as the center core with two additional Falcon 9 first stages serving as strap-on boosters.[8] Falcon Heavy has the highest payload capacity of any currently operational launch vehicle and the third-highest capacity of any rocket ever to reach orbit, trailing the Saturn V and Energia.     ', '2022-02-24', 'second-post', 'Falcon_Heavy.jpg', 'Read the full article below...', 'FH_Side_Boosters.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
