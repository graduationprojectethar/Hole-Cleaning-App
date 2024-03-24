create database Mydb;
use Mydb;
create table flow_rate(
n int,
MD_m float,
cuttings_size_in float,
cuttings_density float,
Estimated_TR float,
Optimal_Q_gpm float,
Enhanced_TR float
);

select * from flow_rate;

SET SQL_SAFE_UPDATES = 0;
delete from flow_rate;