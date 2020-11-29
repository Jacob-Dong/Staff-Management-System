CREATE TRIGGER check_aid BEFORE insert ON sys_admin
FOR each row
BEGIN
    if NEW.aId<1000 then
              rollback tran
		end if
END


mysql> delimiter //
mysql> CREATE TRIGGER upd_check BEFORE UPDATE ON account
   -> FOR EACH ROW
   -> BEGIN
   -> IF NEW.amount < 0 THEN
   -> SET NEW.amount = 0;
   -> ELSEIF NEW.amount > 100 THEN
   -> SET NEW.amount = 100;
   -> END IF;
   -> END;//
mysql> delimiter ;

`aId` int(3) NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `aName` varchar(10) NOT NULL COMMENT '管理员姓名',
  `aPwd` varchar(32) NOT NULL COMMENT '管理员密码',
  `aTel` varchar(15) NOT NULL COMMENT '管理员手机',
  `aEmail` varchar(40) NOT NULL COMMENT '管理员邮箱',
  `aDep` char(20) NOT NULL COMMENT '管理员的部门',
  `aPosition` c

insert into sys_admin values(1000,'a','a','a','a','a','a');
insert into department values(1,'a','a','a','a','a');
insert into checking_in values(1,'a','a','a','1000-01-01');
insert into monthrecord values(1,'a','1000/01/01',1,'1');

create trigger check_aid BEFORE insert
on sys_admin for each ROW
begin
if(NEW.aId<1000) then
delete from sys_admin where aId=NEW.aId;
end IF;
END

create trigger sta_de_sys_sa AFTER delete
on staff for each ROW
begin
delete from salary where staId=Old.stId;
delete from sys_staff where staId=Old.stId;
END

create trigger sta_in_sys_sa after insert
on staff for each ROW
begin
DECLARE id int;
DECLARE sal int;
DECLARE nam varchar(10);
SET id=NEW.stId;
SET sal=NEW.stSalary;
SET nam=NEW.stName;
insert into sys_staff values(id,id);
insert into salary(staId,staName,origin_salary) values(id,nam,sal);
END 

create trigger de_de_sta before delete
on department for each ROW
begin
DECLARE count INT(3);
SET count=(SELECT COUNT(*) FROM staff WHERE stDid=OLD.dId);
if(count>0) then
insert into department values(OLD.dId,OLD.dName,OLD.dDirector,OLD.dDirectorTel,OLD.dDirectorEmail,OLD.dInfo);
end IF;
END 

create trigger ch_sa_stabad after insert on checking_in for each ROW
begin
DECLARE count INT(3);
SET count=(SELECT times FROM salary WHERE staId=New.staId);
if(count>=3) then
update staff_bad set sta_remarks='旷工' where staId=NEW.staId;
end IF;
SET count=count+1;
update salary set times=count where staId=NEW.staId;
END 

create trigger ch_de_sa_stabad after delete on checking_in for each ROW
begin
update staff_bad set sta_remarks=NULL where staId=OLD.staId;
update salary set times=0 where staId=OLD.staId;
END

create trigger mon_in_stago_sa AFTER insert
on monthrecord for each ROW
begin
update staff_good set sta_remarks=NEW.re_remarks where staId=NEW.staId;
update salary set award=NEW.award where staId=NEW.staId;
END


create trigger mon_update_stago_sa AFTER update
on monthrecord for each ROW
begin
update staff_good set sta_remarks=NEW.re_remarks where staId=NEW.staId;
update salary set award=NEW.award where staId=NEW.staId;
END


create trigger mon_dele_stago_sa AFTER delete
on monthrecord for each ROW
begin
update staff_good set sta_remarks=NULL where staId=OLD.staId;
update salary set award=0 where staId=old.staId;
END

create trigger sa_in_sta AFTER insert
on salary for each ROW
begin
update staff set stSalary=NEW.origin_salary where stId=NEW.staId;
END

REATE
TRIGGER `duanxin_before_insert` BEFORE INSERT ON `t_duanxin`
FOR EACH ROW BEGIN
DECLARE msgcount INT(10);
SET msgcount=(SELECT COUNT(*) FROM t_duanxin WHERE FIND_IN_SET(new.to_phone, to_phone) AND new.content=content);
　　IF msgcount>0 THEN
　　DELETE FROM t_duanxin WHERE id=new.id;
　　END IF;

END;

create trigger trigger_order
BEFORE INSERT ON orders FOR EACH ROW
BEGIN
DECLARE var int;
DECLARE mesg varchar(20);
SELECT pnum INTO var FROM product where pid=NEW.pid;
IF var<NEW.onum 
   THEN  SELECT XXXX INTO mesg;
ELSE 
   UPDATE product SET pnum=pnum-NEW.onum where pid=NEW.pid;
END IF; 
END

CREATE TRIGGER u AFTER INSERT ON department FOR EACH ROW
BEGIN
DECLARE s1 VARCHAR(40)character set utf8;
DECLARE s2 VARCHAR(20) character set utf8;
SET s2 = " is created";
SET s1 = CONCAT(NEW.dName,s2);     
END 