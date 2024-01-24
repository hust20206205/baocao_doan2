<!-- Thiết kế hệ thống thêm phần multi tenantcy schema giúp nhiều công ty khác cùng sử dụng hệ thống -->

Table Tenants {
id int [pk, increment]
name varchar(255) [not null]
<!-- LastEditedWhen -->
}

<!-- Thiết kế hệ thống  người dùng quản lý quyền truy cập dựa trên vai trò (RBAC - Role-Based Access Control) -->

Table Users {
id int [pk, increment]
username varchar(255) [not null]
password varchar(255) [not null]
role_id int [ref: > Roles.id]
tenant_id int [ref: > Tenants.id]
}

Table Roles {
id int [pk, increment]
name varchar(255) [not null]
tenant_id int [ref: > Tenants.id]
}

Table UserRoles {
user_id int [ref: > Users.id]
role_id int [ref: > Roles.id]
}

Table Permissions {
id int [pk, increment]
name varchar(255) [not null]
tenant_id int [ref: > Tenants.id]
}

Table RolePermissions {
role_id int [ref: > Roles.id]
permission_id int [ref: > Permissions.id]
}
<!-- Thiết kế hệ thống  người dùng quản lý quyền truy cập dựa trên vai trò (RBAC - Role-Based Access Control) -->
