



**Quản lý vòng đời của các đối tượng miền**

Việc quản lý vòng đời các đối tượng trong miền không hề đơn giản, nếu như làm không đúng sẽ có thể gây ảnh hưởng đến việc mô hình hóa miền.

**Mẫu tổng hợp (Aggregate)**

<!--Tính tương đồng (Aggregate)-->

Mẫu tổng hợp là một nhóm các thực thể và đối tượng giá trị được xem như một tổng thể thống nhất từ ​​góc độ dữ liệu và khái niệm miền.

<!--Hãy để tôi giải thích điều này bằng một minh họa.-->

Một tập hợp bao gồm một nhóm tổng hợp còn được gọi là thực thể gốc.

Thực thể gốc này có một danh tính duy nhất từ ​​phối cảnh miền.

Phần thứ hai của tập hợp là cụm, được hình thành bởi ranh giới của tập hợp.

Trong ranh giới này, có thể không có hoặc nhiều thực thể tổng hợp và đối tượng giá trị. Các đối tượng trong cụm này hoặc đối tượng trong ranh giới được gọi là đối tượng bên trong hoặc đối tượng con.

![](image-4.png)

Aggregate phải cung cấp các giao diện để vận hành trên các đối tượng bên trong.

đảm bảo rằng tất cả hành vi cần thiết để vận hành trên đối tượng bên trong được hiển thị dưới dạng các hàm của đối tượng gốc tổng hợp.

![](image-5.png)




<!-- % Aggregate -->

<!-- Aggregate: https://ddd-practitioners.com/home/glossary/aggregate/ -->

<!-- [[Aggregate]] A cluster of associated objects that are treated as a unit for the purpose of data changes. External references are restricted to one member of the AGGREGATE, designated as the root. A set of consistency rules applies within the AGGREGATE’S boundaries. -->

<!-- State Stored Aggregates : https://ddd-practitioners.com/state-stored-aggregate -->
