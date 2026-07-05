## Definition of Done (aplica a TODA issue antes de pasar a Done)

Una issue solo se cierra si su PR cumple:

- [ ] La lógica nueva tiene **unit tests** que la cubren, con dependencias externas fakeadas (sin red, sin DB). Si el core no se puede testear pasando fakes, es un fallo de diseño (acoplamiento core/adapter), no una excusa para no testear.
- [ ] Todo lo que toca **DB o red real** tiene **integration test** con Testcontainers (Postgres real levantado y destruido por el test).
- [ ] Cada **cliente de API externa** (Spotify; luego MusicBrainz/Discogs/Last.fm) tiene **contract test** con fixtures grabadas — CI no depende de la API viva.
- [ ] `ruff check`, `mypy` (strict) y `pytest` en verde en CI.
- [ ] Sin secretos ni datos sensibles en logs ni en el audit (audit by hash).
- [ ] Frontera core/adapter respetada: sin lógica de dominio en adapters/middleware; sin `os.getenv` ni clientes globales en el core; salida tipada, no `str` en el core.
- [ ] Documentación mínima actualizada (README de la carpeta si aplica).
- [ ] Revisión: al menos 1 aprobación + CI verde. Sin commits directos a `main`. Conventional commits.