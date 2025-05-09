-- 0. 데이터베이스 생성 및 선택
CREATE DATABASE IF NOT EXISTS `cocktail_canvas`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE `cocktail_canvas`;

-- 1. 사용자 테이블
CREATE TABLE IF NOT EXISTS `User` (
  `id`   INT           NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100)  NOT NULL,
  `kakao_id` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. 채팅 세션 테이블
CREATE TABLE IF NOT EXISTS `ChatSessions` (
  `id`         INT           NOT NULL AUTO_INCREMENT,
  `user_id`    INT           NOT NULL,
  `title`      VARCHAR(200)  NOT NULL,
  `created_at` DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_ChS_user` (`user_id`),
  CONSTRAINT `fk_ChS_user`
    FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. 채팅 메시지 테이블
CREATE TABLE IF NOT EXISTS `ChatMessages` (
  `id`         INT           NOT NULL AUTO_INCREMENT,
  `session_id` INT           NOT NULL,
  `role`       VARCHAR(20)   NOT NULL,    -- 'user', 'assistant', 'system' 등
  `content`    TEXT          NOT NULL,
  `created_at` DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_Cm_session` (`session_id`),
  CONSTRAINT `fk_Cm_session`
    FOREIGN KEY (`session_id`) REFERENCES `ChatSessions` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. 칵테일 테이블
CREATE TABLE IF NOT EXISTS `Cocktail` (
  `id`              INT           NOT NULL AUTO_INCREMENT,
  `user_id`         INT           NOT NULL,
  `name`            VARCHAR(100)  NOT NULL,
  `description`     TEXT,
  `registered_date` DATE,
  PRIMARY KEY (`id`),
  KEY `idx_cocktail_user` (`user_id`),
  CONSTRAINT `fk_cocktail_user`
    FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. 칵테일 태그 (다중값)
CREATE TABLE IF NOT EXISTS `CocktailTag` (
  `cocktail_id` INT         NOT NULL,
  `tag`         VARCHAR(50) NOT NULL,
  PRIMARY KEY (`cocktail_id`,`tag`),
  KEY `idx_cttag_cocktail` (`cocktail_id`),
  CONSTRAINT `fk_cttag_cocktail`
    FOREIGN KEY (`cocktail_id`) REFERENCES `Cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. 레시피 테이블 (칵테일 1:1 매핑)
CREATE TABLE IF NOT EXISTS `Recipe` (
  `id`          INT NOT NULL AUTO_INCREMENT,
  `cocktail_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_recipe_cocktail` (`cocktail_id`),
  CONSTRAINT `fk_recipe_cocktail`
    FOREIGN KEY (`cocktail_id`) REFERENCES `Cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7. 재료 테이블
CREATE TABLE IF NOT EXISTS `Ingredient` (
  `id`   INT           NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100)  NOT NULL,
  `tag`  VARCHAR(50),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. 레시피-재료 매핑 테이블 (다대다 + 용량)
CREATE TABLE IF NOT EXISTS `RecipeIngredient` (
  `recipe_id`     INT         NOT NULL,
  `ingredient_id` INT         NOT NULL,
  `amount`        VARCHAR(50),
  PRIMARY KEY (`recipe_id`,`ingredient_id`),
  KEY `idx_ri_recipe`     (`recipe_id`),
  KEY `idx_ri_ingredient` (`ingredient_id`),
  CONSTRAINT `fk_ri_recipe`
    FOREIGN KEY (`recipe_id`) REFERENCES `Recipe` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_ri_ingredient`
    FOREIGN KEY (`ingredient_id`) REFERENCES `Ingredient` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 9. 리뷰 테이블 (사용자 ↔ 칵테일)
CREATE TABLE IF NOT EXISTS `Review` (
  `id`          INT       NOT NULL AUTO_INCREMENT,
  `user_id`     INT       NOT NULL,
  `cocktail_id` INT       NOT NULL,
  `rating`      TINYINT   NOT NULL,
  `comment`     TEXT,
  `review_date` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_review_user`     (`user_id`),
  KEY `idx_review_cocktail` (`cocktail_id`),
  CONSTRAINT `fk_review_user`
    FOREIGN KEY (`user_id`) REFERENCES `User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_review_cocktail`
    FOREIGN KEY (`cocktail_id`) REFERENCES `Cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;