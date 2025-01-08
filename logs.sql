-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 07, 2020 at 03:40 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hosfw`
--

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `logID` int(11) NOT NULL COMMENT 'Unique Log ID',
  `startAccessTime` datetime NOT NULL COMMENT 'Date and Time of which of which log was created',
  `endAccessTime` datetime NOT NULL COMMENT 'the end of the access',
  `employeeID` int(11) NOT NULL COMMENT 'Staff unique ID',
  `patientID` int(11) NOT NULL,
  `activityID` int(11) NOT NULL COMMENT 'The output-related data (''activities'' ID) refer to contacts between patients and the health care system, and to the treatment thereby received. Data are available for hospital discharges of in-patients and day cases, average length of stay of in-patients and medical procedures performed in hospitals',
  `ipAddress` varchar(20) NOT NULL COMMENT 'The device IP Address used to access the records',
  `employeeDepartmentID` int(11) NOT NULL COMMENT 'The department of the healthcare staff',
  `employeeOrganizationID` int(11) NOT NULL COMMENT 'the organizations/hospital of the employee',
  `patientDepartmentID` int(11) NOT NULL COMMENT 'The department which the patient was assigned to',
  `osID` int(11) NOT NULL COMMENT 'The operating system of the device used to access the record',
  `deviceID` int(11) NOT NULL COMMENT 'mac addresses',
  `browserID` int(11) NOT NULL COMMENT 'Type of browser used',
  `roleID` int(11) NOT NULL COMMENT 'Role of the user',
  `ReasonID` int(11) NOT NULL COMMENT 'Reason for some kind of accesses eg, self-authorization',
  `shiftID` int(11) NOT NULL COMMENT 'ID of a shift of a user',
  `siftStartDateTime` datetime NOT NULL,
  `siftEndDateTime` datetime NOT NULL,
  `CRUD` varchar(10) NOT NULL COMMENT 'Create, Read, Update and Delete activities of a user',
  `AccessControlStatus` int(11) NOT NULL COMMENT 'Login,Logout,FailedLogin',
  `SessionID` int(11) NOT NULL COMMENT 'Access Section ID',
  `AccessPatient_Warnings` int(11) NOT NULL COMMENT 'Access patient with warnings is triggered when a user attempts to access patient where an explicit  or implicit relationship with patient does not exists',
  `ModuleUsed` int(11) NOT NULL COMMENT 'This refered to the application module which was used eg, phamacy, radiology, prescrption, finanace etc'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`logID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `logID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Unique Log ID';
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
