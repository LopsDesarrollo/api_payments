CREATE TABLE `app_payments`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NOT NULL DEFAULT 0,
  `date_entry` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

ALTER TABLE `app_payments`.`payments` 
ADD COLUMN `folio` VARCHAR(45) NOT NULL AFTER `id`;