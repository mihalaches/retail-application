CREATE TABLE "customers" (
  "cid" int PRIMARY KEY,
  "email" varchar(255) UNIQUE NOT NULL,
  "role" int NOT NULL,
  "first_name" varchar(255) NOT NULL,
  "last_name" varchar(255) NOT NULL,
  "password" varchar(255) NOT NULL,
  "registerd_date" date NOT NULL,
  "country" varchar(255) NOT NULL,
  "phone_number" int NOT NULL,
  "vat" decimal NOT NULL
);

CREATE TABLE "deposit" (
  "id" int PRIMARY KEY,
  "user_cid" int UNIQUE NOT NULL,
  "amount" decimal NOT NULL,
  "sync_date" date NOT NULL
);

CREATE TABLE "customers_address" (
  "id" int PRIMARY KEY,
  "user_cid" int UNIQUE NOT NULL,
  "country" varchar(255) NOT NULL,
  "city" varchar(255) NOT NULL,
  "phone_number" int NOT NULL,
  "full_address" varchar(255) NOT NULL
);

CREATE TABLE "products" (
  "id" int PRIMARY KEY,
  "product_name" varchar(255) NOT NULL,
  "product_category" int NOT NULL,
  "product_price" decimal NOT NULL,
  "guaranty" date NOT NULL,
  "product_details" varchar(255) NOT NULL,
  "product_image" varchar(500) NOT NULL
);

CREATE TABLE "customers_orders" (
  "id" int PRIMARY KEY,
  "user_cid" int NOT NULL,
  "products" int NOT NULL
);

CREATE TABLE "products_category" (
  "id" int PRIMARY KEY,
  "category_name" varchar(255) NOT NULL
);

CREATE TABLE "roles" (
  "id" int PRIMARY KEY,
  "role_name" varchar(255) NOT NULL
);

ALTER TABLE "customers" ADD FOREIGN KEY ("role") REFERENCES "roles" ("id");

ALTER TABLE "deposit" ADD FOREIGN KEY ("user_cid") REFERENCES "customers" ("cid");

ALTER TABLE "customers_address" ADD FOREIGN KEY ("user_cid") REFERENCES "customers" ("cid");

ALTER TABLE "products" ADD FOREIGN KEY ("product_category") REFERENCES "products_category" ("id");

ALTER TABLE "customers_orders" ADD FOREIGN KEY ("user_cid") REFERENCES "customers" ("cid");

ALTER TABLE "customers_orders" ADD FOREIGN KEY ("products") REFERENCES "products" ("id");
