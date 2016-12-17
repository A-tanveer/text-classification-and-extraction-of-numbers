-- CREATE DATABASE places
--   DEFAULT CHARACTER SET utf8
--   DEFAULT COLLATE utf8_general_ci;

SET FOREIGN_KEY_CHECKS = 0;
  --
  -- Definition of table `division`
  --

  DROP TABLE IF EXISTS `division`;
  CREATE TABLE `division` (
    `division_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(45) CHARACTER SET utf8 NOT NULL,
    `bangla_name` varchar(45) CHARACTER SET utf8 NOT NULL,
    PRIMARY KEY (`division_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=223936 DEFAULT CHARSET=utf8;



  --
  -- Definition of table `District`
  --

  DROP TABLE IF EXISTS `district`;
  CREATE TABLE `district` (
    `district_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `division_id` int(10) unsigned NOT NULL,
    `name` varchar(45) CHARACTER SET utf8 NOT NULL,
    `bangla_name` varchar(45) CHARACTER SET utf8 NOT NULL,
    PRIMARY KEY (`district_id`),
    CONSTRAINT `district_division_fk` FOREIGN KEY (`division_id`) REFERENCES `division` (`division_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
  ) ENGINE=InnoDB AUTO_INCREMENT=223936 DEFAULT CHARSET=utf8;



--
-- Definition of table `upazilla`
--

DROP TABLE IF EXISTS `upazilla`;
CREATE TABLE `upazilla` (
      `upazilla_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `district_id` int(10) unsigned NOT NULL,
      `name` varchar(45) CHARACTER SET utf8 NOT NULL,
      `bangla_name` varchar(45) CHARACTER SET utf8 NOT NULL,
      PRIMARY KEY (`upazilla_id`),
      CONSTRAINT `upazilla_district_fk` FOREIGN KEY (`district_id`) REFERENCES `district` (`district_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=223936 DEFAULT CHARSET=utf8;



--
-- Table structure for table `news_all_processed`
--

DROP TABLE IF EXISTS `processed_news`;
CREATE TABLE IF NOT EXISTS `processed_news` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `content` mediumtext,
  `domain` varchar(541) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL,
  `title` varchar(223) DEFAULT NULL,
  `news_date` date DEFAULT NULL,
  `original_date` date DEFAULT NULL,
  `casualty_count` int(10) DEFAULT 0 NOT NULL ,
  `injury_count` int(10) DEFAULT 0 NOT NULL ,
  `upazilla_id_str` varchar(100) DEFAULT NULL,
  `match_percent` int(10) DEFAULT 0,
  `is_unique` tinyint(1) DEFAULT '1',
  `copy_of` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
