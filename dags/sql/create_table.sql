CREATE TABLE IF NOT EXISTS exchangerates
(
    id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
    btc NUMERIC(19,6),
    sys_create_datetime timestamp without time zone DEFAULT (now() AT TIME ZONE 'utc')
); 