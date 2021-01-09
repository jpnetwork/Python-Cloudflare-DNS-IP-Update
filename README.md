# Python-Cloudflare-DNS-IP-Update
อัพเดท Cloudflare DNS IP Address ด้วย Python

ขั้นตอนการใช้งาน
1. ทำการชี้โดเมนเนมของเราไปใช้บริการ DNS Service ของ Cloudflare ให้เรียบร้อย
2. ให้ทำการสร้าง DNS A record ขึ้นมา 1 ชื่อ เช่น home.mydomain.com
3. หลังจากนั้นเราจะทำการเขียน Script Python (โค้ดอยู่ด้านล่าง) ให้ทำการอัพเดท IP Address ของเน็ตในบ้าน ให้กับ home.mydomain.com
4. ตั้ง Cron job ให้ทำการการ Run script นี้เป็นระยะๆ
5. ต่อไปก็สามารถเรียกใช้งานมายังอุปกรณ์หรือระบบในบ้านผ่าน home.mydomain.com ได้ตลอดไป

ในส่วนของการใช้งาน หลังจากกำหนดค่าตัวแปรต่างๆ เสร็จให้ทำการรันโค้ด 1 ครั้งก่อน เพื่อหาค่า RECORD_ID ของ dns record ที่เราจะทำการอัพเดท IP เมื่อได้ค่า id มาแล้ว ก็เอามาใส่ให้กับตัวแปร RECORD_ID ได้เลยครับ

โค้ดนี้ดัดแปลงมาจากลิ้งค์นี้นะครับ https://www.nathanvangheem.com/posts/2018/07/15/auto-update-cloudflare-dns.html
