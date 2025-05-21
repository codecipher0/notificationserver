A basic notification server

Test using curl/postman
Ex:
curl -X POST http://localhost:8000/notify \
  -H "Content-Type: application/json" \
  -d '{"channel":"email","recipient":"jay@example.com","message":"Hello World!"}'