variable "do_token" {
  type = string
  description = "digital ocean token to login"
}

variable "droplet_name" {
  description = "Name of the droplet"
  default     = "games-pool"

}

variable "app_image_tag" {
  description = "Docker image tag for the application"
}

variable "db_password" {
  description = "Database password"
}
variable "db_user" {
  description = "Database user"
}
variable "db_host" {
  description = "Database host"
}
variable "db_name" {
  description = "Database name"
}
variable "db_port" {
  description = "Database port"
}

