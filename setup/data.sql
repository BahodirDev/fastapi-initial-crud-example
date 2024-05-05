

create table users(
    id BIGSERIAL PRIMARY KEY,
    username varchar(25),
    email varchar(25),
    password varchar(60),
    is_staff boolean default false,
    is_active boolean default true
);