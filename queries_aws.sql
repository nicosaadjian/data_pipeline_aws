create table testeo_mssql (
    id_intento int identity(1,1) primary key,
    descripcion varchar(50),
    time_stamp TIMESTAMP
);

insert into testeo_mssql (descripcion) values ('primera prueba');

select * from testeo_mssql;