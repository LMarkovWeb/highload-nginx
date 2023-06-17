start:
	@docker compose up -d

stop:
	@docker compose down

re:
	@docker compose down && docker compose up -d

logs:
	@docker compose logs -tf

tank-nginx:
	@docker exec -ti tank yandex-tank -c load_nginx.yaml

tank-app:
	@docker exec -ti tank yandex-tank -c load_app.yaml

nginx-enter:
	@docker exec -ti nginx /bin/bash
