/* -- Estrutura da tabela para visualização
CREATE TABLE categories(
	id NUMERIC PRIMARY KEY,
  	name VARCHAR(255)
);

CREATE TABLE products(
	id NUMERIC PRIMARY KEY,
  	name VARCHAR(255),
  	amount NUMERIC,
  	price NUMERIC,
  	id_categories NUMERIC,
  	CONSTRAINT fk_id_categories FOREIGN KEY(id_categories) REFERENCES categories(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE
);

INSERT INTO categories VALUES
    (1,	'Wood'),
    (2,	'Luxury'),
    (3,	'Vintage'),
    (4, 'Modern'),
    (5, 'Super Luxury');


INSERT INTO products VALUES
    (1, 'Two-doors wardrobe', 100, 800.00, 1),
    (2, 'Dining Table', 1000, 570.00, 3),
    (3, 'Tower Holder', 10000, 25.50, 4),
    (4, 'Desk Computer', 350, 320.50, 2),
    (5, 'Chair', 3000, 210.64, 4),
    (6,'Single Bed', 750, 460.00, 1);
*/



select
    categories.name,
    SUM(products.amount)
from products
join categories
on products.id_categories = categories.id
group by categories.name;
