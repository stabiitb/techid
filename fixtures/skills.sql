-- phpMyAdmin SQL Dump
-- version 2.11.11.3
-- http://www.phpmyadmin.net
--
-- Host: 182.50.133.48
-- Generation Time: Dec 30, 2013 at 07:52 PM
-- Server version: 5.0.96
-- PHP Version: 5.1.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `techid`
--

-- --------------------------------------------------------

--
-- Table structure for table `techid_skills`
--

CREATE TABLE `techid_skills` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(255) NOT NULL,
  `tagname` varchar(255) NOT NULL,
  `desc` text NOT NULL,
  `category` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `techid_skills`
--

INSERT INTO `techid_skills` VALUES(1, 'Solid works', 'solid-works', '', 1);
INSERT INTO `techid_skills` VALUES(2, 'CAD & Ansys', 'cad', '', 1);
INSERT INTO `techid_skills` VALUES(3, 'Matlab', 'matlab', '', 1);
INSERT INTO `techid_skills` VALUES(4, 'Simulink', 'simulink', '', 1);
INSERT INTO `techid_skills` VALUES(5, 'Eagle', 'eagle', '', 1);
INSERT INTO `techid_skills` VALUES(6, 'Kicad', 'kicad', '', 1);
INSERT INTO `techid_skills` VALUES(7, 'Ltspice', 'ltspice', '', 1);
INSERT INTO `techid_skills` VALUES(8, 'Simulation software', 'simulation-software', '', 1);
INSERT INTO `techid_skills` VALUES(9, 'Labview', 'labview', '', 1);
INSERT INTO `techid_skills` VALUES(10, 'Basic sensors (sharp, tsop, ultrasonic, ldr''s)', 'basic-sensors', '', 1);
INSERT INTO `techid_skills` VALUES(11, 'Advanced sensors (gyroscope, accelerometer, thermal, humidity, proximity, flex, megnetometer)', 'advanced-sensors', '', 1);
INSERT INTO `techid_skills` VALUES(12, 'Infra red emitters and sensors', 'infra-red-sensors', '', 1);
INSERT INTO `techid_skills` VALUES(13, 'Signal Processing', 'signal-processing', '', 1);
INSERT INTO `techid_skills` VALUES(14, 'noise filtering', 'noise-filtering', '', 1);
INSERT INTO `techid_skills` VALUES(15, 'control theory', 'control-theory', '', 1);
INSERT INTO `techid_skills` VALUES(16, 'system identification', 'system-identification', '', 1);
INSERT INTO `techid_skills` VALUES(17, 'system tuning', 'system-tuning', '', 1);
INSERT INTO `techid_skills` VALUES(18, 'Pure Mechanical knowledge (assembly, gear)', 'pure-mechanics', '', 1);
INSERT INTO `techid_skills` VALUES(19, 'Motors (servo, stepper)', 'motors', '', 1);
INSERT INTO `techid_skills` VALUES(20, 'Piston actuation', 'piston-actuation', '', 1);
INSERT INTO `techid_skills` VALUES(21, 'Shock Absorbers', 'shock-absorbers', '', 1);
INSERT INTO `techid_skills` VALUES(22, 'fabrication processing', 'fabrication-processing', '', 1);
INSERT INTO `techid_skills` VALUES(23, 'Arduino basics', 'arduino-basics', '', 1);
INSERT INTO `techid_skills` VALUES(24, 'Arduino advanced (serial communication - SPI, uart, usart coding, timers )', 'arduino-advanced', '', 1);
INSERT INTO `techid_skills` VALUES(25, 'Avr coding (basic)', 'avr-coding-basic', '', 1);
INSERT INTO `techid_skills` VALUES(26, 'Avr coding (advanced)', 'avr-coding-advanced', '', 1);
INSERT INTO `techid_skills` VALUES(27, 'Processing software', 'processing-software', '', 1);
INSERT INTO `techid_skills` VALUES(28, 'Wireless communication modules (xbee, Bluetooth, manipulating electro magnetic fields)', 'wireless-communication', '', 1);
INSERT INTO `techid_skills` VALUES(29, 'Image processing (visual studio, open cv, processing)', 'image-processing', '', 1);
INSERT INTO `techid_skills` VALUES(30, 'Digital Signal Processing tools', 'digital-signal-processing', '', 1);
INSERT INTO `techid_skills` VALUES(31, 'FPGA related coding', 'FPGA-coding', '', 1);
INSERT INTO `techid_skills` VALUES(32, 'High power electrical applications', 'high-power-electronics', '', 1);
INSERT INTO `techid_skills` VALUES(33, 'HTML', 'html', '', 1);
INSERT INTO `techid_skills` VALUES(34, 'C/C++', 'C/C++', '', 1);
INSERT INTO `techid_skills` VALUES(35, 'Python', 'python', '', 1);
INSERT INTO `techid_skills` VALUES(36, 'Java', 'java', '', 1);
INSERT INTO `techid_skills` VALUES(37, 'CSS', 'css', '', 1);
INSERT INTO `techid_skills` VALUES(38, 'PHP', 'php', '', 1);
INSERT INTO `techid_skills` VALUES(39, 'MySQL', 'mysql', '', 1);
INSERT INTO `techid_skills` VALUES(40, 'Javascript', 'javascript', '', 1);
INSERT INTO `techid_skills` VALUES(41, 'Android', 'android', '', 1);
INSERT INTO `techid_skills` VALUES(42, 'Ruby on Rails', 'RoR', '', 1);
INSERT INTO `techid_skills` VALUES(43, 'iPhone programming', 'iphone-programming', '', 1);
INSERT INTO `techid_skills` VALUES(44, 'Telescope handling', 'telescope-handling', '', 1);
INSERT INTO `techid_skills` VALUES(45, 'Observational Astronomy', 'observational-astronomy', '', 1);
INSERT INTO `techid_skills` VALUES(46, 'Flying aeroplane', 'flying-airplane', '', 1);
INSERT INTO `techid_skills` VALUES(47, 'Board Games( Chess,checkers.go,etc.)', 'board-games', '', 1);
INSERT INTO `techid_skills` VALUES(48, 'Sudoku', 'sudoku', '', 1);
