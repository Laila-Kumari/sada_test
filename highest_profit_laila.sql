-- Ran in MySQL. Imported data using Import Wizard offered by MySQL

CREATE TABLE `world`.`sada_test` (
  `year` INT NOT NULL,
  `rank` VARCHAR(45) NULL,
  `company` VARCHAR(45) NULL,
  `revenue` VARCHAR(45) NULL,
  `profit` VARCHAR(45) NULL);


-- Count total rows 

SELECT COUNT(*) FROM world.sada_test
;


-- Count total rows where value of profit is numeric

SELECT COUNT(*) FROM world.sada_test
where REGEXP_SUBSTR(profit ,"[0-9]+") >= 0
;

-- Top 20 rows with valid 'profit' numeric values

SELECT * FROM world.sada_test
where REGEXP_SUBSTR(profit ,"[0-9]+") >= 0
ORDER BY profit DESC
LIMIT 20
;
