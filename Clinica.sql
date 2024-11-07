-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: seprice
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'Profesional'),(1,'Recepcionista');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (9,1,21),(10,1,22),(11,1,23),(12,1,24),(15,1,34),(16,1,36),(19,1,49),(20,1,50),(21,1,52),(22,1,53),(23,1,54),(24,1,55),(25,1,56),(26,1,57),(27,1,58),(28,1,60),(29,1,61),(30,1,64),(32,1,73),(33,1,74),(34,1,75),(35,1,76),(36,1,77),(37,1,78),(38,1,79),(39,1,80),(40,1,81),(41,1,82),(42,1,83),(43,1,84),(49,2,29),(50,2,30),(51,2,31),(52,2,32),(59,2,50),(65,2,69),(66,2,70),(67,2,71),(68,2,72),(69,2,74),(70,2,75),(71,2,76);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add especialidades',7,'add_especialidades'),(26,'Can change especialidades',7,'change_especialidades'),(27,'Can delete especialidades',7,'delete_especialidades'),(28,'Can view especialidades',7,'view_especialidades'),(29,'Can add historia clinica',8,'add_historiaclinica'),(30,'Can change historia clinica',8,'change_historiaclinica'),(31,'Can delete historia clinica',8,'delete_historiaclinica'),(32,'Can view historia clinica',8,'view_historiaclinica'),(33,'Can add insumos',9,'add_insumos'),(34,'Can change insumos',9,'change_insumos'),(35,'Can delete insumos',9,'delete_insumos'),(36,'Can view insumos',9,'view_insumos'),(37,'Can add proveedores seguros',10,'add_proveedoresseguros'),(38,'Can change proveedores seguros',10,'change_proveedoresseguros'),(39,'Can delete proveedores seguros',10,'delete_proveedoresseguros'),(40,'Can view proveedores seguros',10,'view_proveedoresseguros'),(41,'Can add admin',11,'add_admin'),(42,'Can change admin',11,'change_admin'),(43,'Can delete admin',11,'delete_admin'),(44,'Can view admin',11,'view_admin'),(45,'Can add estudios',12,'add_estudios'),(46,'Can change estudios',12,'change_estudios'),(47,'Can delete estudios',12,'delete_estudios'),(48,'Can view estudios',12,'view_estudios'),(49,'Can add paciente',13,'add_paciente'),(50,'Can change paciente',13,'change_paciente'),(51,'Can delete paciente',13,'delete_paciente'),(52,'Can view paciente',13,'view_paciente'),(53,'Can add ingreso paciente',14,'add_ingresopaciente'),(54,'Can change ingreso paciente',14,'change_ingresopaciente'),(55,'Can delete ingreso paciente',14,'delete_ingresopaciente'),(56,'Can view ingreso paciente',14,'view_ingresopaciente'),(57,'Can add pagos',15,'add_pagos'),(58,'Can change pagos',15,'change_pagos'),(59,'Can delete pagos',15,'delete_pagos'),(60,'Can view pagos',15,'view_pagos'),(61,'Can add facturas',16,'add_facturas'),(62,'Can change facturas',16,'change_facturas'),(63,'Can delete facturas',16,'delete_facturas'),(64,'Can view facturas',16,'view_facturas'),(65,'Can add profesionales',17,'add_profesionales'),(66,'Can change profesionales',17,'change_profesionales'),(67,'Can delete profesionales',17,'delete_profesionales'),(68,'Can view profesionales',17,'view_profesionales'),(69,'Can add resultado laboratorio',18,'add_resultadolaboratorio'),(70,'Can change resultado laboratorio',18,'change_resultadolaboratorio'),(71,'Can delete resultado laboratorio',18,'delete_resultadolaboratorio'),(72,'Can view resultado laboratorio',18,'view_resultadolaboratorio'),(73,'Can add Sala de Espera',19,'add_salaespera'),(74,'Can change Sala de Espera',19,'change_salaespera'),(75,'Can delete Sala de Espera',19,'delete_salaespera'),(76,'Can view Sala de Espera',19,'view_salaespera'),(77,'Can add solicitudes insumos',20,'add_solicitudesinsumos'),(78,'Can change solicitudes insumos',20,'change_solicitudesinsumos'),(79,'Can delete solicitudes insumos',20,'delete_solicitudesinsumos'),(80,'Can view solicitudes insumos',20,'view_solicitudesinsumos'),(81,'Can add turnos',21,'add_turnos'),(82,'Can change turnos',21,'change_turnos'),(83,'Can delete turnos',21,'delete_turnos'),(84,'Can view turnos',21,'view_turnos'),(85,'Can add historia clinica detalle',22,'add_historiaclinicadetalle'),(86,'Can change historia clinica detalle',22,'change_historiaclinicadetalle'),(87,'Can delete historia clinica detalle',22,'delete_historiaclinicadetalle'),(88,'Can view historia clinica detalle',22,'view_historiaclinicadetalle');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$wvHYET9hUFrms5HxaNRilU$AVowh/O1S8DYb2ErryRIk1trh4qRb5kca8A+pWZ6zOI=','2024-11-07 11:59:55.839813',1,'admin','','','',1,1,'2024-11-06 03:38:20.386991'),(2,'pbkdf2_sha256$870000$dmBCwRqx85fBtc8viuDwTa$llMjqHwUEZpRChRaTYccrA4g/sbMRteU+zSR8bHqG80=','2024-11-06 21:29:59.102132',0,'Veronica','Verónica','Hassen','veronicahassen@gmail.com',1,1,'2024-11-06 11:29:54.000000'),(3,'pbkdf2_sha256$870000$qw9V3J8bqTf3rEyS35EwHw$LeWkhyRopU9CY+ghcDT1FVFxV7WVYSv9VFw7IAKA0dw=',NULL,0,'Daniela','Daniela','Homobono','danih@ejemplo.com',1,1,'2024-11-06 11:30:34.000000'),(4,'pbkdf2_sha256$870000$D9PjfgELcp6teiHSIx9Ejm$JZZUrlYzNQbEPyfjfVpmZAMVlH3Wh581yqGpV4CtrUI=','2024-11-07 11:55:00.137644',0,'Romina','Romina','Zagordo','romaz@ejemplo.com',1,1,'2024-11-06 11:31:04.000000'),(5,'pbkdf2_sha256$870000$3aiRXczqwtSbT9H1RwXDT7$QK+RPiZ8ciXMJ+BCVCA3kHzHD9x7g7iDTyANFyJb5ZM=',NULL,0,'Emira','Emira','Toranzo','emirat@ejemplo.com',1,1,'2024-11-06 11:31:24.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,1),(5,4,2),(3,5,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_admin`
--

DROP TABLE IF EXISTS `coreadmin_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `admin_password` varchar(100) NOT NULL,
  `admin_dni` varchar(8) NOT NULL,
  `admin_telefono` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `time` time(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `admin_dni` (`admin_dni`),
  UNIQUE KEY `coreadmin_admin_date_joined_time_06b2753d_uniq` (`date_joined`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_admin`
--

LOCK TABLES `coreadmin_admin` WRITE;
/*!40000 ALTER TABLE `coreadmin_admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `coreadmin_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_especialidades`
--

DROP TABLE IF EXISTS `coreadmin_especialidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_especialidades` (
  `especialidad_id` int NOT NULL AUTO_INCREMENT,
  `especialidad_nombre` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`especialidad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_especialidades`
--

LOCK TABLES `coreadmin_especialidades` WRITE;
/*!40000 ALTER TABLE `coreadmin_especialidades` DISABLE KEYS */;
INSERT INTO `coreadmin_especialidades` VALUES (1,'Cardiología','2024-11-06 03:42:50.908595','2024-11-06 03:42:50.908620'),(2,'Endocrinología','2024-11-06 03:42:57.057361','2024-11-06 03:42:57.057393'),(3,'Ginecología','2024-11-06 03:43:01.857286','2024-11-06 03:43:01.857310'),(4,'Laboratorio','2024-11-06 03:43:06.891584','2024-11-06 03:43:06.891635'),(5,'Traumatología','2024-11-06 11:48:49.267473','2024-11-06 11:48:49.267502'),(6,'Pediatría','2024-11-06 11:48:54.106411','2024-11-06 11:48:54.106446'),(8,'Neurología','2024-11-06 11:49:05.811127','2024-11-06 11:49:05.811153'),(9,'Dermatología','2024-11-06 11:49:16.325711','2024-11-06 11:49:16.325739'),(10,'Obstetricia','2024-11-06 11:49:26.966316','2024-11-06 11:49:26.966342'),(11,'Neonatología','2024-11-06 21:26:31.058719','2024-11-06 21:26:31.058755');
/*!40000 ALTER TABLE `coreadmin_especialidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_estudios`
--

DROP TABLE IF EXISTS `coreadmin_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_estudios` (
  `estudio_id` int NOT NULL AUTO_INCREMENT,
  `estudio_nombre` varchar(50) NOT NULL,
  `estudio_descripcion` varchar(100) NOT NULL,
  `estudio_precio` decimal(10,2) NOT NULL,
  `app_total` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `especialidad_id` int NOT NULL,
  `profesional_id` int NOT NULL,
  PRIMARY KEY (`estudio_id`),
  KEY `coreadmin_estudios_profesional_id_0a04f64c_fk_coreadmin` (`profesional_id`),
  KEY `coreadmin_estudios_especialidad_id_f4bfca2c_fk_coreadmin` (`especialidad_id`),
  CONSTRAINT `coreadmin_estudios_especialidad_id_f4bfca2c_fk_coreadmin` FOREIGN KEY (`especialidad_id`) REFERENCES `coreadmin_especialidades` (`especialidad_id`),
  CONSTRAINT `coreadmin_estudios_profesional_id_0a04f64c_fk_coreadmin` FOREIGN KEY (`profesional_id`) REFERENCES `coreadmin_profesionales` (`profesional_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_estudios`
--

LOCK TABLES `coreadmin_estudios` WRITE;
/*!40000 ALTER TABLE `coreadmin_estudios` DISABLE KEYS */;
INSERT INTO `coreadmin_estudios` VALUES (1,'EcoDoppler','Estudio para controlar el estado cardíaco',5000.00,0,'2024-11-06 03:44:43.983722','2024-11-06 03:44:43.983765',1,1),(2,'Angiografía Coronaria','Imagen de los vasos sanguíneos del corazón para detectar obstrucciones.',15000.00,0,'2024-11-06 13:51:26.250906','2024-11-06 14:02:59.909963',1,1),(3,'Biopsia de piel','Extracción de una muestra de piel para análisis.',4999.99,0,'2024-11-06 14:01:51.463583','2024-11-06 14:01:51.463608',9,4),(4,'Terapia con láser','Tratamiento de lesiones cutáneas con láser.',25000.00,0,'2024-11-06 14:04:07.558507','2024-11-06 14:04:07.558544',9,4),(5,'Medición de Hormonas Tiroideas','Análisis de niveles de hormonas tiroideas en sangre.',2000.00,0,'2024-11-06 14:04:54.276223','2024-11-06 14:04:54.276246',2,11),(6,'Papanicolaou (PAP)','Prueba de detección de cáncer de cuello uterino.',25000.00,0,'2024-11-06 14:05:45.685839','2024-11-06 14:05:45.685866',3,9),(7,'Abc','Abc2',15000.00,0,'2024-11-06 21:28:17.762086','2024-11-06 21:28:17.762125',11,11);
/*!40000 ALTER TABLE `coreadmin_estudios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_estudios_insumos`
--

DROP TABLE IF EXISTS `coreadmin_estudios_insumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_estudios_insumos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `estudios_id` int NOT NULL,
  `insumos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `coreadmin_estudios_insumos_estudios_id_insumos_id_6eba2a7f_uniq` (`estudios_id`,`insumos_id`),
  KEY `coreadmin_estudios_i_insumos_id_973ab2c7_fk_coreadmin` (`insumos_id`),
  CONSTRAINT `coreadmin_estudios_i_estudios_id_f0828657_fk_coreadmin` FOREIGN KEY (`estudios_id`) REFERENCES `coreadmin_estudios` (`estudio_id`),
  CONSTRAINT `coreadmin_estudios_i_insumos_id_973ab2c7_fk_coreadmin` FOREIGN KEY (`insumos_id`) REFERENCES `coreadmin_insumos` (`insumo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_estudios_insumos`
--

LOCK TABLES `coreadmin_estudios_insumos` WRITE;
/*!40000 ALTER TABLE `coreadmin_estudios_insumos` DISABLE KEYS */;
INSERT INTO `coreadmin_estudios_insumos` VALUES (1,1,2),(8,2,3),(9,2,4),(4,3,5),(5,3,6),(10,4,7),(11,5,8),(12,6,9),(13,7,10);
/*!40000 ALTER TABLE `coreadmin_estudios_insumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_facturas`
--

DROP TABLE IF EXISTS `coreadmin_facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_facturas` (
  `factura_id` int NOT NULL AUTO_INCREMENT,
  `factura_numero` int NOT NULL,
  `factura_fecha` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `paciente_id_id` int NOT NULL,
  `pago_id_id` bigint NOT NULL,
  PRIMARY KEY (`factura_id`),
  UNIQUE KEY `factura_numero` (`factura_numero`),
  KEY `coreadmin_facturas_paciente_id_id_c536fc71_fk_coreadmin` (`paciente_id_id`),
  KEY `coreadmin_facturas_pago_id_id_b7bd0355_fk_coreadmin_pagos_id` (`pago_id_id`),
  CONSTRAINT `coreadmin_facturas_paciente_id_id_c536fc71_fk_coreadmin` FOREIGN KEY (`paciente_id_id`) REFERENCES `coreadmin_paciente` (`paciente_id`),
  CONSTRAINT `coreadmin_facturas_pago_id_id_b7bd0355_fk_coreadmin_pagos_id` FOREIGN KEY (`pago_id_id`) REFERENCES `coreadmin_pagos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_facturas`
--

LOCK TABLES `coreadmin_facturas` WRITE;
/*!40000 ALTER TABLE `coreadmin_facturas` DISABLE KEYS */;
INSERT INTO `coreadmin_facturas` VALUES (1,1230000001,'2024-11-06','2024-11-06 20:20:27.793721','2024-11-06 20:20:27.793750',2,2),(2,1234560001,'2024-11-06','2024-11-06 21:35:13.475760','2024-11-06 21:35:13.475793',5,4);
/*!40000 ALTER TABLE `coreadmin_facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_historiaclinica`
--

DROP TABLE IF EXISTS `coreadmin_historiaclinica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_historiaclinica` (
  `historia_id` int NOT NULL AUTO_INCREMENT,
  `historia_fecha` datetime(6) NOT NULL,
  `historia_descripcion` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `paciente_id_id` int NOT NULL,
  PRIMARY KEY (`historia_id`),
  KEY `coreadmin_historiacl_paciente_id_id_5b48a0b6_fk_coreadmin` (`paciente_id_id`),
  CONSTRAINT `coreadmin_historiacl_paciente_id_id_5b48a0b6_fk_coreadmin` FOREIGN KEY (`paciente_id_id`) REFERENCES `coreadmin_paciente` (`paciente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_historiaclinica`
--

LOCK TABLES `coreadmin_historiaclinica` WRITE;
/*!40000 ALTER TABLE `coreadmin_historiaclinica` DISABLE KEYS */;
INSERT INTO `coreadmin_historiaclinica` VALUES (1,'2024-11-06 14:43:25.847571','Estudio satisfactorio','2024-11-06 14:43:25.847604','2024-11-06 21:41:05.963157',2);
/*!40000 ALTER TABLE `coreadmin_historiaclinica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_ingresopaciente`
--

DROP TABLE IF EXISTS `coreadmin_ingresopaciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_ingresopaciente` (
  `ingreso_id` int NOT NULL AUTO_INCREMENT,
  `fecha_ingreso` date NOT NULL,
  `ingreso_hora` time(6) NOT NULL,
  `ingreso_tipo` varchar(20) NOT NULL,
  `ingreso_gravedad` varchar(10) DEFAULT NULL,
  `estado` varchar(20) NOT NULL,
  `fecha_hora_completado` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `HistoriaClinica_id` int DEFAULT NULL,
  `estudio_id` int NOT NULL,
  `paciente_id` int NOT NULL,
  `profesional_id` int NOT NULL,
  `appointment_id_id` int NOT NULL,
  PRIMARY KEY (`ingreso_id`),
  KEY `coreadmin_ingresopac_profesional_id_16dcee74_fk_coreadmin` (`profesional_id`),
  KEY `coreadmin_ingresopac_appointment_id_id_b4c7aaa8_fk_coreadmin` (`appointment_id_id`),
  KEY `coreadmin_ingresopac_HistoriaClinica_id_93076f29_fk_coreadmin` (`HistoriaClinica_id`),
  KEY `coreadmin_ingresopac_estudio_id_9a364e28_fk_coreadmin` (`estudio_id`),
  KEY `coreadmin_ingresopac_paciente_id_e1de301f_fk_coreadmin` (`paciente_id`),
  CONSTRAINT `coreadmin_ingresopac_appointment_id_id_b4c7aaa8_fk_coreadmin` FOREIGN KEY (`appointment_id_id`) REFERENCES `coreadmin_turnos` (`appointment_id`),
  CONSTRAINT `coreadmin_ingresopac_estudio_id_9a364e28_fk_coreadmin` FOREIGN KEY (`estudio_id`) REFERENCES `coreadmin_estudios` (`estudio_id`),
  CONSTRAINT `coreadmin_ingresopac_HistoriaClinica_id_93076f29_fk_coreadmin` FOREIGN KEY (`HistoriaClinica_id`) REFERENCES `coreadmin_historiaclinica` (`historia_id`),
  CONSTRAINT `coreadmin_ingresopac_paciente_id_e1de301f_fk_coreadmin` FOREIGN KEY (`paciente_id`) REFERENCES `coreadmin_paciente` (`paciente_id`),
  CONSTRAINT `coreadmin_ingresopac_profesional_id_16dcee74_fk_coreadmin` FOREIGN KEY (`profesional_id`) REFERENCES `coreadmin_profesionales` (`profesional_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_ingresopaciente`
--

LOCK TABLES `coreadmin_ingresopaciente` WRITE;
/*!40000 ALTER TABLE `coreadmin_ingresopaciente` DISABLE KEYS */;
INSERT INTO `coreadmin_ingresopaciente` VALUES (2,'2024-11-06','14:37:41.000000','CON_TURNO','Baja','Completada','2024-11-06 21:41:10.000000','2024-11-06 14:38:32.423486','2024-11-06 21:41:17.296235',1,3,2,4,1),(3,'2024-11-06','14:38:51.000000','CON_TURNO','Baja','Esperando',NULL,'2024-11-06 14:39:18.318351','2024-11-06 14:39:18.318369',NULL,2,4,3,3),(6,'2024-11-06','20:15:56.000000','CON_TURNO','Media','Esperando',NULL,'2024-11-06 20:18:37.562500','2024-11-06 20:18:37.562523',NULL,6,7,8,4),(7,'2024-11-06','21:32:28.000000','CON_TURNO','Baja','Esperando',NULL,'2024-11-06 21:33:47.097835','2024-11-06 21:33:47.097860',NULL,5,5,7,5);
/*!40000 ALTER TABLE `coreadmin_ingresopaciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_ingresopaciente_insumos`
--

DROP TABLE IF EXISTS `coreadmin_ingresopaciente_insumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_ingresopaciente_insumos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ingresopaciente_id` int NOT NULL,
  `insumos_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `coreadmin_ingresopacient_ingresopaciente_id_insum_35ebb16f_uniq` (`ingresopaciente_id`,`insumos_id`),
  KEY `coreadmin_ingresopac_insumos_id_657fed55_fk_coreadmin` (`insumos_id`),
  CONSTRAINT `coreadmin_ingresopac_ingresopaciente_id_b57208e9_fk_coreadmin` FOREIGN KEY (`ingresopaciente_id`) REFERENCES `coreadmin_ingresopaciente` (`ingreso_id`),
  CONSTRAINT `coreadmin_ingresopac_insumos_id_657fed55_fk_coreadmin` FOREIGN KEY (`insumos_id`) REFERENCES `coreadmin_insumos` (`insumo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_ingresopaciente_insumos`
--

LOCK TABLES `coreadmin_ingresopaciente_insumos` WRITE;
/*!40000 ALTER TABLE `coreadmin_ingresopaciente_insumos` DISABLE KEYS */;
INSERT INTO `coreadmin_ingresopaciente_insumos` VALUES (2,2,5),(3,3,8),(6,6,9),(7,7,10);
/*!40000 ALTER TABLE `coreadmin_ingresopaciente_insumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_ingresopaciente_salaespera`
--

DROP TABLE IF EXISTS `coreadmin_ingresopaciente_salaespera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_ingresopaciente_salaespera` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ingresopaciente_id` int NOT NULL,
  `salaespera_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `coreadmin_ingresopacient_ingresopaciente_id_salae_b7b48d7a_uniq` (`ingresopaciente_id`,`salaespera_id`),
  KEY `coreadmin_ingresopac_salaespera_id_c694befb_fk_coreadmin` (`salaespera_id`),
  CONSTRAINT `coreadmin_ingresopac_ingresopaciente_id_a0517295_fk_coreadmin` FOREIGN KEY (`ingresopaciente_id`) REFERENCES `coreadmin_ingresopaciente` (`ingreso_id`),
  CONSTRAINT `coreadmin_ingresopac_salaespera_id_c694befb_fk_coreadmin` FOREIGN KEY (`salaespera_id`) REFERENCES `coreadmin_salaespera` (`sala_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_ingresopaciente_salaespera`
--

LOCK TABLES `coreadmin_ingresopaciente_salaespera` WRITE;
/*!40000 ALTER TABLE `coreadmin_ingresopaciente_salaespera` DISABLE KEYS */;
INSERT INTO `coreadmin_ingresopaciente_salaespera` VALUES (1,7,1);
/*!40000 ALTER TABLE `coreadmin_ingresopaciente_salaespera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_insumos`
--

DROP TABLE IF EXISTS `coreadmin_insumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_insumos` (
  `insumo_id` int NOT NULL AUTO_INCREMENT,
  `insumo_nombre` varchar(50) NOT NULL,
  `stock_actual` int NOT NULL,
  `stock_minimo` int NOT NULL,
  `unidad_medida` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`insumo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_insumos`
--

LOCK TABLES `coreadmin_insumos` WRITE;
/*!40000 ALTER TABLE `coreadmin_insumos` DISABLE KEYS */;
INSERT INTO `coreadmin_insumos` VALUES (1,'Gasas',500,50,'Unidad','2024-11-06 03:44:06.520414','2024-11-06 03:44:06.520438'),(2,'Gel ecografía',19,5,'Botella','2024-11-06 03:44:21.880626','2024-11-06 20:14:31.505164'),(3,'Guia de cateter',198,50,'Unidad','2024-11-06 13:40:54.520746','2024-11-06 14:02:59.926539'),(4,'Contraste radiológico',98,10,'Botella','2024-11-06 13:41:33.827792','2024-11-06 14:02:59.925467'),(5,'Aguja de biopsia',98,20,'Unidad','2024-11-06 14:01:27.636488','2024-11-06 14:02:45.748589'),(6,'Solución antiséptica',18,5,'Botella','2024-11-06 14:01:49.177082','2024-11-06 14:02:45.749584'),(7,'Gel anestésico',199,50,'Unidad','2024-11-06 14:04:05.781011','2024-11-06 14:04:07.572907'),(8,'Reactivo químico',499,100,'Unidad','2024-11-06 14:04:52.058559','2024-11-06 14:04:54.283972'),(9,'Solución fija',99,10,'Botella','2024-11-06 14:05:43.856093','2024-11-06 14:05:45.691594'),(10,'Jeringas 0.1',99,20,'Unidad','2024-11-06 21:28:07.376444','2024-11-06 21:28:17.790081');
/*!40000 ALTER TABLE `coreadmin_insumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_paciente`
--

DROP TABLE IF EXISTS `coreadmin_paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_paciente` (
  `paciente_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `dni` varchar(8) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `plan_seguro` varchar(50) NOT NULL,
  `numero_asociado` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `HistoriaClinica_id` int DEFAULT NULL,
  `proveedor_nombre_id` int NOT NULL,
  PRIMARY KEY (`paciente_id`),
  UNIQUE KEY `dni` (`dni`),
  UNIQUE KEY `numero_asociado` (`numero_asociado`),
  KEY `coreadmin_paciente_HistoriaClinica_id_f91e9a88_fk_coreadmin` (`HistoriaClinica_id`),
  KEY `coreadmin_paciente_proveedor_nombre_id_1e245ac8_fk_coreadmin` (`proveedor_nombre_id`),
  CONSTRAINT `coreadmin_paciente_HistoriaClinica_id_f91e9a88_fk_coreadmin` FOREIGN KEY (`HistoriaClinica_id`) REFERENCES `coreadmin_historiaclinica` (`historia_id`),
  CONSTRAINT `coreadmin_paciente_proveedor_nombre_id_1e245ac8_fk_coreadmin` FOREIGN KEY (`proveedor_nombre_id`) REFERENCES `coreadmin_proveedoresseguros` (`proveedor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_paciente`
--

LOCK TABLES `coreadmin_paciente` WRITE;
/*!40000 ALTER TABLE `coreadmin_paciente` DISABLE KEYS */;
INSERT INTO `coreadmin_paciente` VALUES (1,'Veronica','Hassen','30228825','1121836922','veronicahassen@gmail.com','default.png','Oro Plus','123456/00','2024-11-06 03:41:24.024376','2024-11-06 03:41:24.024406',NULL,1),(2,'Sara','Calles','11234567','111234567','saracalles@ejemplo.com','default.png','Azul','123456/87','2024-11-06 03:42:09.782057','2024-11-06 03:42:09.782137',NULL,2),(3,'John','Doe','12345678','11987654','johndoe@example.com','default.png','Oro','123456/01','2024-11-06 14:10:40.915578','2024-11-06 14:10:40.915606',NULL,4),(4,'Josué','Evans','99999999','1199999999','josuee@ejemplix.com','default.png','Platinum','789456123','2024-11-06 14:13:47.497864','2024-11-06 14:13:47.497892',NULL,6),(5,'Jorge','Johnson','75395155','1175375312','jorgej@example.com','default.png','Naranja','123123123','2024-11-06 14:14:43.294335','2024-11-06 14:14:43.294367',NULL,5),(6,'Susana','Evans','27444555','1122223333','susanae@gmail.com','default.png','Black','789789789','2024-11-06 14:15:24.793591','2024-11-06 14:15:24.793618',NULL,2),(7,'Muriel','Queens','20159159','1112312314','murielq@gmail.com','default.png','Gold','45672189/9','2024-11-06 14:22:12.837215','2024-11-06 14:22:12.837244',NULL,1);
/*!40000 ALTER TABLE `coreadmin_paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_pagos`
--

DROP TABLE IF EXISTS `coreadmin_pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_pagos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_pago` datetime(6) NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  `ingreso_paciente_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coreadmin_pagos_ingreso_paciente_id_af0c1514_fk_coreadmin` (`ingreso_paciente_id`),
  CONSTRAINT `coreadmin_pagos_ingreso_paciente_id_af0c1514_fk_coreadmin` FOREIGN KEY (`ingreso_paciente_id`) REFERENCES `coreadmin_ingresopaciente` (`ingreso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_pagos`
--

LOCK TABLES `coreadmin_pagos` WRITE;
/*!40000 ALTER TABLE `coreadmin_pagos` DISABLE KEYS */;
INSERT INTO `coreadmin_pagos` VALUES (2,'2024-11-06 14:38:32.438031',5000.00,2),(3,'2024-11-06 14:39:18.322287',0.00,3),(4,'2024-11-06 21:33:47.114520',0.00,7),(5,'2024-11-06 21:33:47.116560',9.99,7);
/*!40000 ALTER TABLE `coreadmin_pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_profesionales`
--

DROP TABLE IF EXISTS `coreadmin_profesionales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_profesionales` (
  `profesional_id` int NOT NULL AUTO_INCREMENT,
  `profesional_nombre` varchar(50) NOT NULL,
  `profesional_apellido` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `especialidad_id_id` int NOT NULL,
  PRIMARY KEY (`profesional_id`),
  KEY `coreadmin_profesiona_especialidad_id_id_ec169441_fk_coreadmin` (`especialidad_id_id`),
  CONSTRAINT `coreadmin_profesiona_especialidad_id_id_ec169441_fk_coreadmin` FOREIGN KEY (`especialidad_id_id`) REFERENCES `coreadmin_especialidades` (`especialidad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_profesionales`
--

LOCK TABLES `coreadmin_profesionales` WRITE;
/*!40000 ALTER TABLE `coreadmin_profesionales` DISABLE KEYS */;
INSERT INTO `coreadmin_profesionales` VALUES (1,'Timoteo','Street','default.png','2024-11-06 03:43:39.872161','2024-11-06 03:43:39.872186',0,1),(2,'Andrew','Lopez','default.png','2024-11-06 03:45:07.498705','2024-11-06 03:45:07.498743',1,2),(3,'John','Carson','profile_pictures/doctor.jpg','2024-11-06 12:34:11.690936','2024-11-06 12:34:11.690966',1,8),(4,'Elizabeth','Blackwell','default.png','2024-11-06 12:46:16.270439','2024-11-06 12:46:16.270474',1,9),(5,'Gerti','Cori','default.png','2024-11-06 12:46:30.639998','2024-11-06 12:46:30.640028',1,3),(6,'Jane','Cook Wright','default.png','2024-11-06 12:46:48.377700','2024-11-06 12:46:48.377735',1,4),(7,'Helen Brooke','Taussig','default.png','2024-11-06 12:47:09.589862','2024-11-06 12:47:09.589895',1,10),(8,'Rosalind','Franklin','default.png','2024-11-06 12:47:24.084539','2024-11-06 12:47:24.084562',1,6),(9,'Edward','Jenner','default.png','2024-11-06 12:47:46.601140','2024-11-06 12:47:46.601166',1,6),(10,'Alexander','Fleming','default.png','2024-11-06 12:48:06.287604','2024-11-06 12:48:06.287637',1,10),(11,'Daniel Hale','Williams','default.png','2024-11-06 12:49:32.225628','2024-11-06 12:49:32.225678',1,4);
/*!40000 ALTER TABLE `coreadmin_profesionales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_proveedoresseguros`
--

DROP TABLE IF EXISTS `coreadmin_proveedoresseguros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_proveedoresseguros` (
  `proveedor_id` int NOT NULL AUTO_INCREMENT,
  `proveedor_nombre` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`proveedor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_proveedoresseguros`
--

LOCK TABLES `coreadmin_proveedoresseguros` WRITE;
/*!40000 ALTER TABLE `coreadmin_proveedoresseguros` DISABLE KEYS */;
INSERT INTO `coreadmin_proveedoresseguros` VALUES (1,'Medife','2024-11-06 03:40:53.185362','2024-11-06 03:40:53.185415'),(2,'Galeno','2024-11-06 03:41:59.204315','2024-11-06 03:41:59.204346'),(3,'Medicus','2024-11-06 13:18:45.734136','2024-11-06 13:18:45.734160'),(4,'OSDE','2024-11-06 13:19:04.533972','2024-11-06 13:19:04.534004'),(5,'SanCor Salud','2024-11-06 13:19:16.907577','2024-11-06 13:19:16.907603'),(6,'OSECAC','2024-11-06 13:19:26.335374','2024-11-06 13:19:26.335415');
/*!40000 ALTER TABLE `coreadmin_proveedoresseguros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_resultadolaboratorio`
--

DROP TABLE IF EXISTS `coreadmin_resultadolaboratorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_resultadolaboratorio` (
  `resultado_id` int NOT NULL AUTO_INCREMENT,
  `resultado_detalle` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `resultado_fecha` date NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `estudio_id_id` int NOT NULL,
  `visita_id_id` int NOT NULL,
  PRIMARY KEY (`resultado_id`),
  KEY `coreadmin_resultadol_estudio_id_id_4de1cbd8_fk_coreadmin` (`estudio_id_id`),
  KEY `coreadmin_resultadol_visita_id_id_ae7f3eda_fk_coreadmin` (`visita_id_id`),
  CONSTRAINT `coreadmin_resultadol_estudio_id_id_4de1cbd8_fk_coreadmin` FOREIGN KEY (`estudio_id_id`) REFERENCES `coreadmin_estudios` (`estudio_id`),
  CONSTRAINT `coreadmin_resultadol_visita_id_id_ae7f3eda_fk_coreadmin` FOREIGN KEY (`visita_id_id`) REFERENCES `coreadmin_ingresopaciente` (`ingreso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_resultadolaboratorio`
--

LOCK TABLES `coreadmin_resultadolaboratorio` WRITE;
/*!40000 ALTER TABLE `coreadmin_resultadolaboratorio` DISABLE KEYS */;
INSERT INTO `coreadmin_resultadolaboratorio` VALUES (1,'sdfsdf','2024-11-06 21:40:37.007448','2024-11-06','2024-11-06 21:40:37.007499',7,2),(2,'fdgdfgd','2024-11-06 21:48:12.061211','2024-11-06','2024-11-06 21:48:12.061253',7,7);
/*!40000 ALTER TABLE `coreadmin_resultadolaboratorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_salaespera`
--

DROP TABLE IF EXISTS `coreadmin_salaespera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_salaespera` (
  `sala_id` int NOT NULL AUTO_INCREMENT,
  `sala_nombre` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `IngresoPaciente_id` int NOT NULL,
  `estudio_id` int DEFAULT NULL,
  `profesional_id` int DEFAULT NULL,
  PRIMARY KEY (`sala_id`),
  KEY `coreadmin_salaespera_IngresoPaciente_id_73ab3888_fk_coreadmin` (`IngresoPaciente_id`),
  KEY `coreadmin_salaespera_estudio_id_91373135_fk_coreadmin` (`estudio_id`),
  KEY `coreadmin_salaespera_profesional_id_e3996938_fk_coreadmin` (`profesional_id`),
  CONSTRAINT `coreadmin_salaespera_estudio_id_91373135_fk_coreadmin` FOREIGN KEY (`estudio_id`) REFERENCES `coreadmin_estudios` (`estudio_id`),
  CONSTRAINT `coreadmin_salaespera_IngresoPaciente_id_73ab3888_fk_coreadmin` FOREIGN KEY (`IngresoPaciente_id`) REFERENCES `coreadmin_ingresopaciente` (`ingreso_id`),
  CONSTRAINT `coreadmin_salaespera_profesional_id_e3996938_fk_coreadmin` FOREIGN KEY (`profesional_id`) REFERENCES `coreadmin_profesionales` (`profesional_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_salaespera`
--

LOCK TABLES `coreadmin_salaespera` WRITE;
/*!40000 ALTER TABLE `coreadmin_salaespera` DISABLE KEYS */;
INSERT INTO `coreadmin_salaespera` VALUES (1,'Con turno','2024-11-06 14:42:52.612033','2024-11-06 21:41:19.293704',2,3,4);
/*!40000 ALTER TABLE `coreadmin_salaespera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_solicitudesinsumos`
--

DROP TABLE IF EXISTS `coreadmin_solicitudesinsumos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_solicitudesinsumos` (
  `estado_solicitud` varchar(20) NOT NULL,
  `solicitud_id` int NOT NULL AUTO_INCREMENT,
  `solicitud_fecha` date NOT NULL,
  `cantidad_solicitada` varchar(5) NOT NULL,
  `solicitado_por` varchar(50) NOT NULL,
  `fecha_completada` date DEFAULT NULL,
  `fecha_actualizacion` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `insumo_id_id` int NOT NULL,
  PRIMARY KEY (`solicitud_id`),
  KEY `coreadmin_solicitude_insumo_id_id_7897c5d8_fk_coreadmin` (`insumo_id_id`),
  CONSTRAINT `coreadmin_solicitude_insumo_id_id_7897c5d8_fk_coreadmin` FOREIGN KEY (`insumo_id_id`) REFERENCES `coreadmin_insumos` (`insumo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_solicitudesinsumos`
--

LOCK TABLES `coreadmin_solicitudesinsumos` WRITE;
/*!40000 ALTER TABLE `coreadmin_solicitudesinsumos` DISABLE KEYS */;
INSERT INTO `coreadmin_solicitudesinsumos` VALUES ('Aprobada',1,'2024-11-06','10','Vero',NULL,NULL,'2024-11-06 21:29:11.195002','2024-11-06 21:29:27.608165',1);
/*!40000 ALTER TABLE `coreadmin_solicitudesinsumos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coreadmin_turnos`
--

DROP TABLE IF EXISTS `coreadmin_turnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreadmin_turnos` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `time` time(6) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `especialidad_id` int NOT NULL,
  `estudio_id` int NOT NULL,
  `paciente_id` int NOT NULL,
  `profesional_id` int NOT NULL,
  PRIMARY KEY (`appointment_id`),
  UNIQUE KEY `coreadmin_turnos_profesional_id_date_time_f208741c_uniq` (`profesional_id`,`date`,`time`),
  KEY `coreadmin_turnos_especialidad_id_c9cdc1c0_fk_coreadmin` (`especialidad_id`),
  KEY `coreadmin_turnos_estudio_id_c7245b0b_fk_coreadmin` (`estudio_id`),
  KEY `coreadmin_turnos_paciente_id_72931097_fk_coreadmin` (`paciente_id`),
  CONSTRAINT `coreadmin_turnos_especialidad_id_c9cdc1c0_fk_coreadmin` FOREIGN KEY (`especialidad_id`) REFERENCES `coreadmin_especialidades` (`especialidad_id`),
  CONSTRAINT `coreadmin_turnos_estudio_id_c7245b0b_fk_coreadmin` FOREIGN KEY (`estudio_id`) REFERENCES `coreadmin_estudios` (`estudio_id`),
  CONSTRAINT `coreadmin_turnos_paciente_id_72931097_fk_coreadmin` FOREIGN KEY (`paciente_id`) REFERENCES `coreadmin_paciente` (`paciente_id`),
  CONSTRAINT `coreadmin_turnos_profesional_id_b61f41fb_fk_coreadmin` FOREIGN KEY (`profesional_id`) REFERENCES `coreadmin_profesionales` (`profesional_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreadmin_turnos`
--

LOCK TABLES `coreadmin_turnos` WRITE;
/*!40000 ALTER TABLE `coreadmin_turnos` DISABLE KEYS */;
INSERT INTO `coreadmin_turnos` VALUES (1,'2024-11-16','03:56:53.000000','SCHEDULED','2024-11-06 03:56:57.876735','2024-11-06 03:56:57.876755',1,1,2,2),(2,'2024-11-25','14:36:46.000000','SCHEDULED','2024-11-06 14:36:49.838639','2024-11-06 14:36:49.838660',9,3,3,6),(3,'2024-11-06','14:37:09.000000','SCHEDULED','2024-11-06 14:37:11.593839','2024-11-06 14:37:11.593863',4,5,4,11),(4,'2024-11-15','12:00:00.000000','SCHEDULED','2024-11-06 20:15:17.741701','2024-11-06 20:15:17.741727',3,6,7,8),(5,'2024-11-16','12:00:00.000000','SCHEDULED','2024-11-06 21:31:56.587504','2024-11-06 21:31:56.587544',4,5,5,3);
/*!40000 ALTER TABLE `coreadmin_turnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-11-06 03:40:53.187007','1','Medife',1,'[{\"added\": {}}]',10,1),(2,'2024-11-06 03:41:24.025624','1','Veronica Hassen',1,'[{\"added\": {}}]',13,1),(3,'2024-11-06 03:41:59.205358','2','Galeno',1,'[{\"added\": {}}]',10,1),(4,'2024-11-06 03:42:09.784508','2','Sara Calles',1,'[{\"added\": {}}]',13,1),(5,'2024-11-06 03:42:50.909850','1','Cardiología',1,'[{\"added\": {}}]',7,1),(6,'2024-11-06 03:42:57.058713','2','Endocrinología',1,'[{\"added\": {}}]',7,1),(7,'2024-11-06 03:43:01.858099','3','Ginecología',1,'[{\"added\": {}}]',7,1),(8,'2024-11-06 03:43:06.893371','4','Laboratorio',1,'[{\"added\": {}}]',7,1),(9,'2024-11-06 03:43:39.873280','1','Timoteo Perfil Profesional',1,'[{\"added\": {}}]',17,1),(10,'2024-11-06 03:44:06.521489','1','1 - Gasas Información Insumo',1,'[{\"added\": {}}]',9,1),(11,'2024-11-06 03:44:21.881983','2','2 - Gel ecografía Información Insumo',1,'[{\"added\": {}}]',9,1),(12,'2024-11-06 03:44:43.998722','1','1 - EcoDoppler Información Estudios',1,'[{\"added\": {}}]',12,1),(13,'2024-11-06 03:45:07.499904','2','Andrew Perfil Profesional',1,'[{\"added\": {}}]',17,1),(14,'2024-11-06 03:56:57.877778','1','1 - Sara Calles - 2024-11-16 03:56:53',1,'[{\"added\": {}}]',21,1),(15,'2024-11-06 11:25:35.661703','1','Recepcionista',1,'[{\"added\": {}}]',3,1),(16,'2024-11-06 11:27:29.311586','2','Profesional',1,'[{\"added\": {}}]',3,1),(17,'2024-11-06 11:29:54.999054','2','Veronica',1,'[{\"added\": {}}]',4,1),(18,'2024-11-06 11:30:17.898528','2','Veronica',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(19,'2024-11-06 11:30:35.640797','3','Daniela',1,'[{\"added\": {}}]',4,1),(20,'2024-11-06 11:30:46.879320','3','Daniela',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(21,'2024-11-06 11:31:04.988456','4','Romina',1,'[{\"added\": {}}]',4,1),(22,'2024-11-06 11:31:25.304553','5','Emira',1,'[{\"added\": {}}]',4,1),(23,'2024-11-06 11:31:33.306209','5','Emira',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(24,'2024-11-06 11:31:43.323548','4','Romina',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]',4,1),(25,'2024-11-06 11:32:00.417318','2','Veronica',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]',4,1),(26,'2024-11-06 11:32:18.520992','4','Romina',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]',4,1),(27,'2024-11-06 11:32:34.076309','5','Emira',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]',4,1),(28,'2024-11-06 11:32:50.191270','3','Daniela',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]',4,1),(29,'2024-11-06 11:48:49.270984','5','Traumatología',1,'[{\"added\": {}}]',7,1),(30,'2024-11-06 11:48:54.115676','6','Pediatría',1,'[{\"added\": {}}]',7,1),(31,'2024-11-06 11:48:59.082611','7','Ginecología',1,'[{\"added\": {}}]',7,1),(32,'2024-11-06 11:49:05.818519','8','Neurología',1,'[{\"added\": {}}]',7,1),(33,'2024-11-06 11:49:16.326697','9','Dermatología',1,'[{\"added\": {}}]',7,1),(34,'2024-11-06 11:49:26.968388','10','Obstetricia',1,'[{\"added\": {}}]',7,1),(35,'2024-11-06 12:34:11.694317','3','John Perfil Profesional',1,'[{\"added\": {}}]',17,1),(36,'2024-11-06 12:46:16.273377','4','Elizabeth Perfil Profesional',1,'[{\"added\": {}}]',17,1),(37,'2024-11-06 12:46:30.641115','5','Gerti Perfil Profesional',1,'[{\"added\": {}}]',17,1),(38,'2024-11-06 12:46:48.379009','6','Jane Perfil Profesional',1,'[{\"added\": {}}]',17,1),(39,'2024-11-06 12:47:09.590714','7','Helen Brooke Perfil Profesional',1,'[{\"added\": {}}]',17,1),(40,'2024-11-06 12:47:24.085557','8','Rosalind Perfil Profesional',1,'[{\"added\": {}}]',17,1),(41,'2024-11-06 12:47:46.602250','9','Edward Perfil Profesional',1,'[{\"added\": {}}]',17,1),(42,'2024-11-06 12:48:06.289325','10','Alexander Perfil Profesional',1,'[{\"added\": {}}]',17,1),(43,'2024-11-06 12:48:15.691957','7','Ginecología',3,'',7,1),(44,'2024-11-06 12:49:32.227770','11','Daniel Hale Perfil Profesional',1,'[{\"added\": {}}]',17,1),(45,'2024-11-06 13:18:45.737188','3','Medicus',1,'[{\"added\": {}}]',10,1),(46,'2024-11-06 13:19:04.542940','4','OSDE',1,'[{\"added\": {}}]',10,1),(47,'2024-11-06 13:19:16.909628','5','SanCor Salud',1,'[{\"added\": {}}]',10,1),(48,'2024-11-06 13:19:26.343218','6','OSECAC',1,'[{\"added\": {}}]',10,1),(49,'2024-11-06 13:40:54.528989','3','3 - Guia de cateter Información Insumo',1,'[{\"added\": {}}]',9,1),(50,'2024-11-06 13:41:33.835419','4','4 - Contraste radiológico Información Insumo',1,'[{\"added\": {}}]',9,1),(51,'2024-11-06 13:51:26.266471','2','2 - Angiografía Coronaria - 15000',1,'[{\"added\": {}}]',12,1),(52,'2024-11-06 14:01:27.637496','5','5 - Aguja de biopsia Información Insumo',1,'[{\"added\": {}}]',9,1),(53,'2024-11-06 14:01:49.178565','6','6 - Solución antiséptica Información Insumo',1,'[{\"added\": {}}]',9,1),(54,'2024-11-06 14:01:51.479651','3','3 - Biopsia de piel - 4999.99',1,'[{\"added\": {}}]',12,1),(55,'2024-11-06 14:02:45.751391','2','2 - Angiografía Coronaria - 15000.00',2,'[{\"changed\": {\"fields\": [\"Insumos\"]}}]',12,1),(56,'2024-11-06 14:02:59.927517','2','2 - Angiografía Coronaria - 15000.00',2,'[{\"changed\": {\"fields\": [\"Insumos\"]}}]',12,1),(57,'2024-11-06 14:04:05.781851','7','7 - Gel anestésico Información Insumo',1,'[{\"added\": {}}]',9,1),(58,'2024-11-06 14:04:07.574123','4','4 - Terapia con láser - 25000',1,'[{\"added\": {}}]',12,1),(59,'2024-11-06 14:04:52.065972','8','8 - Reactivo químico Información Insumo',1,'[{\"added\": {}}]',9,1),(60,'2024-11-06 14:04:54.285241','5','5 - Medición de Hormonas Tiroideas - 2000',1,'[{\"added\": {}}]',12,1),(61,'2024-11-06 14:05:43.856918','9','9 - Solución fija Información Insumo',1,'[{\"added\": {}}]',9,1),(62,'2024-11-06 14:05:45.693134','6','6 - Papanicolaou (PAP) - 25000',1,'[{\"added\": {}}]',12,1),(63,'2024-11-06 14:10:40.916693','3','John Doe',1,'[{\"added\": {}}]',13,1),(64,'2024-11-06 14:13:47.499481','4','Josué Evans',1,'[{\"added\": {}}]',13,1),(65,'2024-11-06 14:14:43.301458','5','Jorge Johnson',1,'[{\"added\": {}}]',13,1),(66,'2024-11-06 14:15:24.801436','6','Susana Evans',1,'[{\"added\": {}}]',13,1),(67,'2024-11-06 14:22:12.838971','7','Muriel Queens',1,'[{\"added\": {}}]',13,1),(68,'2024-11-06 14:36:49.840903','2','2 - John Doe - 2024-11-25 14:36:46',1,'[{\"added\": {}}]',21,1),(69,'2024-11-06 14:37:11.595205','3','3 - Josué Evans - 2024-11-06 14:37:09',1,'[{\"added\": {}}]',21,1),(70,'2024-11-06 14:38:32.440800','2','2 - Sara Calles - Esperando',1,'[{\"added\": {}}, {\"added\": {\"name\": \"pagos\", \"object\": \"Pago de Sara Calles por 5000 el 2024-11-06 14:38:32.438031+00:00\"}}]',14,1),(71,'2024-11-06 14:39:18.323986','3','3 - Josué Evans - Esperando',1,'[{\"added\": {}}, {\"added\": {\"name\": \"pagos\", \"object\": \"Pago de Josu\\u00e9 Evans por 0 el 2024-11-06 14:39:18.322287+00:00\"}}]',14,1),(72,'2024-11-06 14:42:52.615574','1','1 - Con turno - 2 - Sara Calles - Esperando',1,'[{\"added\": {}}]',19,1),(73,'2024-11-06 14:43:25.854940','1','1 Historia Clínica',1,'[{\"added\": {}}]',8,1),(74,'2024-11-06 14:43:33.015921','2','2 - Sara Calles - Esperando',2,'[{\"changed\": {\"fields\": [\"HistoriaClinica\", \"Fecha y Hora Completado\"]}}]',14,1),(75,'2024-11-06 14:44:11.639392','2','2 - Sara Calles - Esperando',2,'[{\"changed\": {\"fields\": [\"Appointment id\"]}}]',14,1),(76,'2024-11-06 20:12:30.555757','1','Recepcionista',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(77,'2024-11-06 20:13:52.682265','1','Recepcionista',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(78,'2024-11-06 20:14:31.507293','2','2 - Gel ecografía Información Insumo',2,'[{\"changed\": {\"fields\": [\"Unidad de Medida\"]}}]',9,2),(79,'2024-11-06 20:15:17.743500','4','4 - Muriel Queens - 2024-11-15 12:00:00',1,'[{\"added\": {}}]',21,2),(80,'2024-11-06 20:18:37.580481','6','6 - Muriel Queens - Esperando',1,'[{\"added\": {}}]',14,2),(81,'2024-11-06 20:20:27.801580','1','1230000001',1,'[{\"added\": {}}]',16,2),(82,'2024-11-06 21:26:31.067434','11','Neonatología',1,'[{\"added\": {}}]',7,1),(83,'2024-11-06 21:28:07.383178','10','10 - Jeringas 0.1 Información Insumo',1,'[{\"added\": {}}]',9,1),(84,'2024-11-06 21:28:17.797300','7','7 - Abc - 15000',1,'[{\"added\": {}}]',12,1),(85,'2024-11-06 21:29:11.200600','1','1 - 1 - Gasas Información Insumo - Pendiente',1,'[{\"added\": {}}]',20,1),(86,'2024-11-06 21:29:27.615499','1','1 - 1 - Gasas Información Insumo - Aprobada',2,'[{\"changed\": {\"fields\": [\"Estado solicitud\"]}}]',20,1),(87,'2024-11-06 21:31:56.590034','5','5 - Jorge Johnson - 2024-11-16 12:00:00',1,'[{\"added\": {}}]',21,2),(88,'2024-11-06 21:33:47.118665','7','7 - Jorge Johnson - Esperando',1,'[{\"added\": {}}, {\"added\": {\"name\": \"pagos\", \"object\": \"Pago de Jorge Johnson por 0 el 2024-11-06 21:33:47.114520+00:00\"}}, {\"added\": {\"name\": \"pagos\", \"object\": \"Pago de Jorge Johnson por 9.99 el 2024-11-06 21:33:47.116560+00:00\"}}]',14,2),(89,'2024-11-06 21:35:13.477694','2','1234560001',1,'[{\"added\": {}}]',16,2),(90,'2024-11-06 21:36:06.924946','2','Profesional',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(91,'2024-11-06 21:36:39.364369','4','Romina',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(92,'2024-11-06 21:40:37.012533','1','1 - 2024-11-06',1,'[{\"added\": {}}]',18,4),(93,'2024-11-06 21:41:05.966960','1','1 Historia Clínica',2,'[]',8,4),(94,'2024-11-06 21:41:17.306289','2','2 - Sara Calles - Completada',2,'[{\"changed\": {\"fields\": [\"Estado\", \"Fecha y Hora Completado\"]}}]',14,4),(95,'2024-11-06 21:41:19.299365','1','1 - Con turno - 2 - Sara Calles - Completada',2,'[]',19,4),(96,'2024-11-06 21:48:12.062979','2','2 - 2024-11-06',1,'[{\"added\": {}}]',18,1),(97,'2024-11-07 11:35:06.103944','2','Profesional',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(98,'2024-11-07 12:00:43.031072','2','Profesional',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(99,'2024-11-07 12:02:55.427947','1','Recepcionista',2,'[]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'coreadmin','admin'),(7,'coreadmin','especialidades'),(12,'coreadmin','estudios'),(16,'coreadmin','facturas'),(8,'coreadmin','historiaclinica'),(22,'coreadmin','historiaclinicadetalle'),(14,'coreadmin','ingresopaciente'),(9,'coreadmin','insumos'),(13,'coreadmin','paciente'),(15,'coreadmin','pagos'),(17,'coreadmin','profesionales'),(10,'coreadmin','proveedoresseguros'),(18,'coreadmin','resultadolaboratorio'),(19,'coreadmin','salaespera'),(20,'coreadmin','solicitudesinsumos'),(21,'coreadmin','turnos'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-11-06 03:37:50.136167'),(2,'auth','0001_initial','2024-11-06 03:37:51.273969'),(3,'admin','0001_initial','2024-11-06 03:37:51.560319'),(4,'admin','0002_logentry_remove_auto_add','2024-11-06 03:37:51.573201'),(5,'admin','0003_logentry_add_action_flag_choices','2024-11-06 03:37:51.589965'),(6,'contenttypes','0002_remove_content_type_name','2024-11-06 03:37:51.747693'),(7,'auth','0002_alter_permission_name_max_length','2024-11-06 03:37:51.858538'),(8,'auth','0003_alter_user_email_max_length','2024-11-06 03:37:51.907704'),(9,'auth','0004_alter_user_username_opts','2024-11-06 03:37:51.920261'),(10,'auth','0005_alter_user_last_login_null','2024-11-06 03:37:52.016241'),(11,'auth','0006_require_contenttypes_0002','2024-11-06 03:37:52.020227'),(12,'auth','0007_alter_validators_add_error_messages','2024-11-06 03:37:52.036640'),(13,'auth','0008_alter_user_username_max_length','2024-11-06 03:37:52.238279'),(14,'auth','0009_alter_user_last_name_max_length','2024-11-06 03:37:52.397310'),(15,'auth','0010_alter_group_name_max_length','2024-11-06 03:37:52.435536'),(16,'auth','0011_update_proxy_permissions','2024-11-06 03:37:52.449940'),(17,'auth','0012_alter_user_first_name_max_length','2024-11-06 03:37:52.558707'),(18,'coreadmin','0001_initial','2024-11-06 03:37:55.660439'),(19,'sessions','0001_initial','2024-11-06 03:37:55.709487'),(20,'coreadmin','0002_alter_pagos_options_ingresopaciente_salaespera_and_more','2024-11-06 20:18:20.733189'),(21,'coreadmin','0003_alter_resultadolaboratorio_options_and_more','2024-11-07 17:56:26.266651');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-07 15:28:56
