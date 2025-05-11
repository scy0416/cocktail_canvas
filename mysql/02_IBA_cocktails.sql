/*!40101 SET NAMES utf8mb4 */;

USE `cocktail_canvas`;

-- id: 1, name: 송찬영, kakao_id: 4253413824로 추가(어드민 계정)

-- INSERT INTO `User` VALUES (1, '송찬영', '4253413824');
INSERT INTO `User` VALUES (1, '관리자', 'admin');

-- 칵테일 재료 추가
-- 증류주
INSERT INTO `Ingredient` VALUES (1, "진", "증류주");
INSERT INTO `Ingredient` VALUES (2, "드라이 진", "증류주");
INSERT INTO `Ingredient` VALUES (3, "올드 톰 진", "증류주");
INSERT INTO `Ingredient` VALUES (4, "보드카", "증류주");
INSERT INTO `Ingredient` VALUES (5, "화이트 럼", "증류주");
INSERT INTO `Ingredient` VALUES (6, "카샤사", "증류주");
INSERT INTO `Ingredient` VALUES (7, "버번", "증류주");
INSERT INTO `Ingredient` VALUES (8, "라이 위스키", "증류주");
INSERT INTO `Ingredient` VALUES (9, "브랜디", "증류주");
INSERT INTO `Ingredient` VALUES (10, "꼬냑", "증류주");
INSERT INTO `Ingredient` VALUES (11, "칼바도스", "증류주");
INSERT INTO `Ingredient` VALUES (12, "아구아르에테", "증류주");
INSERT INTO `Ingredient` VALUES (13, "압생트", "증류주");
-- 리큐르, 아페리티프, 비터스
INSERT INTO `Ingredient` VALUES (14, "크렘 드 카카오 (브라운)", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (15, "크렘 드 바이올렛", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (16, "마라스키노 룩사르도", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (17, "애프리콧", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (18, "트리플 섹", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (19, "쿠앵트로", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (20, "그랑 마니에르", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (21, "커피 리큐르", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (22, "크렘 드 뮤르", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (23, "큐라소", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (24, "그린 샤르트뢰즈", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (25, "팔레넘", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (26, "스위트 레드 버무스", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (27, "드라이 버무스", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (28, "릴렐 블랑", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (29, "비터 캄파리", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (30, "아로마틱 비터스", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (31, "오렌지 비터스", "리큐르·아페리티프·비터스");
INSERT INTO `Ingredient` VALUES (32, "앙고스투라 비터스스", "리큐르·아페리티프·비터스");
-- 와인, 스파클링
INSERT INTO `Ingredient` VALUES (33, "프로세코", "와인·스파클링");
INSERT INTO `Ingredient` VALUES (34, "샴페인", "와인·스파클링");
-- 주스 퓨레
INSERT INTO `Ingredient` VALUES (35, "생레몬 주스", "주스·퓨레");
INSERT INTO `Ingredient` VALUES (36, "생라임 주스", "주스·퓨레");
INSERT INTO `Ingredient` VALUES (37, "생오렌지 주스", "주스·퓨레");
INSERT INTO `Ingredient` VALUES (38, "토마토 주스", "주스·퓨레");
INSERT INTO `Ingredient` VALUES (39, "생파인애플 주스", "주스·퓨레");
INSERT INTO `Ingredient` VALUES (40, "백도 복숭아 퓨레", "주스·퓨레");
-- 스위트너, 시럽
INSERT INTO `Ingredient` VALUES (41, "꿀 시럽", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (42, "심플 시럽", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (43, "설탕 시럽", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (44, "라즈베리 시럽", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (45, "백설탕", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (46, "생꿀", "스위트너·시럽");
INSERT INTO `Ingredient` VALUES (47, "각설탕", "스위트너·시럽");
-- 믹서, 기타 음료
INSERT INTO `Ingredient` VALUES (48, "소다 워터", "믹서·기타 음료");
INSERT INTO `Ingredient` VALUES (49, "물", "믹서·기타 음료");
INSERT INTO `Ingredient` VALUES (50, "우스터 소스", "믹서·기타 음료");
INSERT INTO `Ingredient` VALUES (51, "타바스코", "믹서·기타 음료");
INSERT INTO `Ingredient` VALUES (52, "셀러리 솔트", "믹서·기타 음료");
INSERT INTO `Ingredient` VALUES (53, "후추", "믹서·기타 음료");
-- 유제품, 식재료
INSERT INTO `Ingredient` VALUES (54, "생크림", "유제품·식재료");
INSERT INTO `Ingredient` VALUES (55, "달걀 흰자", "유제품·식재료");
INSERT INTO `Ingredient` VALUES (56, "라임", "유제품·식재료");

-- IBA 칵테일 정보들 추가
INSERT INTO `Cocktail` VALUES (1, 1, "Alexander", "IBA 공식 칵테일 Alexander", NOW(), 21.7, "1_Alexander.png", "-");
INSERT INTO `Cocktail` VALUES (2, 1, "Americano", "IBA 공식 칵테일 Americano", NOW(), 13.3, "2_Americano.png", "-");
INSERT INTO `Cocktail` VALUES (3, 1, "Angel Face", "IBA 공식 칵테일 Angel Face", NOW(), 40.0, "3_Angel Face.png", "-");
INSERT INTO `Cocktail` VALUES (4, 1, "Aviation", "IBA 공식 칵테일 Aviation", NOW(), 29.8, "4_Aviation.png", "-");
INSERT INTO `Cocktail` VALUES (5, 1, "Bee's Knees", "IBA 공식 칵테일 Bee's Knees", NOW(), 19.5, "5_Bee's Knees.png", "-");
INSERT INTO `Cocktail` VALUES (6, 1, "Bellini", "IBA 공식 칵테일 Bellini", NOW(), 7.3, "6_Bellini.png", "-");
INSERT INTO `Cocktail` VALUES (7, 1, "Between the Sheets", "IBA 공식 칵테일 Between the Sheets", NOW(), 30.0, "7_Between the Sheets.png", "-");
INSERT INTO `Cocktail` VALUES (8, 1, "Black Russian", "IBA 공식 칵테일 Black Russian", NOW(), 34.3, "8_Black Russian.png", "-");
INSERT INTO `Cocktail` VALUES (9, 1, "Bloody Mary", "IBA 공식 칵테일 Bloody Mary", NOW(), 17.1, "9_Bloody Mary.png", "-");
INSERT INTO `Cocktail` VALUES (10, 1, "Boulevardier", "IBA 공식 칵테일 Boulevardier", NOW(), 28.6, "10_Boulevardier.png", "-");
INSERT INTO `Cocktail` VALUES (11, 1, "Bramble", "IBA 공식 칵테일 Bramble", NOW(), 22.4, "11_Bramble.png", "-");
INSERT INTO `Cocktail` VALUES (12, 1, "Brandy Crusta", "IBA 공식 칵테일 Brandy Crusta", NOW(), 29.3, "12_Brandy Crusta.png", "-");
INSERT INTO `Cocktail` VALUES (13, 1, "Caipirinha", "IBA 공식 칵테일 Caipirinha", NOW(), 21.8, "13_Caipirinha.png", "-");
INSERT INTO `Cocktail` VALUES (14, 1, "Canchanchara", "IBA 공식 칵테일 Canchanchara", NOW(), 17.1, "14_Canchanchara.png", "-");
INSERT INTO `Cocktail` VALUES (15, 1, "Cardinale", "IBA 공식 칵테일 Cardinale", NOW(), 30.9, "15_Cardinale.png", "-");
INSERT INTO `Cocktail` VALUES (16, 1, "Casino", "IBA 공식 칵테일 Casino", NOW(), 32.0, "16_Casino.png", "-");
INSERT INTO `Cocktail` VALUES (17, 1, "Chanpagne Cocktail", "IBA 공식 칵테일 Chanpagne Cocktail", NOW(), 14.8, "17_Chanpagne Cocktail.png", "-");
INSERT INTO `Cocktail` VALUES (18, 1, "Chartreuse Swizzle", "IBA 공식 칵테일 Chartreuse Swizzle", NOW(), 23.5, "18_Chartreuse Swizzle.png", "-");
INSERT INTO `Cocktail` VALUES (19, 1, "Clover Club", "IBA 공식 칵테일 Clover Club", NOW(), 20.0, "19_Clover Club.png", "-");
INSERT INTO `Cocktail` VALUES (20, 1, "Corpse Reviver #2", "IBA 공식 칵테일 Corpse Reviver #2", NOW(), 24.5, "20_Corpse Reviver no2.png", "-");

-- 칵테일 태그 정보 추가
INSERT INTO `CocktailTag` VALUES (1, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (2, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (3, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (4, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (5, "New Era");
INSERT INTO `CocktailTag` VALUES (6, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (7, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (8, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (9, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (10, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (11, "New Era");
INSERT INTO `CocktailTag` VALUES (12, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (13, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (14, "New Era");
INSERT INTO `CocktailTag` VALUES (15, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (16, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (17, "Contemporary Classics");
INSERT INTO `CocktailTag` VALUES (18, "New Era");
INSERT INTO `CocktailTag` VALUES (19, "The unforgettables");
INSERT INTO `CocktailTag` VALUES (20, "Contemporary Classics");

-- 칵테일 재료 등록
-- 1
INSERT INTO `RecipeIngredient` VALUES (1, 10, "30ml");
INSERT INTO `RecipeIngredient` VALUES (1, 14, "30ml");
INSERT INTO `RecipeIngredient` VALUES (1, 54, "30ml");
-- 2
INSERT INTO `RecipeIngredient` VALUES (2, 29, "30ml");
INSERT INTO `RecipeIngredient` VALUES (2, 26, "30ml");
INSERT INTO `RecipeIngredient` VALUES (2, 48, "약간");
-- 3
INSERT INTO `RecipeIngredient` VALUES (3, 1, "30ml");
INSERT INTO `RecipeIngredient` VALUES (3, 17, "30ml");
INSERT INTO `RecipeIngredient` VALUES (3, 11, "30ml");
-- 4
INSERT INTO `RecipeIngredient` VALUES (4, 1, "45ml");
INSERT INTO `RecipeIngredient` VALUES (4, 16, "15ml");
INSERT INTO `RecipeIngredient` VALUES (4, 35, "15ml");
INSERT INTO `RecipeIngredient` VALUES (4, 15, "1바 스푼");
-- 5
INSERT INTO `RecipeIngredient` VALUES (5, 2, "52.5ml");
INSERT INTO `RecipeIngredient` VALUES (5, 41, "2티스푼");
INSERT INTO `RecipeIngredient` VALUES (5, 35, "22.5ml");
INSERT INTO `RecipeIngredient` VALUES (5, 37, "22.5ml");
-- 6
INSERT INTO `RecipeIngredient` VALUES (6, 33, "100ml");
INSERT INTO `RecipeIngredient` VALUES (6, 40, "50ml");
-- 7
INSERT INTO `RecipeIngredient` VALUES (7, 5, "30ml");
INSERT INTO `RecipeIngredient` VALUES (7, 10, "30ml");
INSERT INTO `RecipeIngredient` VALUES (7, 18, "30ml");
INSERT INTO `RecipeIngredient` VALUES (7, 35, "20ml");
-- 8
INSERT INTO `RecipeIngredient` VALUES (8, 4, "50ml");
INSERT INTO `RecipeIngredient` VALUES (8, 21, "20ml");
-- 9
INSERT INTO `RecipeIngredient` VALUES (9, 4, "45ml");
INSERT INTO `RecipeIngredient` VALUES (9, 38, "90ml");
INSERT INTO `RecipeIngredient` VALUES (9, 35, "15ml");
INSERT INTO `RecipeIngredient` VALUES (9, 50, "2대시");
INSERT INTO `RecipeIngredient` VALUES (9, 51, "취향껏");
INSERT INTO `RecipeIngredient` VALUES (9, 52, "취향껏");
INSERT INTO `RecipeIngredient` VALUES (9, 53, "취향껏");
-- 10
INSERT INTO `RecipeIngredient` VALUES (10, 7, "45ml");
INSERT INTO `RecipeIngredient` VALUES (10, 8, "45ml(버번 대체)");
INSERT INTO `RecipeIngredient` VALUES (10, 26, "30ml");
-- 11
INSERT INTO `RecipeIngredient` VALUES (11, 1, "50ml");
INSERT INTO `RecipeIngredient` VALUES (11, 35, "25ml");
INSERT INTO `RecipeIngredient` VALUES (11, 43, "12.5ml");
INSERT INTO `RecipeIngredient` VALUES (11, 22, "15ml");
-- 12
INSERT INTO `RecipeIngredient` VALUES (12, 9, "52.5ml");
INSERT INTO `RecipeIngredient` VALUES (12, 16, "7.5ml");
INSERT INTO `RecipeIngredient` VALUES (12, 23, "1바 스푼");
INSERT INTO `RecipeIngredient` VALUES (12, 35, "15ml");
INSERT INTO `RecipeIngredient` VALUES (12, 42, "1바 스푼");
INSERT INTO `RecipeIngredient` VALUES (12, 30, "2대시");
-- 13
INSERT INTO `RecipeIngredient` VALUES (13, 6, "60ml");
INSERT INTO `RecipeIngredient` VALUES (13, 56, "1개");
INSERT INTO `RecipeIngredient` VALUES (13, 45, "4 티스푼");
-- 14
INSERT INTO `RecipeIngredient` VALUES (14, 12, "60ml");
INSERT INTO `RecipeIngredient` VALUES (14, 36, "15ml");
INSERT INTO `RecipeIngredient` VALUES (14, 46, "15ml");
INSERT INTO `RecipeIngredient` VALUES (14, 49, "50ml");
-- 15
INSERT INTO `RecipeIngredient` VALUES (15, 1, "40ml");
INSERT INTO `RecipeIngredient` VALUES (15, 27, "20ml");
INSERT INTO `RecipeIngredient` VALUES (15, 29, "10ml");
-- 16
INSERT INTO `RecipeIngredient` VALUES (16, 3, "40ml");
INSERT INTO `RecipeIngredient` VALUES (16, 16, "10ml");
INSERT INTO `RecipeIngredient` VALUES (16, 35, "10ml");
INSERT INTO `RecipeIngredient` VALUES (16, 31, "2 대시");
-- 17
INSERT INTO `RecipeIngredient` VALUES (17, 34, "90ml");
INSERT INTO `RecipeIngredient` VALUES (17, 10, "10ml");
INSERT INTO `RecipeIngredient` VALUES (17, 32, "2 대시");
INSERT INTO `RecipeIngredient` VALUES (17, 20, "약간");
INSERT INTO `RecipeIngredient` VALUES (17, 47, "1개");
-- 18
INSERT INTO `RecipeIngredient` VALUES (18, 24, "45ml");
INSERT INTO `RecipeIngredient` VALUES (18, 39, "30ml");
INSERT INTO `RecipeIngredient` VALUES (18, 36, "22.5ml");
INSERT INTO `RecipeIngredient` VALUES (18, 25, "15ml");
-- 19
INSERT INTO `RecipeIngredient` VALUES (19, 1, "30ml");
INSERT INTO `RecipeIngredient` VALUES (19, 44, "15ml");
INSERT INTO `RecipeIngredient` VALUES (19, 35, "15ml");
INSERT INTO `RecipeIngredient` VALUES (19, 55, "약간");
-- 20
INSERT INTO `RecipeIngredient` VALUES (20, 1, "30ml");
INSERT INTO `RecipeIngredient` VALUES (20, 19, "30ml");
INSERT INTO `RecipeIngredient` VALUES (20, 28, "30ml");
INSERT INTO `RecipeIngredient` VALUES (20, 35, "30ml");
INSERT INTO `RecipeIngredient` VALUES (20, 13, "1 대시");

-- 칵테일 제작법 추가
-- 1
INSERT INTO `Recipe` VALUES (1, 1, "얼음 큐브로 채워진 칵테일 쉐이커에 모든 재료를 넣는다.");
INSERT INTO `Recipe` VALUES (2, 1, "잘 흔든다.");
INSERT INTO `Recipe` VALUES (3, 1, "차가운 칵테일 잔에 따른다.");
-- 2
INSERT INTO `Recipe` VALUES (4, 2, "얼음 큐브로 채워진 올드 패션드 글라스에 재료들을 직접 넣고 섞는다.");
INSERT INTO `Recipe` VALUES (5, 2, "소다 워터를 약간 넣는다.");
INSERT INTO `Recipe` VALUES (6, 2, "부드럽게 젓는다.");
-- 3
INSERT INTO `Recipe` VALUES (7, 3, "얼음 큐브로 채워진 칵테일 쉐이커에 모든 재료를 넣는다.");
INSERT INTO `Recipe` VALUES (8, 3, "잘 흔든다.");
INSERT INTO `Recipe` VALUES (9, 3, "차가운 칵테일 잔에 따른다.");
-- 4
INSERT INTO `Recipe` VALUES (10, 4, "모든 재료를 칵테일 쉐이커에 넣는다.");
INSERT INTO `Recipe` VALUES (11, 4, "조각 얼음과 함께 흔든다.");
INSERT INTO `Recipe` VALUES (12, 4, "차가운 칵테일 잔에 따른다.");
-- 5
INSERT INTO `Recipe` VALUES (13, 5, "꿀이 녹을 때까지 레몬 및 오렌지 주스와 함께 젓는다.");
INSERT INTO `Recipe` VALUES (14, 5, "진을 넣고 얼음과 함께 흔든다.");
INSERT INTO `Recipe` VALUES (15, 5, "차가운 칵테일 잔에 따른다.");
-- 6
INSERT INTO `Recipe` VALUES (16, 6, "복숭아 퓨레를 얼음과 함께 믹싱 글라스에 붓는다.");
INSERT INTO `Recipe` VALUES (17, 6, "프로세코 와인을 넣는다.");
INSERT INTO `Recipe` VALUES (18, 6, "부드럽게 젓는다.");
INSERT INTO `Recipe` VALUES (19, 6, "차가운 플루트 글라스에 따른다.");
-- 7
INSERT INTO `Recipe` VALUES (20, 7, "모든 재료를 칵테일 쉐이커에 넣는다.");
INSERT INTO `Recipe` VALUES (21, 7, "얼음과 함께 잘 흔든다.");
INSERT INTO `Recipe` VALUES (22, 7, "차가운 칵테일 잔에 따른다.");
-- 8
INSERT INTO `Recipe` VALUES (23, 8, "보드카와 커피 리큐르를 얼음 큐브로 채워진 올드 패션드 글라스에 붓는다.");
INSERT INTO `Recipe` VALUES (24, 8, "재료들을 부드럽게 젓는다.");
INSERT INTO `Recipe` VALUES (25, 8, "혼합물을 얼음이 채워진 동일한 올드 패션드 글라스에 따른다.");
-- 9
INSERT INTO `Recipe` VALUES (26, 9, "모든 재료를 얼음과 함께 믹싱 글라스에서 부드럽게 젓는다.");
INSERT INTO `Recipe` VALUES (27, 9, "락 글라스에 따른다.");
INSERT INTO `Recipe` VALUES (28, 9, "참고: 얼음과 함께 제공하도록 요청받으면 하이볼 글라스에 따른다.");
-- 10
INSERT INTO `Recipe` VALUES (29, 10, "모든 재료를 얼음 큐브로 채워진 믹싱 글라스에 붓는다.");
INSERT INTO `Recipe` VALUES (30, 10, "잘 젓는다.");
INSERT INTO `Recipe` VALUES (31, 10, "차가운 칵테일 잔에 따른다.");
-- 11
INSERT INTO `Recipe` VALUES (32, 11, "크렘 드 뮤르를 제외한 모든 재료를 칵테일 쉐이커에 붓는다.");
INSERT INTO `Recipe` VALUES (33, 11, "얼음과 함께 잘 흔든다.");
INSERT INTO `Recipe` VALUES (34, 11, "조각 얼음으로 채워진 차가운 올드 패션드 글라스에 따른다.");
INSERT INTO `Recipe` VALUES (35, 11, "음료 위에 블랙베리 리큐르(크렘 드 뮤르)를 원을 그리며 붓는다.");
-- 12
INSERT INTO `Recipe` VALUES (36, 12, "모든 재료를 얼음 큐브와 함께 믹싱 글라스에서 섞는다.");
INSERT INTO `Recipe` VALUES (37, 12, "준비된 슬림 칵테일 글라스에 따른다.");
INSERT INTO `Recipe` VALUES (38, 12, "오렌지(또는 레몬) 슬라이스로 글라스의 가장자리를 문지른다.");
INSERT INTO `Recipe` VALUES (39, 12, "글라스 가장자리에 가루 설탕을 묻혀 붙도록 한다.");
INSERT INTO `Recipe` VALUES (40, 12, "오렌지 또는 레몬 껍질을 조심스럽게 말아 글라스 안쪽에 놓는다.");
-- 13
INSERT INTO `Recipe` VALUES (41, 13, "라임과 설탕을 더블 올드 패션드 글라스에 넣는다.");
INSERT INTO `Recipe` VALUES (42, 13, "부드럽게 머들링한다.");
INSERT INTO `Recipe` VALUES (43, 13, "글라스에 조각 얼음을 채운다.");
INSERT INTO `Recipe` VALUES (44, 13, "카샤사를 넣는다.");
INSERT INTO `Recipe` VALUES (45, 13, "재료가 섞이도록 부드럽게 젓는다.");
-- 14
INSERT INTO `Recipe` VALUES (46, 14, "꿀을 물, 라임 주스와 섞어 글라스 바닥과 옆면에 바른다.");
INSERT INTO `Recipe` VALUES (47, 14, "조각 얼음을 넣고 럼을 넣는다.");
INSERT INTO `Recipe` VALUES (48, 14, "바닥에서 위로 힘차게 저어 마무리한다.");
-- 15
INSERT INTO `Recipe` VALUES (49, 15, "모든 재료를 얼음 큐브가 담긴 믹싱 글라스에 붓는다.");
INSERT INTO `Recipe` VALUES (50, 15, "잘 젓는다.");
INSERT INTO `Recipe` VALUES (51, 15, "차가운 칵테일 잔에 따른다.");
-- 16
INSERT INTO `Recipe` VALUES (52, 16, "모든 재료를 칵테일 쉐이커에 붓는다.");
INSERT INTO `Recipe` VALUES (53, 16, "얼음과 함께 잘 흔든다.");
INSERT INTO `Recipe` VALUES (54, 16, "얼음으로 채워진 차가운 락 글라스에 따른다.");
-- 17
INSERT INTO `Recipe` VALUES (55, 17, "큰 샴페인 글라스에 각설탕과 비터스 2대시를 넣는다.");
INSERT INTO `Recipe` VALUES (56, 17, "꼬냑을 넣는다.");
INSERT INTO `Recipe` VALUES (57, 17, "차가운 샴페인을 부드럽게 붓는다.");
-- 18
INSERT INTO `Recipe` VALUES (58, 18, "모든 재료를 긴 글라스에 붓는다.");
INSERT INTO `Recipe` VALUES (59, 18, "페블 아이스를 글라스에 넣는다.");
INSERT INTO `Recipe` VALUES (60, 18, "스위즐 스틱이나 칵테일 스푼을 사용하여 재료를 힘차게 섞는다.");
INSERT INTO `Recipe` VALUES (61, 18, "글라스에 페블 아이스를 더 채워 음료를 완성한다.");
-- 19
INSERT INTO `Recipe` VALUES (62, 19, "모든 재료를 칵테일 쉐이커에 붓고 얼음과 함께 잘 흔든다.");
INSERT INTO `Recipe` VALUES (63, 19, "차가운 칵테일 잔에 따른다.");
-- 20
INSERT INTO `Recipe` VALUES (64, 20, "모든 재료를 얼음과 함께 쉐이커에 넣는다.");
INSERT INTO `Recipe` VALUES (65, 20, "잘 흔든다.");
INSERT INTO `Recipe` VALUES (66, 20, "차가운 칵테일 잔에 따른다.");
