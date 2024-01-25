


Repository độc lập miền và lưu trữ sql (dễ tuhaajn tiện Unit testing and Mocking)

Repository trong ORM

<!--https: //images.viblo.asia/fd4b10a0-f1b1-4ed1-9bd1-578c871820ae.png-->

, gprc rabitmq đồng bộ hay k, ít hay nhiều như pub sub

# 5. Service Mesh, CICD, microfe, API gateway, cache redis, log xử lí lỗi,

<!---->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https: //dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

https: //helpsme.misa.vn/2020/kb/quan-ly-hoa-don-dien-tu/

https: //helpsme.misa.vn/2022/kb/quy-trinh-nghiep-vu-hddt-theo-nghi-dinh-123-2020-nd-cp/

https: //www.meinvoice.vn/tin-tuc/3442/nhung-nghiep-vu-co-ban-cua-hoa-don-dien-tu-xac-thuc/

<!---->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https: //dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

https: //helpsme.misa.vn/2020/kb/quan-ly-hoa-don-dien-tu/

https: //helpsme.misa.vn/2022/kb/quy-trinh-nghiep-vu-hddt-theo-nghi-dinh-123-2020-nd-cp/

https: //www.meinvoice.vn/tin-tuc/3442/nhung-nghiep-vu-co-ban-cua-hoa-don-dien-tu-xac-thuc/

<!--Thay thế = NULL-->

<!--Bị thay thế = NULL-->

<!--quy trình tương tự như lập mới hóa đơn giá trị gia tăng.-->

<!---->

<!--@Chú ý ở đồ án này:-->

<!--Sử dụng hàm ngẫu nhiên (tỉ lệ 10%) cho trường hợp "Mã số thuế không tồn tại."-->

<!--Sử dụng hàm ngẫu nhiên tạo tên cho Tên NNT vì em không có thông tin đăng ký thực tế của NNT.-->

<!--Sử dụng hàm ngẫu nhiên trong bảng CSDL cho "Mã cơ quan thuế quản lý" và "Tên cơ quan thuế quản lý"-->

Bảng CSDL này được em thu thập dữ liệu từ trang web CƠ SỞ DỮU DANH MỤC DÙNG CHUNG (https: //dmdc.mof.gov.vn/khai-thac-pb/co-quan-thue)

<!--!Mã thuế số-chi nhánh-->

<!--Mã captcha không đúng.-->

<!--0107001729-->

dấu chấm cuối câu .

email=>Thư điện tử

Viết tắt NNT...

<!--Validtae-->

Điều kiện

<!---->

Chỉ dùng 1 loại hóa đơn vì em thấy tương tự.

Loại hóa đơn: + Hóa đơn giá trị gia tăng + Hóa đơn bán hàng + Hóa đơn bán tài sản công + Hóa đơn bán hàng dự trữ quốc gia + Hóa đơn khác + Chứng từ điện tử được sử dụng và quản lý như hóa đơn

<!--Nghiệp vụ của bài toán chính-->

Video Viettel

<!--@Chú ý ở đồ án này:-->

Mã giao dịch điện tử = Mã số thuế + Thời gian đăng kí

Sử dụng hàm ngẫu nhiên (tỉ lệ 10%) cho trường hợp từ chối.

<!--Phân tích và thiết kế-->

Xác định các tính năng cần thiết và các yêu cầu kỹ thuật tạo ra một thiết kế hệ thống hoặc kiến trúc đáp ứng.

<!---->

<!--Các công nghệ phổ biến trong kiến trúc vi dịch vụ-->

Docker container.....

Docker container.....

Docker container.....

Docker container.....

[](0.9.KetLuan_TongKet.md)

[](_.TaiLieuThamKhao.md)

<!--RxJS-->

https: //www.youtube.com/watch? v=6jSk_J7RA24

https: //www.youtube.com/watch? v=Jc-lGeDuphg

https: //www.youtube.com/watch? v=UXHzxX4png0

https: //www.youtube.com/watch? v=glZs4QFfwbc
 

# 6. Container và Container Orchestration

Docker and Kubernetes (often abbreviated as K8s) are two powerful technologies commonly used in the world of container orchestration and deployment. Let's briefly explore each of them:

1. **Docker: **

- **Containerization Technology: ** Docker is a platform that enables developers to automate the deployment of applications inside lightweight, portable containers. Containers encapsulate an application and its dependencies, ensuring consistency across different environments.

- **Docker Image: ** A Docker image is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, and system tools.

- **Docker Container: ** An instance of a Docker image is called a Docker container. Containers run consistently across different environments, providing a consistent and reproducible runtime.

2. **Kubernetes (K8s): **

- **Container Orchestration: ** Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It abstracts the underlying infrastructure and provides a unified API to manage clusters of containers.

- **Key Concepts: ** Kubernetes introduces concepts like Pods (smallest deployable units), Deployments (managing replica sets and rolling updates), Services (networking abstraction for pods), and more.

- **Scaling and Load Balancing: ** Kubernetes can scale applications horizontally by adding or removing instances (pods) based on demand. It also provides load balancing to distribute traffic across multiple instances.

**How Docker and Kubernetes Work Together: **

- Docker is used to create containerized applications, and Kubernetes manages the orchestration of these containers.

- Developers package their applications into Docker containers, which can run locally on a developer's machine.

- Kubernetes then takes these containers and orchestrates their deployment, ensuring high availability, scalability, and easy management.

**Common Commands: **

- **Docker Commands: **

- `docker build`: Build a Docker image from a Dockerfile.

- `docker run`: Create and start a Docker container.

- `docker push`: Push a Docker image to a registry.

- **Kubernetes Commands: **

- `kubectl apply`: Apply configurations to a cluster.

- `kubectl get`: Display information about resources.

- `kubectl describe`: Show detailed information about a resource.

- `kubectl scale`: Scale the number of replicas in a deployment.

**Integration: **

- Docker images are often stored in container registries like Docker Hub.

- Kubernetes can pull these Docker images from a registry and deploy them onto the cluster.

In summary, Docker is used to containerize applications, and Kubernetes is used to orchestrate and manage these containers in a production environment. Together, they provide a powerful and scalable solution for deploying and managing containerized applications.

# 7. Broker Pattern dịch vụ dicovery

https: //www.youtube.com/watch? v=UXHzxX4png0

# 8. Dependency Injection

# 9. Kết luận tổng kết

Kiến trúc vi dịch vụ, với việc tách biệt hệ thống thành các thành phần nhỏ quản lý độc lập, mang lại tính linh hoạt và khả năng mở rộng.

thiết kế hướng miền giúp xây dựng mô hình chính xác và nhất quán của lĩnh vực kinh doanh, giúp đảm bảo rằng hệ thống phản ánh đúng yêu cầu nghiệp vụ.

# 10. Tài liệu tham khảo

http

<!--Căn cứ pháp lý-->

<!--Thông tư 78/2021/TT-BTC-->

<!--Nghị định 123/2020/NĐ-CP-->

<!--Thông tư 78/2021/TT-BTC-->

Thông tư 32/2011/TT-BTC: https: //thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Thong-tu-32-2011-TT-BTC-huong-dan-ve-khoi-tao-phat-hanh-su-dung-hoa-don-dien-tu-120233.aspx

<!--https: //vanban.chinhphu.vn/default.aspx? pageid=27160&docid=99887-->

Thông tư 78/2021/TT-BTC: https: //thuvienphapluat.vn/van-ban/Tai-chinh-nha-nuoc/Thong-tu-78-2022-TT-BTC-du-toan-ngan-sach-Nha-nuoc-2023-547888.aspx

<!--https: //vanban.chinhphu.vn/default.aspx? pageid=27160&docid=204200-->

Nghị định 123/2020/NĐ-CP: https: //thuvienphapluat.vn/van-ban/Ke-toan-Kiem-toan/Nghi-dinh-123-2020-ND-CP-quy-dinh-hoa-don-chung-tu-445980.aspx

<!--https: //vanban.chinhphu.vn/? pageid=27160&docid=201365-->

<!--https: //hoadondientu.gdt.gov.vn-->

<!--https: //en.wikipedia.org/wiki/kiến trúc vi dịch vụ-->

<!--https: //en.wikipedia.org/wiki/Domain-driven_design-->

<!--https: //kiến trúc vi dịch vụ.io-->

<!--2. Richardson, C. (2018). _kiến trúc vi dịch vụ Patterns: With Examples in Java._ O'Reilly Media.-->

<!--https: //refactoring.guru/design-mẫu/catalog-->

<!--“thiết kế hướng miền: Tackling Complexity in the Heart of Software”, nhà xuất bản AddisonWesley, ISBN: 0-321-12521-5.-->

<!--1. Evans, E. (2003). _thiết kế hướng miền: Tackling Complexity in the Heart of Software._ Addison-Wesley.-->

<!--https: //learn.microsoft.com/en-us/archive/msdn-magazine/2009/february/best-practice-an-introduction-to-domain-driven-design-->

<!--https: //learn.microsoft.com/en-us/dotnet/architecture/kiến trúc vi dịch vụ/kiến trúc vi dịch vụ- thiết kế hướng miền -cqrs-mẫu/ thiết kế hướng miền -oriented-kiến trúc vi dịch vụ-->

<!--3. Newman, S. (2015). _Building kiến trúc vi dịch vụ: Designing Fine-Grained Systems._ O'Reilly Media.-->

<!--https: //github.com/GoogleCloudPlatform/kiến trúc vi dịch vụ-demo-->

<!--https: //www.uml-diagrams.org-->

<!--https: //www.udemy.com/course/domain-driven-design-and-kiến trúc vi dịch vụ-->

https: //viblo.asia/p/tim-hieu-ve-kiến trúc vi dịch vụ-phan-1-kiến trúc vi dịch vụ-la-gi-63vKjVjyK2R

https: //viblo.asia/p/domain-driven-design-phan-1-mrDGMOExkzL














