# FRA502_Project_Phase3_62340500025
Author : Tanakorn Teerabundit 62340500025

วิธีการใช้งาน

1.ทำการ cd Project/DiffBot/src

2.ทำการ source $HOME/Project/DiffBot/devel/setup.bash

3.ทำการ launch ไฟล์ต่างๆ

    3.1ทำการ roslaunch banks_dd bankgazebo.launch หลังจากนั้นจะขึ้น

    3.2ทำการ roslaunch banks_dd bankspawn.launch

    3.3ทำการ roslaunch banks_dd banknavigation.launch

    3.4ทำการ roslaunch banks_dd bankrviz.launch

    3.5ทำการ rosrun banks_dd Goaltostation.py

4.เมื่อ rosrun banks_dd Goaltostation.py ใน Terminal จะขึ้นว่า Going to Charger_Station For Sethome นั้นเเปลว่าหุ่นยนต์จะไปที่ state เเรกสุดนั้นคือหุ่นยนต์จะกลับ Charger_Station เพื่อรอการเสิร์ฟกาเเฟ

5.เมื่อหุ่นยนต์ถึง Charger_Station จะขึ้นว่า Reached At The Charger_Station หลังจากนั้นจะขึ้น Say The Room That You Want เพื่อรอคำสั่งว่าจะให้ไปเสิร์ฟกาเเฟที่ห้องไหน

6.คำสั่งที่ใช้จะมีทั้งหมด 4 คำสั่ง 

    6.1พูดว่า "ห้อง 1" หุ่นยนต์ก็จะเดินไปเสิร์ฟกาเเฟที่ห้อง 1 เเละขึ้นที่ terminal ว่า Going toRoom_1
    
    6.2พูดว่า "ห้อง 2" หุ่นยนต์ก็จะเดินไปเสิร์ฟกาเเฟที่ห้อง 2 เเละขึ้นที่ terminal ว่า Going toRoom_2
    
    6.3พูดว่า "ห้อง 3" หุ่นยนต์ก็จะเดินไปเสิร์ฟกาเเฟที่ห้อง 3 เเละขึ้นที่ terminal ว่า Going toRoom_3
    
    6.4พูดว่า "ห้องใหญ่" หุ่นยนต์ก็จะเดินไปเสิร์ฟกาเเฟที่ห้องใหญ่ เเละขึ้นที่ terminal ว่า Going toRoom_main

7.เมื่อหุ่นยนต์มาถึงห้องตามคำสั่งที่ terminal ก็จะขึ้นว่า Reached At The Room That You Want เเละที่ terminal จะขึ้นว่า Customer Can Keep The Coffee เพื่อบอกว่าลูกค้าสามารถหยิบกาเเฟได้เลยเเละจะเเจ้งเตือนต่อไปอีกว่า The Robot Will Back To The Charger_Station In 10 Seconds เพื่อบอกผู้บริโภคว่าหุ่นยนต์จะกลับ Charger_Station อีก 10 วินาที

8.เมื่อครบ 10 วินาทีหุ่นยนต์จะกลับ Charger_Station โดยจะขึ้นเเจ้งเตือนว่า Going to Charger_Station For Sethome

9.เมื่อหุ่นยนต์ถึง Charger_Station ที่ Terminal จะขึ้นเเจ้งเตือนว่า Reached At The Charger_Station เพื่อรอคำสั่งในการเสิร์ฟกาเเฟต่อไป

