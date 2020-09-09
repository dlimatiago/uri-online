/* -- Estrurura do banco
CREATE TABLE customers(
	id NUMERIC PRIMARY KEY,
  	name VARCHAR(255),
  	street VARCHAR(255),
  	city VARCHAR(255),
  	state VARCHAR(255),
  	credit_limit NUMERIC
);
CREATE TABLE orders(
	id numeric PRIMARY key,
  	orders_date date,
  	id_customers numeric,
  	CONSTRAINT fk_id_customers FOREIGN KEY(id_customers) REFERENCES customers(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE
);
INSERT INTO customers VALUES
    (1,	'Nicolas Diogo Cardoso', 'Acesso Um', 'Porto Alegre', 'RS', 475),
    (2,	'Cecília Olivia Rodrigues', 'Rua Sizuka Usuy', 'Cianorte', 'PR', 3170),
    (3,	'Augusto Fernando Carlos Eduardo Cardoso', 'Rua Baldomiro Koerich',	'Palhoça', 'SC', 1067),
    (4,	'Nicolas Diogo Cardoso', 'Acesso Um', 'Porto Alegre', 'RS', 475),
    (5,	'Sabrina Heloisa Gabriela Barros', 'Rua Engenheiro Tito Marques Fernandes', 'Porto Alegre', 'RS', 4312),
    (6,	'Joaquim Diego Lorenzo Araújo', 'Rua Vitorino', 'Novo Hamburgo', 'RS', 2314);
INSERT INTO orders VALUES
    (1, '2016-05-13', 3),
    (2, '2016-01-12', 2),
    (3,	'2016-04-18', 5),
    (4,	'2016-09-07', 4),
    (5, '2016-02-13', 6),
    (6,	'2016-08-05', 3);
*/

select
	cus.name,
    ord.id
from customers as cus
join orders as ord
on cus.id = ord.id_customers
where ord.orders_date BETWEEN '2016-01-01' and '2016-06-30';