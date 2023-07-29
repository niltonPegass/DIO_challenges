-- INSERÇÃO DE DADOS NO BANCO -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

USE ECOMMERCE;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_PRODUCT, PNAME, CLASSIFICATION_KIDS BOOLEAN, CATEGORY('ELETRÔNICO','VESTUÁRIO','BRINQUEDO','ALIMENTO','OUTRA'), AVALIAÇÃO, SIZE
INSERT INTO PRODUCTS (PNAME, CLASSIFICATION_KIDS, CATEGORY, RATING, PRICE) VALUES
	('FONE DE OUVIDO',DEFAULT,'ELETRÔNICO','4',100),
	('BARBIE ELSA',TRUE,'BRINQUEDO','3',80),
	('BODY CARTERS',TRUE,'VESTUÁRIO','5',80),
	('MICROFONE VEDO - YOUTUBER',FALSE,'ELETRÔNICO','4',200),
	('SOFÁ RETRÁTIL',DEFAULT,'OUTRA','3',2000),
	('FARINHA DE ARROZ',DEFAULT,'ALIMENTO','2',5),
	('FIRE STICK AMAZON',FALSE,'ELETRÔNICO','3',250);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- FLAG (ENUM), CARD_NUMBER, VALIDITY, VERIFICATION_CODE, CARDHOLDER_NAME
INSERT INTO CREDIT_CARD (FLAG, CARD_NUMBER, VALIDITY, VERIFICATION_CODE, CARDHOLDER_NAME) VALUES
	('OUTRO',0000000000000000, '2100-12-31',000,''),
    ('VISA',1111222233334444,'2028-05-12',233,'MARIA M SILVA'),
    ('VISA',2222111155559999,'2029-12-25',194,'RICADO F SILVA'),
    ('MASTERCARD',1234876543211234,'2027-01-03',923,'JULIA S FRANÇA'),
    ('AMERICAN EXPRESS',8765146798660011,'2033-12-31',772,'ISABELA M CRUZ');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_CREDIT_CARD, FNAME, MINIT, LNAME, CPF, ADDRESS, BIRTH_DATE
INSERT INTO CLIENTS (ID_CREDIT_CARD, FNAME, MINIT, LNAME, CPF, ADDRESS, BIRTH_DATE) VALUES
	(1, 'MARIA','M','SILVA', 12346789, 'RUA SILVA DE PRATA 29, CARANGOLA - CIDADE DAS FLORES', "1995-05-19"),
	(NULL, 'MATHEUS','O','PIMENTEL', 987654321,'RUA ALEMEDA 289, CENTRO - CIDADE DAS FLORES', "1998-05-23"),
	(2, 'RICARDO','F','SILVA', 45678913,'AVENIDA ALEMEDA VINHA 1009, CENTRO - CIDADE DAS FLORES', "1986-01-04"),
	(3, 'JULIA','S','FRANÇA', 789123456,'RUA LAREIJRAS 861, CENTRO - CIDADE DAS FLORES', "1994-05-12"),
	(NULL, 'ROBERTA','G','ASSIS', 98745631,'AVENIDADE KOLLER 19, CENTRO - CIDADE DAS FLORES', "1995-09-19"),
	(4, 'ISABELA','M','CRUZ', 654789123,'RUA ALEMEDA DAS FLORES 28, CENTRO - CIDADE DAS FLORES', "2001-07-23");

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM CLIENTS;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_CLIENT, ORDER_STATUS (ENUM), ORDER_DESCRIPTION, SEND_PRICE, PAYMENT_CASH (BOOL)
INSERT INTO ORDERS (ID_CLIENT, ORDER_STATUS, ORDER_DESCRIPTION, SEND_PRICE, PAYMENT_CASH) VALUES
	(1,DEFAULT,'COMPRA VIA APLICATIVO',15,0),
	(3,DEFAULT,'COMPRA VIA APLICATIVO',50,1),
	(4,'CONFIRMADO','COMPRA VIA APLICATIVO',15,1),
	(6,DEFAULT,'COMPRA VIA WEB SITE',150,0);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM CLIENTS;
-- SELECT * FROM PRODUCTS;
-- SELECT * FROM ORDERS;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_POPRODUCT, ID_POORDER, PO_QUANTITY, PO_STATUS (ENUM)
INSERT INTO PRODUCT_ORDER (ID_POPRODUCT, ID_POORDER, PO_QUANTITY, PO_STATUS) VALUES
	(1,1,2,DEFAULT),
	(4,1,1,DEFAULT),
	(5,2,1,DEFAULT),
    (5,4,1,DEFAULT),
    (6,4,1,DEFAULT);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- STORAGE_LOCATION,QUANTITY
INSERT INTO PRODUCT_STORAGE (STORAGE_LOCATION, QUANTITY, RACK) VALUES 
	('SÃO PAULO',10,'SP20'),
	('SÃO PAULO',100,'SP20'),
	('SÃO PAULO',10,'SP10'),
	('BRASÍLIA',60,'BR10'),
	('RIO DE JANEIRO',1000,'RJ20'),
	('RIO DE JANEIRO',500,'RJ10');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

SELECT * FROM PRODUCTS;
SELECT * FROM PRODUCT_STORAGE;

-- ID_LPRODUCT, ID_LSTORAGE, LOCATION
INSERT INTO STORAGE_LOCATION (ID_LPRODUCT, ID_LSTORAGE, LOCATION) VALUES
	(1,2,'RJ'),
	(2,6,'GO');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SOCIAL_NAME, CNPJ, CONTACT, EMAIL
INSERT INTO SUPPLIER (SOCIAL_NAME, CNPJ, CONTACT, EMAIL) VALUES
	('ALMEIDA E FILHOS', 123456789123456,'21985474', 'CONTATO_1@OUTLOOK.COM'),
	('ELETRÔNICOS SILVA',854519649143457,'21985484', 'CONTATO_2@OUTLOOK.COM'),
	('ELETRÔNICOS VALMA', 934567893934695,'21975474', NULL);
                            
-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --                            

-- SELECT * FROM SUPPLIER;
-- SELECT * FROM PRODUCTS;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_PSSUPPLIER, ID_PSPRODUCT, QUANTITY
INSERT INTO PRODUCT_SUPPLIER (ID_PSSUPPLIER, ID_PSPRODUCT, QUANTITY) VALUES
	(1,1,500),
	(1,2,400),
	(2,4,633),
	(3,3,5),
	(2,5,10);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SOCIAL_NAME, ABST_NAME, CNPJ, CPF, LOCATIONS, CONTACT, EMAIL
INSERT INTO SELLER (SOCIAL_NAME, ABST_NAME, CNPJ, CPF, LOCATIONS, CONTACT, EMAIL) VALUES
	('TECH ELETRONICS', NULL, 123456789456321, NULL, 'RIO DE JANEIRO', 219946287, 'S1@MAIL.COM'),
	('BOTIQUE DURGAS',NULL,NULL,123456783,'RIO DE JANEIRO', 219567895, 'S2@MAIL.COM'),
	('KIDS WORLD',NULL,456789123654485,NULL,'SÃO PAULO', 1198657484, 'S3@MAIL.COM');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM SELLER;
-- SELECT * FROM PRODUCT;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_PSELLER, ID_PPRODUCT, PRODQUANTITY
INSERT INTO PRODUCT_SELLER (ID_PSELLER, ID_PPRODUCT, PRODQUANTITY) VALUES
	(1,6,80),
	(2,7,10);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- BATCH_NUMBER, VALIDITY, OBSERVATION
INSERT INTO BATCH (BATCH_NUMBER, VALIDITY, OBSERVATION) VALUES
	(202309,'2026-12-31',NULL),
    (202303,'2026-12-31',NULL),
    (202301,'2026-05-28',NULL);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM PRODUCTS;
-- SELECT * FROM BATCH;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_PRODUCT, ID_BATCH
INSERT INTO PRODUCT_BATCH (ID_PRODUCT, ID_BATCH) VALUES
	(1,2),
    (2,2),
    (3,2),
    (4,1),
    (5,3),
    (6,3),
    (7,3);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- PAYMENT_CASH_NUMBER, TERM
INSERT INTO PAYMENT_CASH (PAYMENT_CASH_NUMBER, TERM) VALUES
	(000000000000000000000000000000000000000000000000, '2100-12-31'),
    (123456789012345678901234567890123456789012345678, '2023-08-10'),
	(098765432109876543210987654321098765432109876543, '2023-08-13');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM ORDERS;
-- SELECT * FROM PAYMENT_CASH;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_ORDER, ID_PAYMENT_CASH, TYPE_PAYMENT (ENUM)
INSERT INTO PAYMENTS (ID_ORDER, ID_PAYMENT_CASH, TYPE_PAYMENT) VALUES
	(1,1,'BOLETO'),
	(2,6,'CARTÃO'), -- BOLETO 0000 // UTILIZANDO CARTÃO
    (3,6,'CARTÃO'), -- BOLETO 0000 // UTILIZANDO CARTÃO
    (4,2,'BOLETO');

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SELECT * FROM ORDERS;
-- SELECT * FROM CREDIT_CARD;
-- SELECT * FROM PAYMENTS;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- ID_ORDER, ID_CREDIT_CARD
INSERT INTO PAYMENT_CREDIT_CARD (ID_ORDER, ID_CREDIT_CARD) VALUES
	(1,5),
    (2,1),
    (3,4),
    (4,5);