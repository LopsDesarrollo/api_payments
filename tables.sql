CREATE TABLE `app_payments`.`payments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NOT NULL DEFAULT 0,
  `date_entry` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

ALTER TABLE `app_payments`.`payments` 
ADD COLUMN `folio` VARCHAR(45) NOT NULL AFTER `id`;

CREATE TABLE IF NOT EXISTS `app_payments`.`details` (
  `iddetails` INT(11) NOT NULL AUTO_INCREMENT,
  `payments_id` INT(11) NOT NULL,
  `one` INT(11) NOT NULL DEFAULT 0,
  `two` INT(11) NOT NULL DEFAULT 0,
  `five` INT(11) NOT NULL DEFAULT 0,
  `ten` INT(11) NOT NULL DEFAULT 0,
  `twenty` INT(11) NOT NULL DEFAULT 0,
  `fifty` INT(11) NOT NULL DEFAULT 0,
  `hundred` INT(11) NOT NULL DEFAULT 0,
  `two_hundred` INT(11) NOT NULL DEFAULT 0,
  `five_hundred` INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`iddetails`),
  INDEX `fk_details_payments_idx` (`payments_id` ASC) VISIBLE,
  CONSTRAINT `fk_details_payments`
    FOREIGN KEY (`payments_id`)
    REFERENCES `app_payments`.`payments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

