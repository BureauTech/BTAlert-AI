create database if not exists btalert;
use btalert;

create user if not exists 'app_btalert'@'localhost' IDENTIFIED BY 'k!w^=An)KQtJwZ:Wa"n@_=8S';
grant select, insert, update, delete on btalert.* TO 'app_btalert'@'localhost';

create table if not exists test (
	tes_cod bigint unsigned not null auto_increment,
	tes_text text not null,
	primary key (tes_cod)
);
