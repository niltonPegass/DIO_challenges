-- SCRIPT PARA CRIAÇÃO DO BANCO DE DADOS  -- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- E-COMMERCE  -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- DROP DATABASE ECOMMERCE;
CREATE DATABASE ECOMMERCE;
USE ECOMMERCE;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- DROP TABLE CLIENTS;
CREATE TABLE CLIENTS (
    ID_CLIENT INT AUTO_INCREMENT PRIMARY KEY,
    ID_CREDIT_CARD INT,
    FNAME VARCHAR(10) NOT NULL,
    MINIT CHAR(3) NOT NULL,
    LNAME VARCHAR(20) NOT NULL,
    CPF CHAR(11) NOT NULL,
    ADDRESS VARCHAR(255) NOT NULL,
    BIRTH_DATE DATE NOT NULL,
    CONSTRAINT UNIQUE_CPF_CLIENT UNIQUE (CPF)
    -- , CONSTRAINT FK_CREDIT_CARD FOREIGN KEY (ID_CREDIT_CARD) REFERENCES CREDIT_CARD(ID_CREDIT_CARD)
);

ALTER TABLE CLIENTS AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- DROP TABLE PRODUCTS;
CREATE TABLE PRODUCTS (
	ID_PRODUCT INT AUTO_INCREMENT PRIMARY KEY,
    PNAME VARCHAR(100) NOT NULL,
    CLASSIFICATION_KIDS BOOL DEFAULT FALSE,
    CATEGORY ENUM('ELETRÔNICO', 'CASA', 'VESTUÁRIO', 'BRINQUEDO', 'ALIMENTO', 'OUTRA') NOT NULL,
    RATING ENUM('5', '4', '3', '2', '1'),
    PRICE FLOAT
);
-- [PRODUCTS] RETORNOU WARNING AO DETERMINAR NUMERO DE CASAS PARA VARIAVEL FLOAT
-- EM VERSÕES FUTURAS ESSA OPCAO SERA DESCONTINUADA

ALTER TABLE PRODUCTS AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- DROP TABLE PAYMENT_CASH
CREATE TABLE PAYMENT_CASH (
    ID_PAYMENT_CASH INT AUTO_INCREMENT PRIMARY KEY,
    PAYMENT_CASH_NUMBER CHAR(48) NOT NULL,
    TERM DATE NOT NULL,
    CONSTRAINT UNIQUE_PAYMENT_CASH_NUMBER UNIQUE (PAYMENT_CASH_NUMBER)
);

ALTER TABLE PAYMENT_CASH AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE ORDERS (
	ID_ORDER INT AUTO_INCREMENT PRIMARY KEY,
    ID_CLIENT INT NOT NULL,
    ORDER_STATUS ENUM('EM PROCESSAMENTO', 'CONFIRMADO', 'CANCELADO') DEFAULT 'EM PROCESSAMENTO',
    ORDER_DESCRIPTION VARCHAR(255),
    SEND_PRICE FLOAT NOT NULL DEFAULT 13.99,
    PAYMENT_CASH BOOL DEFAULT FALSE,
    CONSTRAINT FK_ORDER_CLIENT FOREIGN KEY (ID_CLIENT) REFERENCES CLIENTS(ID_CLIENT)
    -- , CONSTRAINT FK_ORDER_PAYMENT FOREIGN KEY (ID_ORDER) REFERENCES PAYMENTS(ID_ORDER) [CONSTRAINT REDUNDANTE (?) ID_ORDER EM PAYMENTS] 
);
-- [!] [ORDERS] MODIFICAR COM ALTER TABLE E ADICIONAR CONSTRAINT FOREIGN KEY [!]

ALTER TABLE ORDERS AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- DROP TABLE PAYMENTS;
CREATE TABLE PAYMENTS (
	ID_PAYMENT INT AUTO_INCREMENT,
    ID_ORDER INT NOT NULL,
    ID_PAYMENT_CASH INT,
    TYPE_PAYMENT ENUM('BOLETO', 'CARTÃO', 'DOIS CARTÕES') DEFAULT 'CARTÃO',
    PRIMARY KEY (ID_PAYMENT, ID_ORDER, ID_PAYMENT_CASH),
    CONSTRAINT FK_PAYMENT_1 FOREIGN KEY (ID_PAYMENT_CASH) REFERENCES PAYMENT_CASH(ID_PAYMENT_CASH),
    CONSTRAINT FK_PAYMENT_2 FOREIGN KEY (ID_ORDER) REFERENCES ORDERS(ID_ORDER)
);

ALTER TABLE PAYMENTS AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE CREDIT_CARD (
    ID_CREDIT_CARD INT AUTO_INCREMENT PRIMARY KEY,
    FLAG ENUM('VISA', 'MASTERCARD', 'AMERICAN EXPRESS', 'OUTRO') NOT NULL,
    CARD_NUMBER CHAR(16) NOT NULL,
    VALIDITY DATE NOT NULL,
    VERIFICATION_CODE CHAR(3) NOT NULL,
    CARDHOLDER_NAME VARCHAR(45) NOT NULL,
    CONSTRAINT UNIQUE_CARD_NUMBER UNIQUE (CARD_NUMBER)
);
-- [!] [CREDIT_CARD] MODIFICAR COM ALTER TABLE E ADICIONAR CONSTRAINT FOREIGN KEY [!]

ALTER TABLE CREDIT_CARD AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

ALTER TABLE CLIENTS
ADD CONSTRAINT FK_CREDIT_CARD FOREIGN KEY (ID_CREDIT_CARD) REFERENCES CREDIT_CARD(ID_CREDIT_CARD);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PAYMENT_CREDIT_CARD (
    ID_ORDER INT NOT NULL,
    ID_CREDIT_CARD INT,
    PRIMARY KEY (ID_ORDER, ID_CREDIT_CARD),
    CONSTRAINT FK_PAYMENT_CARD_1 FOREIGN KEY (ID_ORDER) REFERENCES PAYMENTS(ID_ORDER),
    CONSTRAINT FK_PAYMENT_CARD_2 FOREIGN KEY (ID_CREDIT_CARD) REFERENCES CREDIT_CARD(ID_CREDIT_CARD)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PRODUCT_STORAGE (
	ID_PROD_STORAGE INT AUTO_INCREMENT PRIMARY KEY,
    STORAGE_LOCATION VARCHAR(255),
    QUANTITY INT DEFAULT 0,
    RACK VARCHAR(20)
);

ALTER TABLE PRODUCT_STORAGE AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE SUPPLIER (
	ID_SUPPLIER INT AUTO_INCREMENT PRIMARY KEY,
    SOCIAL_NAME VARCHAR(255) NOT NULL,
    CNPJ CHAR(15) NOT NULL,
    CONTACT CHAR(11) NOT NULL,
    EMAIL VARCHAR(45),
    CONSTRAINT UNIQUE_SUPPLIER UNIQUE (CNPJ)
);

ALTER TABLE SUPPLIER AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE SELLER (
	ID_SELLER INT AUTO_INCREMENT PRIMARY KEY,
    SOCIAL_NAME VARCHAR(255) NOT NULL,
    ABST_NAME VARCHAR(255),
    CNPJ CHAR(15),
    CPF CHAR(9),
    LOCATIONS VARCHAR(255),
    CONTACT CHAR(11) NOT NULL,
    EMAIL VARCHAR(45),
    CONSTRAINT UNIQUE_CNPJ_SELLER UNIQUE (CNPJ),
    CONSTRAINT UNIQUE_CPF_SELLER UNIQUE (CPF)
);

ALTER TABLE SELLER AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PRODUCT_SELLER (
	ID_PSELLER INT,
    ID_PPRODUCT INT,
    PRODQUANTITY INT DEFAULT 1,
    PRIMARY KEY (ID_PSELLER, ID_PPRODUCT),
    CONSTRAINT FK_PRODUCT_SELLER FOREIGN KEY (ID_PSELLER) REFERENCES SELLER(ID_SELLER),
    CONSTRAINT FK_PRODUCT_PRODUCT FOREIGN KEY (ID_PPRODUCT) REFERENCES PRODUCTS(ID_PRODUCT)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PRODUCT_ORDER (
	ID_POPRODUCT INT,
    ID_POORDER INT,
    PO_QUANTITY INT DEFAULT 1,
    PO_STATUS ENUM('DISPONÍVEL', 'SEM ESTOQUE') DEFAULT 'DISPONÍVEL',
    PRIMARY KEY (ID_POPRODUCT, ID_POORDER),
    CONSTRAINT FK_PRODUCTORDER_PRODUCT FOREIGN KEY (ID_POPRODUCT) REFERENCES PRODUCTS(ID_PRODUCT),
    CONSTRAINT FK_PRODUCTORDER_ORDER FOREIGN KEY (ID_POORDER) REFERENCES ORDERS(ID_ORDER)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE STORAGE_LOCATION (
	ID_LPRODUCT INT,
    ID_LSTORAGE INT,
    LOCATION VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID_LPRODUCT, ID_LSTORAGE),
    CONSTRAINT FK_STORAGE_LOCATION_PRODUCT FOREIGN KEY (ID_LPRODUCT) REFERENCES PRODUCTS(ID_PRODUCT),
    CONSTRAINT FK_STORAGE_LOCATION_STORAGE FOREIGN KEY (ID_LSTORAGE) REFERENCES PRODUCT_STORAGE(ID_PROD_STORAGE)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PRODUCT_SUPPLIER (
	ID_PSSUPPLIER INT,
    ID_PSPRODUCT INT,
    QUANTITY INT NOT NULL,
    PRIMARY KEY (ID_PSSUPPLIER, ID_PSPRODUCT),
    CONSTRAINT FK_PRODUCT_SUPPLIER_SUPPLIER FOREIGN KEY (ID_PSSUPPLIER) REFERENCES SUPPLIER(ID_SUPPLIER),
    CONSTRAINT FK_PRODUCT_SUPPLIER_PRODCUT FOREIGN KEY (ID_PSPRODUCT) REFERENCES PRODUCTS(ID_PRODUCT)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE BATCH (
    ID_BATCH INT AUTO_INCREMENT PRIMARY KEY,
    BATCH_NUMBER VARCHAR(255) NOT NULL,
    VALIDITY DATE,
    OBSERVATION VARCHAR(255)
);

ALTER TABLE BATCH AUTO_INCREMENT=1;

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE TABLE PRODUCT_BATCH (
    ID_PRODUCT INT,
    ID_BATCH INT,
    PRIMARY KEY(ID_PRODUCT, ID_BATCH),
    CONSTRAINT FK_PRODUCT_BATCH_1 FOREIGN KEY (ID_BATCH) REFERENCES BATCH(ID_BATCH),
    CONSTRAINT FK_PRODUCT_BATCH_2 FOREIGN KEY (ID_PRODUCT) REFERENCES PRODUCTS(ID_PRODUCT)
);

-- -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- SHOW DATABASES;
-- USE INFORMATION_SCHEMA;
-- SHOW TABLES;
-- DESC REFERENTIAL_CONSTRAINTS;
-- SELECT * FROM REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA = 'ECOMMERCE';