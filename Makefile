start:
	@docker compose up -d

stop:
	@docker compose down

restart:
	@docker compose down && docker compose up -d

logs:
	@docker compose logs -tf

tank:
	@docker exec -ti tank yandex-tank -c load.yaml