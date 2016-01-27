drop table if exists notes;
create table notes (
    id integer primary key autoincrement,
    username text not null,
    text text not null,
    pub_date integer
    );
