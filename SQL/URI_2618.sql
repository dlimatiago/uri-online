/* -- Estrutura da tabela para visualização
CREATE TABLE categories(
	id NUMERIC PRIMARY KEY,
  	name VARCHAR(255)
);
CREATE TABLE providers(
	id NUMERIC PRIMARY KEY,
  	name VARCHAR(255),
  	street VARCHAR(255),
  	city VARCHAR(255),
  	state VARCHAR(255)
);
CREATE TABLE products(
	id NUMERIC PRIMARY key,
  	name VARCHAR(255),
  	amount NUMERIC,
  	price NUMERIC,
  	id_providers NUMERIC,
  	id_categories NUMERIC,
  	CONSTRAINT fk_id_providers FOREIGN KEY(id_providers) REFERENCES providers(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE,
  	CONSTRAINT fk_id_categories FOREIGN KEY(id_categories) REFERENCES categories(id)
  	ON DELETE CASCADE
  	ON UPDATE CASCADE
);
INSERT INTO providers VALUES
    (1, 'Ajax SA', 'Rua Presidente Castelo Branco', 'Porto Alegre',	'RS'),
    (2, 'Sansul SA', 'Av Brasil', 'Rio de Janeiro', 'RJ'),
    (3,	'South Chairs', 'Rua do Moinho', 'Santa Maria', 'RS'),
    (4, 'Elon Electro', 'Rua Apolo', 'São Paulo', 'SP'),
    (5,	'Mike Electro',	'Rua Pedro da Cunha', 'Curitiba', 'PR');

INSERT INTO categories VALUES
    (1,	'Super Luxury'),
    (2,	'Imported'),
    (3,	'Tech'),
    (4, 'Vintage'),
    (5, 'Supreme');


INSERT INTO products VALUES
    (1, 'Blue Chair', 30, 300.00, 5, 5),
    (2, 'Red Chair', 50, 2150.00, 2, 1),
    (3, 'Disney Wardrobe', 400, 829.50, 4, 1),
    (4, 'Blue Toaster', 20, 9.90, 3, 1),
    (5, 'TV', 30, 3000.25, 2, 2);
*/

select
	prod.name,
    prov.name,
    cat.name
from products as prod
JOIN providers as prov
on prov.id = prod.id_providers
join categories as cat
on cat.id = prod.id_categories
where prov.name = 'Sansul SA'
	and cat.name = 'Imported';

