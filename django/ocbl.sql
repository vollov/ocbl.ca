-- MySQL dump 10.13  Distrib 5.5.51, for Win64 (x86)
--
-- Host: localhost    Database: ocbl
-- ------------------------------------------------------
-- Server version	5.5.51

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `ocbl`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ocbl` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `ocbl`;

--
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `phone` varchar(64) NOT NULL,
  `birthday` date NOT NULL,
  `id` varchar(64) NOT NULL,
  `user_id` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_userprofile_user_id_92240672_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

LOCK TABLES `accounts_userprofile` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES ('519-555-6677','1975-10-13','4eeadbb6-c1e4-4ac3-823d-0ac3596341f1',2,0),('461-222-3333','1979-04-28','4fe008c8-6c66-41e9-8f0b-a1308b958e1d',9,176),('416-333-4444','1977-10-03','d04b73f5-4c0a-441c-a631-6ae3c8433cde',8,0);
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (3,'captain'),(1,'member'),(2,'player');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,8),(2,1,23),(3,2,8),(5,2,23),(4,2,26),(6,3,7),(7,3,8),(8,3,22),(9,3,23),(10,3,25),(11,3,26),(12,3,29);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add captcha store',7,'add_captchastore'),(20,'Can change captcha store',7,'change_captchastore'),(21,'Can delete captcha store',7,'delete_captchastore'),(22,'Can add user profile',8,'add_userprofile'),(23,'Can change user profile',8,'change_userprofile'),(24,'Can delete user profile',8,'delete_userprofile'),(25,'Can add player',9,'add_player'),(26,'Can change player',9,'change_player'),(27,'Can delete player',9,'delete_player'),(28,'Can add team',10,'add_team'),(29,'Can change team',10,'change_team'),(30,'Can delete team',10,'delete_team'),(31,'Can add player history',11,'add_playerhistory'),(32,'Can change player history',11,'change_playerhistory'),(33,'Can delete player history',11,'delete_playerhistory'),(34,'Can add team history',12,'add_teamhistory'),(35,'Can change team history',12,'change_teamhistory'),(36,'Can delete team history',12,'delete_teamhistory'),(37,'Can add team history',10,'add_teamhistory'),(38,'Can change team history',10,'change_teamhistory'),(39,'Can delete team history',10,'delete_teamhistory'),(40,'Can add team',11,'add_team'),(41,'Can change team',11,'change_team'),(42,'Can delete team',11,'delete_team'),(43,'Can add player history',12,'add_playerhistory'),(44,'Can change player history',12,'change_playerhistory'),(45,'Can delete player history',12,'delete_playerhistory'),(46,'Can add game',13,'add_game'),(47,'Can change game',13,'change_game'),(48,'Can delete game',13,'delete_game'),(49,'Can add season',14,'add_season'),(50,'Can change season',14,'change_season'),(51,'Can delete season',14,'delete_season');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$KhacFfsGkGpB$oYqsABgoPdxvkBqy0eY/UnI0AzVUymzFg3ZNh6oWh0g=','2016-10-14 19:23:49',1,'admin','','','admin@abc.ca',1,1,'2016-10-05 19:55:59'),(2,'pbkdf2_sha256$30000$DtzTWTpdl2w6$22uptLPUgHZtaV2LJ5Gk2cjEf+wr7hIkgEQA97wjADw=','2016-10-11 19:33:52',0,'dave','','','dave@an.cn',1,1,'2016-10-05 20:35:54'),(8,'pbkdf2_sha256$30000$mIatT3dIpDWK$48TfeFPr67VsHwJOjj1vksqs+cdjrrol4jS+zjBF4Ss=','2016-10-11 01:24:11',0,'rogan','rogan','Li','rogan@abc.com',0,1,'2016-10-07 22:16:37'),(9,'pbkdf2_sha256$30000$BmMMU2caLtKl$RSsZAm6AjbnFnyPwNrt5HdI125mlxCT6Gpknuzd4I68=','2016-10-11 20:22:07',0,'dustin','砥可','张','dz@abc.com',1,1,'2016-10-10 16:57:22');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,9,3);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (1,'DSHD','dshd','e624013220838d242edb8cb98b0657bc310e9a9d','2016-10-11 19:35:21'),(2,'LALT','lalt','6312c433355046a3c25754cc3f3329bf856ac0b5','2016-10-11 19:38:23'),(3,'MZZR','mzzr','20425bc7ca117c2593082a5cab226e98ef591952','2016-10-11 19:40:31'),(4,'CJAZ','cjaz','7695e8d1590923eba32d4c174dbcf72777869446','2016-10-11 19:51:12'),(5,'MZKR','mzkr','83fb4bf0e9a88542f9aed0696348689fba3e1770','2016-10-14 14:23:30'),(6,'MRFG','mrfg','562c4ccd542476a4d58a57509f0443a920e86083','2016-10-14 14:23:38'),(7,'CKCX','ckcx','c057cf2ef15fa80588844bbb8e940b7ea7842a3c','2016-10-14 14:24:22'),(8,'VTGP','vtgp','1c46f74c4079777c3cdf5fc55e5b77f5db80dc89','2016-10-14 17:31:47'),(9,'CXKX','cxkx','292caf9432c9d214acc14c2a51e210b642f1f90b','2016-10-14 17:31:49'),(10,'PPGL','ppgl','6beddabfce13219c6cab3bb0c6d979752ed6d91a','2016-10-14 17:51:33'),(11,'ZMOW','zmow','b77f9e3e04e08d115da2bee146d1dbc005cce2c7','2016-10-14 17:52:08'),(12,'NSFL','nsfl','1ad9b535e6a7e0fb078a8b39c9d8e26b4fa1ad8e','2016-10-14 17:59:50'),(13,'WMQN','wmqn','ef09058a89786ba95412dfbcb4a3f774a300aa6c','2016-10-14 18:02:46'),(14,'LXLG','lxlg','9de4742c3f3239170cedb8592c6164c33621a543','2016-10-14 18:04:11');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-10-14 19:02:54','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016 多伦多杯',1,'[{\"added\": {}}]',14,1),(2,'2016-10-14 19:25:31','4868fd40-43c0-46f2-b53f-6a919644abe0','Oakville vs Kitchener',1,'[{\"added\": {}}]',13,1),(3,'2016-10-14 19:27:50','f30cbd38-62d7-429c-8d15-44827a7c387b','Mississauga',1,'[{\"added\": {}}]',11,1),(4,'2016-10-14 19:28:20','82b8c655-7ff0-45ef-8fea-98bbe290d0ab','Milton',1,'[{\"added\": {}}]',11,1),(5,'2016-10-14 19:29:22','13f00c32-709a-4467-ad01-2bda251a7e6c','Mississauga vs Milton',1,'[{\"added\": {}}]',13,1),(6,'2016-10-14 19:30:19','c74f9d72-3896-4e77-855a-52a43fb22176','Mississauga vs Oakville',1,'[{\"added\": {}}]',13,1),(7,'2016-10-14 19:30:52','8a8eaafa-f2c3-4a27-9862-85c34281d236','Milton vs Kitchener',1,'[{\"added\": {}}]',13,1),(8,'2016-10-14 19:32:30','b93b642d-58ab-4e26-b834-461e0bff52cc','Oakville vs Milton',1,'[{\"added\": {}}]',13,1),(9,'2016-10-14 19:33:08','b4266fa9-a6a3-43c5-9972-1b0d82b33d43','Kitchener vs Mississauga',1,'[{\"added\": {}}]',13,1),(10,'2016-10-14 21:30:13','9','dustin',2,'[{\"changed\": {\"fields\": [\"birthday\", \"height\"], \"object\": \"dustin\", \"name\": \"user profile\"}}]',3,1),(11,'2016-10-14 21:34:41','ab16d571-dd94-40cb-aa96-3891df1a2ac5','dustin',2,'[{\"changed\": {\"fields\": [\"number\"]}}]',9,1),(12,'2016-10-14 21:35:36','9','dustin',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\"]}}]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'accounts','userprofile'),(1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(7,'captcha','captchastore'),(5,'contenttypes','contenttype'),(13,'game','game'),(14,'game','season'),(6,'sessions','session'),(9,'team','player'),(12,'team','playerhistory'),(11,'team','team'),(10,'team','teamhistory');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-10-11 19:09:39'),(2,'auth','0001_initial','2016-10-11 19:09:39'),(3,'accounts','0001_initial','2016-10-11 19:09:40'),(4,'admin','0001_initial','2016-10-11 19:09:40'),(5,'admin','0002_logentry_remove_auto_add','2016-10-11 19:09:40'),(6,'contenttypes','0002_remove_content_type_name','2016-10-11 19:09:40'),(7,'auth','0002_alter_permission_name_max_length','2016-10-11 19:09:40'),(8,'auth','0003_alter_user_email_max_length','2016-10-11 19:09:40'),(9,'auth','0004_alter_user_username_opts','2016-10-11 19:09:40'),(10,'auth','0005_alter_user_last_login_null','2016-10-11 19:09:40'),(11,'auth','0006_require_contenttypes_0002','2016-10-11 19:09:40'),(12,'auth','0007_alter_validators_add_error_messages','2016-10-11 19:09:40'),(13,'auth','0008_alter_user_username_max_length','2016-10-11 19:09:40'),(14,'captcha','0001_initial','2016-10-11 19:09:40'),(15,'sessions','0001_initial','2016-10-11 19:09:40'),(16,'team','0001_initial','2016-10-11 19:09:41'),(17,'team','0002_remove_player_is_captain','2016-10-11 19:09:41'),(18,'team','0003_teamhistory_captain','2016-10-11 19:09:41'),(19,'team','0004_auto_20161010_2110','2016-10-11 19:09:41'),(20,'accounts','0002_userprofile_height','2016-10-14 14:17:19'),(21,'team','0005_player_number','2016-10-14 14:17:19'),(22,'game','0001_initial','2016-10-14 18:58:17'),(23,'game','0002_auto_20161014_1523','2016-10-14 19:23:23');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6wdx1cbsv95kfb78gvkcs84p1adfd2y1','ZDBiYzU3MWFiNTc3ZWE5OGNkZjVhOGE0YTVlYzk5YTJkYzg2MTJkNTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU5ZjcxYzg4NTJlNzMwMmMwYzBlYjYwOTU4YzU1NTQ0MDU2MTNlZjMiLCJfbWVzc2FnZXMiOiJbW1wiX19qc29uX21lc3NhZ2VcIiwxLDI1LFwiVGhlIHBsYXllciBcXFwiPGEgaHJlZj1cXFwiL2FkbWluL3RlYW0vcGxheWVyL2FiMTZkNTcxLWRkOTQtNDBjYi1hYTk2LTM4OTFkZjFhMmFjNS9jaGFuZ2UvXFxcIj5kdXN0aW48L2E+XFxcIiB3YXMgY2hhbmdlZCBzdWNjZXNzZnVsbHkuXCJdLFtcIl9fanNvbl9tZXNzYWdlXCIsMSwyNSxcIlRoZSB1c2VyIFxcXCI8YSBocmVmPVxcXCIvYWRtaW4vYXV0aC91c2VyLzkvY2hhbmdlL1xcXCI+ZHVzdGluPC9hPlxcXCIgd2FzIGNoYW5nZWQgc3VjY2Vzc2Z1bGx5LlwiXV0iLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-10-28 21:35:36');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_game`
--

DROP TABLE IF EXISTS `game_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_game` (
  `id` varchar(64) NOT NULL,
  `host_score` int(11) DEFAULT NULL,
  `guest_score` int(11) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `finished` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  `guest_id` varchar(64) NOT NULL,
  `host_id` varchar(64) NOT NULL,
  `season_id` varchar(64) NOT NULL,
  `end_time` datetime,
  `start_time` datetime,
  PRIMARY KEY (`id`),
  KEY `game_game_guest_id_f9c3eef5_fk_team_team_id` (`guest_id`),
  KEY `game_game_host_id_2542ab62_fk_team_team_id` (`host_id`),
  KEY `game_game_b11701f0` (`season_id`),
  CONSTRAINT `game_game_guest_id_f9c3eef5_fk_team_team_id` FOREIGN KEY (`guest_id`) REFERENCES `team_team` (`id`),
  CONSTRAINT `game_game_host_id_2542ab62_fk_team_team_id` FOREIGN KEY (`host_id`) REFERENCES `team_team` (`id`),
  CONSTRAINT `game_game_season_id_d9ef083f_fk_game_season_id` FOREIGN KEY (`season_id`) REFERENCES `game_season` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_game`
--

LOCK TABLES `game_game` WRITE;
/*!40000 ALTER TABLE `game_game` DISABLE KEYS */;
INSERT INTO `game_game` VALUES ('13f00c32-709a-4467-ad01-2bda251a7e6c',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:29:22','82b8c655-7ff0-45ef-8fea-98bbe290d0ab','f30cbd38-62d7-429c-8d15-44827a7c387b','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-10-23 00:30:00','2016-10-22 23:30:00'),('4868fd40-43c0-46f2-b53f-6a919644abe0',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:25:31','a3256bc3-af94-4b7d-b547-3ac4630cd8b7','51d1bad3-a4f6-4a29-a5a2-62d96491c60f','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-10-23 00:30:00','2016-10-22 23:30:00'),('8a8eaafa-f2c3-4a27-9862-85c34281d236',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:30:52','a3256bc3-af94-4b7d-b547-3ac4630cd8b7','82b8c655-7ff0-45ef-8fea-98bbe290d0ab','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-10-30 00:30:00','2016-10-29 23:30:00'),('b4266fa9-a6a3-43c5-9972-1b0d82b33d43',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:33:08','f30cbd38-62d7-429c-8d15-44827a7c387b','a3256bc3-af94-4b7d-b547-3ac4630cd8b7','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-11-06 00:30:00','2016-11-05 23:30:00'),('b93b642d-58ab-4e26-b834-461e0bff52cc',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:32:30','82b8c655-7ff0-45ef-8fea-98bbe290d0ab','51d1bad3-a4f6-4a29-a5a2-62d96491c60f','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-11-06 00:30:00','2016-11-05 23:30:00'),('c74f9d72-3896-4e77-855a-52a43fb22176',0,0,'2015 Pan Am Blvd, Milton, ON L9T 2X6',0,'2016-10-14 19:30:19','51d1bad3-a4f6-4a29-a5a2-62d96491c60f','f30cbd38-62d7-429c-8d15-44827a7c387b','a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016-10-30 00:30:00','2016-10-29 23:30:00');
/*!40000 ALTER TABLE `game_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_season`
--

DROP TABLE IF EXISTS `game_season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `game_season` (
  `id` varchar(64) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `year` varchar(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_season`
--

LOCK TABLES `game_season` WRITE;
/*!40000 ALTER TABLE `game_season` DISABLE KEYS */;
INSERT INTO `game_season` VALUES ('a8742d8d-1b5b-4742-aede-47f1eaad5eb6','2016 多伦多杯','2015 Pan Am Blvd, Milton, ON L9T 2X6','2016');
/*!40000 ALTER TABLE `game_season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_player`
--

DROP TABLE IF EXISTS `team_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_player` (
  `id` varchar(64) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  `team_id` varchar(64),
  `user_profile_id` varchar(64),
  `number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_profile_id` (`user_profile_id`),
  KEY `team_player_f6a7ca40` (`team_id`),
  CONSTRAINT `team_player_team_id_031b9c1d_fk_team_team_id` FOREIGN KEY (`team_id`) REFERENCES `team_team` (`id`),
  CONSTRAINT `team_player_user_profile_id_872d78db_fk_accounts_userprofile_id` FOREIGN KEY (`user_profile_id`) REFERENCES `accounts_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_player`
--

LOCK TABLES `team_player` WRITE;
/*!40000 ALTER TABLE `team_player` DISABLE KEYS */;
INSERT INTO `team_player` VALUES ('ab16d571-dd94-40cb-aa96-3891df1a2ac5',1,'2016-10-11 01:23:24','a3256bc3-af94-4b7d-b547-3ac4630cd8b7','4fe008c8-6c66-41e9-8f0b-a1308b958e1d',11),('eaab9c83-d7fb-4a0c-8705-01cc30c0b675',1,'2016-10-11 01:24:14','a3256bc3-af94-4b7d-b547-3ac4630cd8b7','d04b73f5-4c0a-441c-a631-6ae3c8433cde',0);
/*!40000 ALTER TABLE `team_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_playerhistory`
--

DROP TABLE IF EXISTS `team_playerhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_playerhistory` (
  `id` varchar(64) NOT NULL,
  `name` varchar(32) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `year` varchar(4) NOT NULL,
  `team_history_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `team_playerhistory_104e757d` (`team_history_id`),
  CONSTRAINT `team_playerhisto_team_history_id_844feb09_fk_team_teamhistory_id` FOREIGN KEY (`team_history_id`) REFERENCES `team_teamhistory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_playerhistory`
--

LOCK TABLES `team_playerhistory` WRITE;
/*!40000 ALTER TABLE `team_playerhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_playerhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_team`
--

DROP TABLE IF EXISTS `team_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_team` (
  `id` varchar(64) NOT NULL,
  `name` varchar(32) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_team`
--

LOCK TABLES `team_team` WRITE;
/*!40000 ALTER TABLE `team_team` DISABLE KEYS */;
INSERT INTO `team_team` VALUES ('51d1bad3-a4f6-4a29-a5a2-62d96491c60f','Oakville','Oakville',1,'2016-10-08 15:20:30'),('82b8c655-7ff0-45ef-8fea-98bbe290d0ab','Milton','Milton',1,'2016-10-14 19:28:20'),('a3256bc3-af94-4b7d-b547-3ac4630cd8b7','Kitchener','Kitchener',1,'2016-10-08 15:20:12'),('f30cbd38-62d7-429c-8d15-44827a7c387b','Mississauga','Mississauga',1,'2016-10-14 19:27:50');
/*!40000 ALTER TABLE `team_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_teamhistory`
--

DROP TABLE IF EXISTS `team_teamhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_teamhistory` (
  `id` varchar(64) NOT NULL,
  `name` varchar(32) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `year` varchar(4) NOT NULL,
  `team_id` varchar(64) NOT NULL,
  `captain_id` int(11),
  PRIMARY KEY (`id`),
  KEY `team_teamhistory_team_id_475cd637_fk_team_team_id` (`team_id`),
  KEY `team_teamhistory_8f300ce6` (`captain_id`),
  CONSTRAINT `team_teamhistory_captain_id_572f45a5_fk_auth_user_id` FOREIGN KEY (`captain_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `team_teamhistory_team_id_475cd637_fk_team_team_id` FOREIGN KEY (`team_id`) REFERENCES `team_team` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_teamhistory`
--

LOCK TABLES `team_teamhistory` WRITE;
/*!40000 ALTER TABLE `team_teamhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_teamhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-14 17:47:21
