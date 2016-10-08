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
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `phone` varchar(64) NOT NULL,
  `id` varchar(64) NOT NULL,
  `user_id` int(11) NOT NULL,
  `birthday` date NOT NULL,
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
INSERT INTO `accounts_userprofile` VALUES ('515-223-4444','2829f38e-f833-4c90-9b98-60b794f7376c',2,'1988-10-07'),('(416)-222-3333','5c0b044f-545a-490f-9801-eb395c3a6997',8,'1978-12-03');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add captcha store',7,'add_captchastore'),(20,'Can change captcha store',7,'change_captchastore'),(21,'Can delete captcha store',7,'delete_captchastore'),(22,'Can add user profile',8,'add_userprofile'),(23,'Can change user profile',8,'change_userprofile'),(24,'Can delete user profile',8,'delete_userprofile'),(25,'Can add team',9,'add_team'),(26,'Can change team',9,'change_team'),(27,'Can delete team',9,'delete_team'),(28,'Can add team history',10,'add_teamhistory'),(29,'Can change team history',10,'change_teamhistory'),(30,'Can delete team history',10,'delete_teamhistory'),(31,'Can add abstract player',11,'add_abstractplayer'),(32,'Can change abstract player',11,'change_abstractplayer'),(33,'Can delete abstract player',11,'delete_abstractplayer'),(34,'Can add player history',12,'add_playerhistory'),(35,'Can change player history',12,'change_playerhistory'),(36,'Can delete player history',12,'delete_playerhistory'),(37,'Can add player',13,'add_player'),(38,'Can change player',13,'change_player'),(39,'Can delete player',13,'delete_player');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$KhacFfsGkGpB$oYqsABgoPdxvkBqy0eY/UnI0AzVUymzFg3ZNh6oWh0g=','2016-10-07 20:24:48',1,'admin','','','admin@abc.ca',1,1,'2016-10-05 19:55:59'),(2,'pbkdf2_sha256$30000$DtzTWTpdl2w6$22uptLPUgHZtaV2LJ5Gk2cjEf+wr7hIkgEQA97wjADw=','2016-10-07 22:27:40',0,'dave','','','dave@an.cn',0,1,'2016-10-05 20:35:54'),(8,'pbkdf2_sha256$30000$iUK2QmoE7TGt$QBCzSymKwJclglXIMNPyeX6WdGdrd+XwqgCM8dP62yI=','2016-10-07 22:27:55',0,'rogan','rogan','Li','rogan@abc.com',0,1,'2016-10-07 22:16:37');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (5,'DWYU','dwyu','adc537b91972bcfe7d742c0a19d74e296e06da94','2016-10-07 22:28:04');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-10-07 20:27:06','2','dave',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',3,1),(2,'2016-10-07 22:15:33','2','dave',2,'[{\"added\": {\"object\": \"dave\", \"name\": \"user profile\"}}]',3,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'accounts','userprofile'),(1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(7,'captcha','captchastore'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(11,'team','abstractplayer'),(13,'team','player'),(12,'team','playerhistory'),(9,'team','team'),(10,'team','teamhistory');
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-10-05 19:55:22'),(2,'auth','0001_initial','2016-10-05 19:55:22'),(3,'accounts','0001_initial','2016-10-05 19:55:23'),(4,'admin','0001_initial','2016-10-05 19:55:23'),(5,'admin','0002_logentry_remove_auto_add','2016-10-05 19:55:23'),(6,'contenttypes','0002_remove_content_type_name','2016-10-05 19:55:23'),(7,'auth','0002_alter_permission_name_max_length','2016-10-05 19:55:23'),(8,'auth','0003_alter_user_email_max_length','2016-10-05 19:55:23'),(9,'auth','0004_alter_user_username_opts','2016-10-05 19:55:23'),(10,'auth','0005_alter_user_last_login_null','2016-10-05 19:55:23'),(11,'auth','0006_require_contenttypes_0002','2016-10-05 19:55:23'),(12,'auth','0007_alter_validators_add_error_messages','2016-10-05 19:55:23'),(13,'auth','0008_alter_user_username_max_length','2016-10-05 19:55:23'),(14,'captcha','0001_initial','2016-10-05 19:55:23'),(15,'sessions','0001_initial','2016-10-05 19:55:23'),(16,'team','0001_initial','2016-10-05 19:55:23'),(17,'accounts','0002_auto_20161007_1752','2016-10-07 21:52:19'),(18,'team','0002_auto_20161007_1752','2016-10-07 21:52:19');
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
INSERT INTO `django_session` VALUES ('36puttto2vxy45bhvwmsq9m229u53sbc','NDlmOGZlMTFjODlmZTYyYWFmODFkZmEwMWZiZGZmZjJmMDk3OWJiMzp7fQ==','2016-10-21 20:27:19'),('g2cud7w64dkqpae5sqvhw9ukw6h6cjhv','OWQwZjM3M2JhZTZkMzgwMWQ0MWM1NTk0N2UzNDg1MjljNjVhM2Q1NTp7Il9hdXRoX3VzZXJfaGFzaCI6ImU5ZjcxYzg4NTJlNzMwMmMwYzBlYjYwOTU4YzU1NTQ0MDU2MTNlZjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-10-21 20:24:48'),('o0sofvxzmvvntwlvizxd3zo1uh1ujq4u','NDlmOGZlMTFjODlmZTYyYWFmODFkZmEwMWZiZGZmZjJmMDk3OWJiMzp7fQ==','2016-10-21 22:26:27'),('ob80bbdngsagztcra69rm4kcc6n0okgu','NDlmOGZlMTFjODlmZTYyYWFmODFkZmEwMWZiZGZmZjJmMDk3OWJiMzp7fQ==','2016-10-21 20:30:59');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_abstractplayer`
--

DROP TABLE IF EXISTS `team_abstractplayer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_abstractplayer` (
  `id` varchar(64) NOT NULL,
  `is_captain` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `team_abstractplayer_user_id_2d9111a9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_abstractplayer`
--

LOCK TABLES `team_abstractplayer` WRITE;
/*!40000 ALTER TABLE `team_abstractplayer` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_abstractplayer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_player`
--

DROP TABLE IF EXISTS `team_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_player` (
  `abstractplayer_ptr_id` varchar(64) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  `team_id` varchar(64) NOT NULL,
  PRIMARY KEY (`abstractplayer_ptr_id`),
  KEY `team_player_team_id_031b9c1d_fk_team_team_id` (`team_id`),
  CONSTRAINT `team_player_team_id_031b9c1d_fk_team_team_id` FOREIGN KEY (`team_id`) REFERENCES `team_team` (`id`),
  CONSTRAINT `team_pl_abstractplayer_ptr_id_7ca20fed_fk_team_abstractplayer_id` FOREIGN KEY (`abstractplayer_ptr_id`) REFERENCES `team_abstractplayer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_player`
--

LOCK TABLES `team_player` WRITE;
/*!40000 ALTER TABLE `team_player` DISABLE KEYS */;
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
  `team_id` varchar(64) NOT NULL,
  `team_history_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `team_playerhistory_team_id_cf9b6d11_fk_team_team_id` (`team_id`),
  KEY `team_playerhisto_team_history_id_844feb09_fk_team_teamhistory_id` (`team_history_id`),
  CONSTRAINT `team_playerhistory_team_id_cf9b6d11_fk_team_team_id` FOREIGN KEY (`team_id`) REFERENCES `team_team` (`id`),
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
  PRIMARY KEY (`id`),
  KEY `team_teamhistory_team_id_475cd637_fk_team_team_id` (`team_id`),
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

-- Dump completed on 2016-10-08  9:17:11
